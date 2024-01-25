from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    roll = serializers.IntegerField()
    address = serializers.CharField(max_length=200)
    email = serializers.EmailField(max_length=200)
