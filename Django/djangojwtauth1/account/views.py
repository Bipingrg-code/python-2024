from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import UserRegSerializer, UserLoginSerializer, UserProfileSerializer, UserPasswordChangeSerializer,UserSendPasswordRestEmailSerializer,UserPasswordRestSerializer
from django.contrib.auth import authenticate
from .renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

# token generate

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# Create your views here.
# user registration view


class UserRegView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        data = request.data
        serializer = UserRegSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({'token': token, 'msg': 'Registrations Successfully.!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# user login view


class UserLoginView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({'token': token, 'msg': 'Login Successfully.!'}, status=status.HTTP_200_OK)
            else:
                return Response({'errors': {'non_field_errors': ['Email or Password is not Valid.!']}}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# user profile viewset
class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
# User Change Password

class UserPasswordChangeView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self,request,format=None):
        serializer =  UserPasswordChangeSerializer(data=request.data,context={'user':request.user})
        if serializer.is_valid(raise_exception=True): 
            return Response({'msg':'Password Changed Successfully.!'},status=status.HTTP_200_OK) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Password rest email
class UserSendPasswordRestEmailView(APIView):
    renderer_classes = [UserRenderer]
    def post(self,request,format=None):
        serializer = UserSendPasswordRestEmailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'Password Reset link sent. Please check your email!'},status=status.HTTP_200_OK) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
          
        
class UserPasswordRestView(APIView):
    renderer_classes = [UserRenderer]
    def post(self,request,uid,token, format=None):
        serializer =UserPasswordRestSerializer(data=request.data,context={'token':token,'uid':uid})
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'Password reset successfully.!'},status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)