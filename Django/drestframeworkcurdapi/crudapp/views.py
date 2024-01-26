from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse,HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt 
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




# for exempting the csrf token from the third-party api
@csrf_exempt
def students_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        
        if serializer.is_valid():
            email_exists = Student.objects.filter(email=python_data['email']).exists()
            
            if email_exists:
                error_msg = {'email': ['This email address is already in use.']}
                json_err = JSONRenderer().render({'error': error_msg})
                return JsonResponse(json_err, safe=False)
                
            serializer.save()
            res = {'msg':'data created.!'}
            json_res = JSONRenderer().render(res).decode('utf-8')
            return JsonResponse(json_res,safe=False)
        
        
        else:
            json_err = JSONRenderer().render(serializer.error).decode('utf-8')
            return HttpResponseBadRequest(json_err,safe=False)
        
@csrf_exempt
def students_update(request):
    if request.method == "PUT":
        json_data = request.body
        stream = io.BytesIO(json_data)
        parse_data= JSONParser().parse(stream)
        id = parse_data.get('id')
        stu = Student.objects.get(id=id)
        # To update complete data - Required All data from front end/client
        # serializer = StudentSerializer(stu,data=parse_data)
        # For The Partial update  needs to be id 
        serializer = StudentSerializer(stu, data=parse_data, partial=True)   
        
        if serializer.is_valid():
            serializer.save()
            res = {"msg":"Data updated successfully..!"}
            json_res = JSONRenderer().render(res).decode('utf-8')
            return JsonResponse(json_res,safe=False)
        json_data = JSONRenderer().render(serializer.error).decode('utf-8')
        return JsonResponse(json_data, safe=False)
@csrf_exempt       
def students_delete(request):
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        parse_data = JSONParser().parse(stream)
        id = parse_data.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {"msg": "Data Deleted Successfully..!"}
        json_res = JSONRenderer().render(res).decode('utf-8')
        return JsonResponse(json_res,safe=False)
        
    