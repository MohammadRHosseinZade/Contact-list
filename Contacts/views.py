from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status,parsers
from drf_spectacular.utils import extend_schema
from .serializers import GenerateContactSerializer
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