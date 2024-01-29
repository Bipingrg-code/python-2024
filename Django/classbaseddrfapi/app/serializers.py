from rest_framework import serializers
from .models import Student
import re

# validators
def start_with_r(value):
    if value[0].lower() != 'b':
        raise serializers.ValidationError('Name Shoud be start with B')
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200, validators=[start_with_r])
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
    
    # Field Level Validation
    def validate_roll(self,value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return value
    
    # Object level Validation
    
    def validate(self,data):
        name = data.get("name")
        address = data.get("address")
                
        if name.lower() == "bipin" and address.lower() != 'kathmandu':
            raise serializers.ValidationError('address must be kathmandu')
        return data
        
    
    