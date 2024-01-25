
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserProfile
from .serializers import UserProfileSerializer, UserRegistrationSerializer

class UserProfileView(APIView):
    def get(self, request, *args, **kwargs):
        user_profile = UserProfile.objects.get(id=request.user.id)
        serializer = UserProfileSerializer(user_profile)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        user_profile = UserProfile.objects.get(id=request.user.id)
        serializer = UserProfileSerializer(user_profile, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserRegistrationView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

