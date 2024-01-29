from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    roll = serializers.IntegerField()
    address = serializers.CharField(max_length=200)
    email = serializers.EmailField(max_length=100)
    
    def create(self,validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.roll = validated_data.get('roll',instance.roll)
        instance.address = validated_data.get('address',instance.address)
        instance.email = validated_data.get('email',instance.email)
        instance.save()
        return instance