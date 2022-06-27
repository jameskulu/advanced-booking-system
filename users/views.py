from django.contrib import auth
from django.conf import settings
from django.http import JsonResponse

from rest_framework import status, filters
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView 

import jwt
from .serializer import  LoginSerializer,RegistrationSerializer
from .models import Account


class RegisterView(GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data = {
                'user':serializer.data
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        email = request.data.get('email', '')
        password = request.data.get('password', '')
        serializer = LoginSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        if user := auth.authenticate(email=email, password=password):
            auth_token = jwt.encode(
                {'id': user.id}, settings.JWT_SECRET_KEY)
            serializer = RegistrationSerializer(user)
            data = {
                'user': serializer.data,
                'token': auth_token
            }
            return Response(data, status=status.HTTP_200_OK)

        return Response({'details': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)