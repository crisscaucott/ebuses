from django.db import models

# Create your models here.
class Plan(models.Model):
	nombre = models.CharField(max_length = 20)
	duracion = models.SmallIntegerField()
	limite_imgs = models.SmallIntegerField()

	class Meta:
		db_table = 'plan'

class Pago(models.Model):
	empresa = models.ForeignKey('buses.EmpresaBuses')
	plan = models.ForeignKey(Plan)
	fecha_inicio = models.DateTimeField()
	fecha_termino = models.DateTimeField()

	class Meta:
		db_table = 'pago'


class Banner(models.Model):
	url_img = models.CharField(max_length = 200)
	pago = models.ForeignKey(Pago)

	class Meta:
		db_table = 'banner'
