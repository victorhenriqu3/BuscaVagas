from . import views
from django.urls import path


urlpatterns = [
    path('',views.employeeList, name='employee-list'),
    path('employee-create',views.employeeCreate, name='employee-create'),
    path('employee-update/<int:id>',views.employeeUpdate, name='employee-update'),
    path('employee-delete/<int:id>', views.employeeDelete, name='employee-delete'),
]

