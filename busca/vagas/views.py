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
            except Exception as e:
                pass
    else:  
        form = EmployeeForm()  
        
    return render(request,'employeeCreate.html',{'form':form})  

def employeeDelete(request ,id):
    employees = Employee.objects.get(id=id)
    try:
        employees.delete()
    except:
        pass
    return redirect('employee-list')

def employeeUpdate(request, id):  
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(initial={'Nome':  employee.Nome,'Valor_da_Diária': employee.Valor_da_Diária, 'CPF': employee.CPF, 'Email': employee.Email, 'Data_de_Nascimento': employee.Data_de_Nascimento, 'Descrição_das_Atividades': employee.Descrição_das_Atividades  })
    if request.method == "POST":  
        form = EmployeeForm(request.POST, instance=employee)  
        if form.is_valid():  
            try:  
                form.save() 
                return redirect('/')  
            except Exception as e: 
                pass    
    return render(request,'employeeUpdate.html',{'form':form}) 
