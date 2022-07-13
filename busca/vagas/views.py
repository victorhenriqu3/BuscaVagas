from django.shortcuts import redirect, render

from .forms import EmployeeForm

from .models import Employee

# Create your views here.
def employeeList(request):
  employees = Employee.objects.all()
  return render(request,"employeeList.html",{'employees':employees})

def employeeCreate(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                return redirect('employee-list')  
            except:
                pass
    else:  
        form = EmployeeForm()  
        
    return render(request,'employeeCreate.html',{'form':form})  
