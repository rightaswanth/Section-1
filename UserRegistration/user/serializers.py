
from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model =UserProfile
        fields =['id', 'username', 'email', 'bio']  

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model =UserProfile
        fields =['username', 'email', 'password']
        extra_kwargs ={'password': {'write_only': True}}
