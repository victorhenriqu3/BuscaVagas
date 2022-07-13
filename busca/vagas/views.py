from django.shortcuts import render

from .models import Employee

# Create your views here.
def employeeList(request):
  employees = Employee.objects.all()
  return render(request,"employeeList.html",{'employees':employees})
