from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status,parsers
from django.forms.models import model_to_dict
from drf_spectacular.utils import extend_schema
from .serializers import GenerateContactSerializer, UpdateContactDetail
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from .models import (ContactDetail, UserContactsDetail, Phone2ContactDetail, PhoneNumber)

class GeneratePhoneContactView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [parsers.JSONParser, parsers.FormParser]
    @extend_schema(
        description='Generating a Contact for a user',
        request=GenerateContactSerializer,
        responses={200: 'application/json'}
    )
    def post(self, request, *args, **kwargs):
        serializer = GenerateContactSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = self.request.user
                phone_obj, phone_created = PhoneNumber.objects.get_or_create(phone_number = serializer.validated_data['phone_number'])
                detail_obj = ContactDetail.objects.create(
                                            full_name = serializer.validated_data['full_name'],
                                            address = serializer.validated_data['address'],
                                            description = serializer.validated_data['description'])   
                phone2detail = Phone2ContactDetail.objects.create(phone_id = phone_obj, detail_id = detail_obj) 
                UserContactsDetail.objects.create(user_id = user, phone_detail_id = phone2detail)
                return Response({'success': 'Contact generated successfully'}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': f'Error generating contact: {e}'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
class UserContactlistView(APIView):
    permission_classes = [IsAuthenticated]
    @extend_schema(
        description='Generating a Contact for a user',
        responses={200: 'application/json'}
    )
    def get(self, request):
            try:
                user = request.user
                obj_list = UserContactsDetail.objects.filter(user_id = user)
                result = []
                for obj in obj_list:
                    result.append({"detail" : model_to_dict(obj.phone_detail_id.detail_id),
                    "number" : obj.phone_detail_id.phone_id.phone_number})
                return Response({'data': result}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': f'Error generating contact: {e}'}, status=status.HTTP_400_BAD_REQUEST)   
    

class ContactInfoUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [parsers.JSONParser, parsers.FormParser]
    @extend_schema(
        description='Updating a Contact details',
        request=UpdateContactDetail,
        responses={200: 'application/json', 400: 'application/json', 404: 'application/json'}
    )
    def put(self, request, detail_id):
        serializer = UpdateContactDetail(data=request.data)
        if serializer.is_valid():
            try: 
                user = request.user
                obj = UserContactsDetail.objects.filter(user_id = user).get(phone_detail_id__detail_id__id = detail_id).phone_detail_id
                obj.detail_id.full_name = serializer.validated_data['full_name']
                obj.detail_id.description = serializer.validated_data['description']
                obj.detail_id.address = serializer.validated_data['address']
                obj.detail_id.save()
                return Response({'data': model_to_dict(obj.detail_id)}, status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                return Response({'error': 'Contact detail not found'}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({'error': f'Error generating contact: {e}'}, status=status.HTTP_400_BAD_REQUEST)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    

class DeleteContactView(APIView):
    permission_classes = [IsAuthenticated]
    @extend_schema(
        description='Delete a contact detail',
        responses={200: 'application/json', 400: 'application/json', 404: 'application/json'}
    )
    def delete(self, request, detail_id):
        try:
            user = request.user
            contact_detail = UserContactsDetail.objects.get(user_id=user, phone_detail_id__detail_id__id=detail_id).phone_detail_id
            contact_detail.detail_id.delete()
            return Response({'success': "Contact deleted"}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'error': 'Contact detail not found'}, status=status.HTTP_404_NOT_FOUND)
        except PermissionDenied:
            return Response({'error': 'You do not have permission to delete this contact'}, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({'error': f'Error deleting contact: {e}'}, status=status.HTTP_400_BAD_REQUEST)