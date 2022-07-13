from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(db_column='name', max_length=100, blank=False)
    description = models.TextField(db_column='description', max_length=1000)
    dailyRate = models.DecimalField(db_column='daily',decimal_places=2,max_digits=5, blank=False)
    birthday = models.DateField(db_column='bday', blank=False)
    cpf = models.CharField(db_column='cpf' ,max_length=11, blank=False)
    email = models.EmailField(db_column='email', blank=False)
