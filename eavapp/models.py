from django.db import models
import eav
from django.contrib import admin
from eav.forms import BaseDynamicEntityForm
from eav.admin import BaseEntityAdmin



class Patient(models.Model):

    titulo = models.CharField(verbose_name='Título',max_length=100,null=True,blank=True)



eav.register(Patient)