from .models import Employee
from rest_framework import serializers

class EmployeeSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=50)
    email=serializers.EmailField()
    password=serializers.CharField(max_length=30)
    phone=serializers.CharField(max_length=10)

    def create(self,validated_data):
        print("create method called....")
        return Employee.objects.create(**validated_data)
    
    #add this for PUT request
    def update(self,employee,validated_data): 
        newEmployee=Employee(**validated_data)
        newEmployee.id=employee.id;
        newEmployee.save() 
        return newEmployee   

class UserSerializer(serializers.Serializer):
    first_name=serializers.CharField(max_length=50)
    last_name=serializers.CharField(max_length=50)
    email=serializers.EmailField()
    password=serializers.CharField(max_length=50)



