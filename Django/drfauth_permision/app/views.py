from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
# from rest_framework.authentication import BasicAuthentication
from rest_framework.authentication import SessionAuthentication
from .custompermission import MyPermission
# from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions
# Create your views here.
class StudentApiViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAdminUser]
    # permission_classes = [DjangoModelPermissions]
    authentication_classes = [SessionAuthentication]
    permission_classes = [MyPermission]
    

