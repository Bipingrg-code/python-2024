from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
# Create your views here.
def students_details(request):
    if request.method == 'GET':
        json_data =  request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        
        id = pythondata.get('id',None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')

    student = Student.objects.all()
    serializer = StudentSerializer(student,many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')  
        

       

    