from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .models import Student
from .serailizers import StudentSerializers
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.
# @api_view(['GET','POST'])
# def studentapi(request):
#     if request.method == 'GET':
#         return Response({'msg':'Hello Rest Framework'})
#     if request.method == 'POST':
#         print(request.data)
#         return Response({'msg':'Hello Rest Framework POST'})
@api_view(['GET','POST','PUT','PATCH','DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def studentAPI(request, pk=None):
    if request.method == 'GET':
        # print(request.data)
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializers(stu)
            return Response(serializer.data)
        
        stu = Student.objects.all()
        serializer = StudentSerializers(stu,many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        data = request.data
        serializer = StudentSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Created SuccessFully.!'}
            return Response(res,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':
        data = request.data
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializers(stu,data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Complete Data updated successfully.!'},status=status.HTTP_206_PARTIAL_CONTENT)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PATCH':
        data = request.data
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializers(stu,data=data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Partial Data updated successfully.!'},status=status.HTTP_206_PARTIAL_CONTENT)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        id = pk
        data = Student.objects.get(id=id)
        data.delete()
        return Response({'msg':'Data Deleted Successfully.!'},status=status.HTTP_200_OK)
    
        
        
       
        
   
    

