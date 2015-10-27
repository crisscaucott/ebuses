from django.contrib import admin
from .models import EmpresaBuses,Parada,Recorrido,ParadaRecorrido,Usuario,Clasificacion

# Register your models here.
@admin.register(EmpresaBuses)
class EmpresaBusesAdmin(admin.ModelAdmin):
	list_display = ['nombre', 'url', 'telefono', 'direccion']

@admin.register(Parada)
class ParadaAdmin(admin.ModelAdmin):
	list_display = ['nombre', 'gps_lat', 'gps_lon']

@admin.register(Recorrido)
class RecorridoAdmin(admin.ModelAdmin):
	list_display = ['nombre', 'precio', 'hora_llegada', 'hora_salida', 'origen', 'destino', 'empresa_bus']

@admin.register(ParadaRecorrido)
class ParadaRecorridoAdmin(admin.ModelAdmin):
	list_display = ['recorrido', 'parada']

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
	list_display = ['nombre']

@admin.register(Clasificacion)
class ClasificacionAdmin(admin.ModelAdmin):
	list_display = ['estrellas', 'comentario', 'usuario', 'recorrido']
