from datetime import datetime
from django.db import models

# Create your models here.
class Employee(models.Model):
    Nome = models.CharField(db_column='name', max_length=100, blank=False)
    Descrição_das_Atividades= models.TextField(db_column='description', max_length=500, default='')
    Valor_da_Diária= models.DecimalField(db_column='daily',decimal_places=2,max_digits=5, blank=False)
    Data_de_Nascimento = models.DateField(db_column='bday', default= datetime.now() )
    CPF = models.CharField(db_column='cpf' ,max_length=11, blank=False)
    Email = models.EmailField(db_column='email', blank=False)
