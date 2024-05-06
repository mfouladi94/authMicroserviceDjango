from rest_framework import serializers
from .models import *

class UserNameSignupSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=50, required=True)
    password1 = serializers.CharField(min_length=5, max_length=50, required=True)
    password2 = serializers.CharField(min_length=5, max_length=50, required=True)

class LoginSerializerInput(serializers.Serializer):
    email = serializers.CharField(max_length=50, required=True)
    password = serializers.CharField(min_length=5, max_length=50, required=True)
    
    
    
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'