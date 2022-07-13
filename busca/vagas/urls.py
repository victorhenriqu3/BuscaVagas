from . import views
from django.urls import path


urlpatterns = [
    path('employee-list',views.employeeList, name='employee-list')
]
