
from django.forms import DateField,ModelForm
from .widgets import DatePickerInput
from .models import Employee

class EmployeeForm(ModelForm):
  class Meta:
    model = Employee
    fields = '__all__'
    
  Data_de_Nascimento = DateField(widget=DatePickerInput())
