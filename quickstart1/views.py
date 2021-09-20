from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import Employee
from .serializers import EmployeeSerializer,UserSerializer
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework .parsers import JSONParser
from rest_framework import status

# Create your views here.
@csrf_exempt
def employeeListView(request):
    if request.method=='GET':
        employees=Employee.objects.all()  #get all model Emoloyee fields.
        serializer=EmployeeSerializer(employees,many=True)
        return JsonResponse(serializer.data,safe=False)

    elif request.method=='POST':
        jsonData=JSONParser().parse(request)  #read the data
        serializer=EmployeeSerializer(data=jsonData)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,safe=False) 
        else:
            return JsonResponse(serializer.errors,safe=False)

#primary key based operation
@csrf_exempt
def employeeDetailView(request,pk):
    try:
        employee=Employee.objects.get(pk=pk)   
        #return JsonResponse("Employee +str(pk)",safe=False)
    except Employee.DoesNotExist:       
        return HttpResponse(status=404) 

    if request.method =='GET':
        serializer=EmployeeSerializer(employee)
        return JsonResponse(serializer.data ,safe=False)  
    elif request.method =='PUT':
        jsonData=JSONParser().parse(request)  #read the data
        serializer=EmployeeSerializer(employee,data=jsonData)  #convert into json object
        if serializer.is_valid(): #if fields is valid
            serializer.save()   #saved it
            return JsonResponse(serializer.data,safe=False) 
        else:
            return JsonResponse(serializer.errors,safe=False)
    elif request.method =='DELETE':
        employee.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

def userListView(request):
    users=User.objects.all()
    serializer=UserSerializer(users,many=True)
    return JsonResponse(serializer.data ,safe=False) 


      
class ProductList(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    def get(self,request):
        if request.user.is_authenticated(): 
            userCompanyId = request.user.get_profile().companyId
            products = Product.objects.filter(company = userCompanyId)
            serializer = ProductSerializer(products,many=True)
            return Response(serializer.data)

    def post(self,request):
        serializer = ProductSerializer(data=request.DATA, files=request.FILES)
        if serializer.is_valid():
            serializer.save()
            return Response(data=request.DATA)