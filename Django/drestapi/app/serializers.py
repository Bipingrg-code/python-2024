from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    address = serializers.CharField(max_length=200)
    
    def create(self,validate_data):
        return Student.objects.create(**validate_data)