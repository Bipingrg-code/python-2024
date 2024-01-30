from django.shortcuts import render
from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Student
from rest_framework import status
from rest_framework import viewsets

class StudentViewSet(viewsets.ViewSet):
    def list(self,request):
        student = Student.objects.all()
        serializer = StudentSerializer(student,many=True)
        return Response(serializer.data)
    def retrieve(self,request,pk=None):
        id = pk
        if id is not None:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
            
    def create(self,request):
        data = request.data
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data created.!'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk=None):
        id = pk
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data updated'},status=status.HTTP_202_ACCEPTED)
        return Response(serializer.error,status=status.HTTP_202_ACCEPTED)
    
    def partial_update(self,request,pk=None):
        id = pk
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student,data=request.data,partial=True)
        if id is not None:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_206_PARTIAL_CONTENT)
        return Response(serializer.error,status=status.HTTP_202_ACCEPTED)
    
    def destroy(self,request,pk=None):
        id = pk
        student = Student.objects.get(id=id)
        student.delete()
        return Response({'msg':'deleted.!'},status=status.HTTP_200_OK)
        

# # Create your views here.
# model viewsets
# class StudentViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer = StudentSerializer
# read only model viewsets
# class StudentViewReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Student.objects.all()
#     serializer = StudentsSerializer