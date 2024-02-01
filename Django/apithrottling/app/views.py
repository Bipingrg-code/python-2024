from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from app.teacherapithrottle import TeacherRateThrottle
from rest_framework import viewsets
# Create your views here.
class StudentVewSetAPI(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [AnonRateThrottle,TeacherRateThrottle]
    # throttle_classes = [AnonRateThrottle,UserRateThrottle]
    