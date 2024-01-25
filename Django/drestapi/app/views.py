from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer 
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
import io
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# single student's data
def student_detail(request, pk):
    stu = Student.objects.get(id=pk)
    serializer = StudentSerializer(stu)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

def students_list(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return JsonResponse(serializer.data, safe=False)

# for exempting the csrf token from the third-party api
@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        parsed_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=parsed_data)
        
        if serializer.is_valid():
            serializer.save()
            response_data = {'msg': 'Data created!'}
            json_response = JSONRenderer().render(response_data)
            return HttpResponse(json_response, content_type='application/json')

        json_response = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_response, status=400, content_type='application/json')

    return JsonResponse({'msg': 'Invalid request method'}, status=405)
