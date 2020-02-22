from django.shortcuts import render
from rest_framework.views import APIView
from .models import Employees
from .serializers import EmployessSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class EmployeesView(APIView):

    def get(self,request):
        employees = Employees.objects.all()
        employeeSerializer = EmployessSerializer(employees, many = True)
        return Response(employeeSerializer.data)

    @staticmethod
    def key_validation(data, keys):
        for i in keys:
            print(data)
            if i not in data:
                return False
        else:
            return True

    def post(self,request):
        temp ={}
        data_keys = ["firstname" , "lastname", "emp_id" ]
        if not self.key_validation(request.data,data_keys):
            return Response("Valid headers not present in the request", status=status.HTTP_400_BAD_REQUEST)
        employeeSerializer = EmployessSerializer(data=request.data)
        if employeeSerializer.is_valid():
            employeeSerializer.save()
            temp["success"] = "User added successfully"
            return Response(temp, status=status.HTTP_201_CREATED)
        return Response(employeeSerializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request):
        pass
