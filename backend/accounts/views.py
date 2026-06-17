import jwt
import os
import logging

from datetime import datetime, timedelta

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, GenericAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import SignupSerializer, PasswordForgotSerializer, PasswordResetSerializer, CustomTokenObtainPairSerializer, UserSerializer, UserUpdateSerializer, AddressSerializer
from .models import User
from . import emails
from drfecom.keys import TokenTypes
from .mixins import GeneralUserPermissionMixin, StaffEditorPermissionMixin

"""
Used for create-only endpoints. Provides a post method handler.
"""
class SignupView(CreateAPIView):
    serializer_class = SignupSerializer

    def post(self, request, *args, **kwargs): # Use perform_create instead from serializer
        user_instance = None
        user_email = request.data.get('email')
        try:
            user_instance = User.objects.get(email=user_email)
            if user_instance.is_active:
                return Response({'message': 'This account is already verified, now you can use this account!'}, status=status.HTTP_208_ALREADY_REPORTED) 
        except Exception:
            pass

        serializer = None
        if user_instance is not None:
            serializer = SignupSerializer(user_instance, data=request.data)
        else:
            serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save(is_active = False)

            payload = {
                "type": TokenTypes.REGISTER.value,
                "email": user_email,
                "id": user.id,
                "exp": datetime.utcnow() + timedelta(minutes=20)
            }

            encoded_token = jwt.encode(payload, os.getenv('JSON_TOKEN_SECRET'), algorithm="HS256")

            emails.SendEmail.send_signup_confirmation(request, user, encoded_token)
            return Response({'message': 'a verification url is been sent to your email'}, status=status.HTTP_201_CREATED) 

        return Response({'message': 'Provide valid data in order to '}, status=status.HTTP_406_NOT_ACCEPTABLE) 
    

class VerifySignupView(GenericAPIView):
    serializer_class = UserSerializer
    # def perform_create(self, serializer):
        # queryset = SignupRequest.objects.filter(user=self.request.user)
        # if queryset.exists():
        #     raise ValidationError('You have already signed up')
        # serializer.save(user=self.request.user)

    def put(self, request, token):
        try:
            decoded_token = jwt.decode(token, os.getenv('JSON_TOKEN_SECRET'), algorithms=["HS256"])
            if decoded_token['type'] != TokenTypes.REGISTER.value:
                return Response({'message': 'Invalid token'}, status=status.HTTP_406_NOT_ACCEPTABLE)                 
            
            user_instance = User.objects.get(email=decoded_token['email'])
            if user_instance is None:
                return Response({'message': 'No user registered, with this email'}, status=status.HTTP_406_NOT_ACCEPTABLE)                 
            if user_instance.is_active:
                return Response({'message': 'Account already activated.'}, status=status.HTTP_208_ALREADY_REPORTED)
            
            user_instance.is_active = True 
            user_instance.save()
            return Response({'message': 'Account activated successfully.'}, status=status.HTTP_200_OK)
        except jwt.exceptions.ExpiredSignatureError:
            return Response({'message': 'The token had been expired'}, status=status.HTTP_406_NOT_ACCEPTABLE) 
        except Exception as e:
            print("Error")
            logging.error(e)
            return Response({'message': str(e)}, status=status.HTTP_406_NOT_ACCEPTABLE)  
        

class ForgotPasswordView(GenericAPIView):
    serializer_class = PasswordForgotSerializer
    
    def put(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data.get('user')
        user_email = user.email

        payload = {
                "type": TokenTypes.RESET_PASSWORD.value,
                "email": user_email,
                "id": user.id,
                "exp": datetime.utcnow() + timedelta(minutes=20)
            }
        encoded_token = jwt.encode(payload, os.getenv('JSON_TOKEN_SECRET'), algorithm="HS256")
        
        emails.SendEmail.send_reset_password_email(request=request, user_email=user_email, token=encoded_token)
        return Response({'detail': 'Password reset email sent.'}, status=status.HTTP_200_OK)


class PasswordResetView(GenericAPIView):
    serializer_class = PasswordResetSerializer

    def put(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'token': kwargs.get('token')}) # Generic views - Returns a serializer instance.
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'detail': 'Password has been reset.'}, status=status.HTTP_200_OK)
    

class SigninTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class UserObtainView(GeneralUserPermissionMixin, RetrieveAPIView):
    serializer_class = UserSerializer
    
    def get_queryset(self):
        decoded_token = jwt.decode(self.request.headers['Authorization'].split(' ')[1], os.getenv('JSON_TOKEN_SECRET'), algorithms=["HS256"])
        queryset = User.objects.filter(id =decoded_token['user_id'])
        return queryset
    
    def get_object(self):
        queryset = self.get_queryset()
        filter = {}
        obj = get_object_or_404(queryset, **filter)
        return obj
    
class UserUpdateView( GeneralUserPermissionMixin, UpdateAPIView):
    serializer_class = UserUpdateSerializer
    queryset = User.objects.all()
    # update user with a new address and update address data inside UpdateAPIView
    def perform_update(self, serializer):
        user = self.get_object()
        address_data = self.request.data.get('address', {})

        instance = serializer.save()
        address_data['user'] = user.id

        # Update or create address
        address_serializer = None
        if address_data.get('id') and address_data.get('id') is not None and address_data.get('id') != '':
            address_qs = user.address.filter(id=address_data.get('id'))
            if address_qs.exists():
                address = address_qs.first()
                address_serializer = AddressSerializer(address, data=address_data, partial=True)
            else:
                address_serializer = AddressSerializer(data=address_data)
        else:
            address_serializer = AddressSerializer(data=address_data)
        
        address_serializer.is_valid(raise_exception=True)
        address_serializer.save()
    
class UserListView(StaffEditorPermissionMixin, ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    



        














