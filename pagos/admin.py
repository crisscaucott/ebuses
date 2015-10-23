from django.contrib import admin
from .models import Plan,Pago,Banner

# Register your models here.
@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
	list_display = ['nombre', 'duracion', 'limite_imgs']

@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
	list_display = ['empresa', 'plan', 'fecha_inicio', 'fecha_termino']

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
	list_display = ['url_img', 'pago']