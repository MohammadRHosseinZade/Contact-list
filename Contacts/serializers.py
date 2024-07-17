from rest_framework import serializers
from re import compile, search


class GenerateContactSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length = 15)
    full_name = serializers.CharField(max_length = 128)
    address = serializers.CharField(required=False)
    description = serializers.CharField(required=False) 

    def validate_phone_number(self, value): 
        match = search(pattern=compile(r"^(\+98)?(9\d{9})$"), string=value) 
        if match:
            return value
        raise serializers.ValidationError("Phone number format is invalid. Example: +989213006869")
    