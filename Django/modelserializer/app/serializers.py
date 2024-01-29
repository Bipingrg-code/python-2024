from rest_framework import serializers
from .models import Student
# def start_with_r(value):
#     if value[0].lower() != 'b':
#         raise serializers.ValidationError('Name Shoud be start with B')
class StudentSerializer(serializers.ModelSerializer):
    # name = Serializers.CharField(read_only=True)
    class Meta:
        model = Student
        fields = ['name','roll','address']
        # extra_kwargs = {'name':{'read_only':True}}
     # Field Level Validation
    def validate_roll(self,value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return value
    
    # Object level Validation
    
    # def validate(self,data):
    #     name = data.get("name")
    #     address = data.get("address")
                
    #     if name.lower() == "bipin" and address.lower() != 'kathmandu':
    #         raise serializers.ValidationError('address must be kathmandu')
    #     return data
        
    