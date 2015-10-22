from django.contrib import admin
from .models import Persona

@admin.register(Persona)
class PersonAdmin(admin.ModelAdmin):
	list_display = ('id', 'nombre', 'apellido')

# Register your models here.
