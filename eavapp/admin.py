from django.contrib import admin
from eav.forms import BaseDynamicEntityForm
from eav.admin import BaseEntityAdmin
from .models import Patient
class PatientAdminForm(BaseDynamicEntityForm):
    model = Patient

class PatientAdmin(BaseEntityAdmin):
    form = PatientAdminForm

admin.site.register(Patient, PatientAdmin)
