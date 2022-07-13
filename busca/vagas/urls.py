from . import views
from django.urls import path


urlpatterns = [
    path('',views.employeeList, name='employee-list'),
    path('employee-create',views.employeeCreate, name='employee-create')
]
