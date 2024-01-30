from django.shortcuts import render
from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Student
from rest_framework.views import APIView
from rest_framework import status



# Create your views here.
class StudentAPI(APIView):
    def get(self, request, format=None,pk=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        student = Student.objects.all()
        serializer = StudentSerializer(student,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        data = request.data
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data created.!'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk,format=None):
        id = pk
        data = request.data
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":'Data updated'},status=status.HTTP_206_PARTIAL_CONTENT)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk,format=None,):
        id = pk
        data = request.data
       
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":'Partial Data updated'},status=status.HTTP_206_PARTIAL_CONTENT)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,format=None,pk=None):
        id = pk
        if id is not None:
            student = Student.objects.get(id=id)
            student.delete()
            return Response({'msg':'data deleted successfully.!'},status=status.HTTP_201_CREATED)
        return Response({'msg':'Request invalid'},status=status.HTTP_400_BAD_REQUEST)
    
    
        
        
        