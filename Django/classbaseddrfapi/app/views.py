from django.shortcuts import render
from .models import Student
import io
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import JsonResponse, HttpResponseBadRequest,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
# Create your views here.

@method_decorator(csrf_exempt,name='dispatch')
class StudentAPI(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        parse_data = JSONParser().parse(stream) 

        id = parse_data.get("id", None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(data=stu)
            json_data = JSONRenderer().render(serializer).decode('utf-8')
            return JsonResponse(json_data, safe=False)

        student = Student.objects.all()
        serializer = StudentSerializer(data=student, many=True)
        json_data = JSONRenderer().render(serializer).decode('utf-8')
        return JsonResponse(json_data, safe="False")

    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            exist_email = Student.objects.filter(email = data['email']).exists()
            if exist_email:
                error_msg = {'email': ['This email address is already in use.']}
                json_err = JSONRenderer().render({'error': error_msg})
                return HttpResponse(json_data, content_type="application/json")
            serializer.save()
            res = {'msg': 'data created.!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type="application/json")
        else:
            json_err = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_err, content_type="application/json")

    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        id = data.get("id")
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            res = {"msg": "data updated.!"}
            json_res = JSONRenderer().render(res)
            return JsonResponse(json_res, safe=False)
        else:
            json_err = JSONRenderer().render(serializer.errors).decode('utf-8')
            return HttpResponseBadRequest(json_err, safe=False)

    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        id = data.get("id")
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {"msg": "Data Deleted Successfully..!"}
        json_res = JSONRenderer().render(res).decode('utf-8')
        return JsonResponse(json_res,safe=False)
