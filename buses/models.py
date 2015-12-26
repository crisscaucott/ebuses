from django.db import models
import allauth.app_settings
# Create your models here.
class EmpresaBuses(models.Model):
	nombre = models.CharField(max_length = 40)
	url = models.URLField(max_length = 100)
	telefono = models.CharField(max_length = 20)
	direccion = models.CharField(max_length = 40)
	activo = models.BooleanField(default=True)

	class Meta:
		db_table = 'empresa_buses'

	def __unicode__(self):
		return self.nombre

class Parada(models.Model):
	nombre = models.CharField(max_length = 30)
	gps_lat = models.FloatField()
	gps_lon = models.FloatField()

	class Meta:
		db_table = 'parada'

class Recorrido(models.Model):
	nombre = models.CharField(max_length = 40)
	precio = models.PositiveIntegerField()
	hora_llegada = models.TimeField()
	hora_salida = models.TimeField()
	origen = models.ForeignKey(Parada, null = True, related_name = 'origen')
	destino = models.ForeignKey(Parada, null = True, related_name = 'destino')
	empresa_bus = models.ForeignKey(EmpresaBuses)
	dia = models.DateTimeField(null = True)

	class Meta:
		db_table = 'recorridos'


class ParadaRecorrido(models.Model):
	recorrido = models.ForeignKey(Recorrido)
	parada = models.ForeignKey(Parada)

	class Meta:
		db_table = 'parada_recorrido'

class Usuario(models.Model):
	nombre = models.CharField(max_length = 40)
	apellido = models.CharField(max_length = 40)
	rut = models.CharField(max_length = 12)
	
	class Meta:
		db_table = 'usuario'


class Clasificacion(models.Model):
	#empresa = models.ForeignKey(EmpresaBuses)
	estrellas = models.PositiveSmallIntegerField()
	comentario = models.TextField()
	# usuario = models.ForeignKey(Usuario)
	usuario = models.ForeignKey(allauth.app_settings.USER_MODEL)
	recorrido = models.ForeignKey(Recorrido)

	class Meta:
		db_table = 'clasificacion'

