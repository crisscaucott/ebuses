from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.core.urlresolvers import reverse, reverse_lazy
# import pprint
from django.contrib.auth import logout
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.db.models import Q
from .models import EmpresaBuses, Recorrido, Parada, Clasificacion, ParadaRecorrido

# Create your views here.
class EmpresaBusesListView(ListView):
	model = EmpresaBuses
	template_name = 'buses/empresa_view.html'

	def logout_view(request):

		print "LOGOUTTT"

	# FILTRAR 
	def get_queryset(self):
		q = super(EmpresaBusesListView, self).get_queryset()
		Recorrido.objects.filter(empresa_bus__activo=True)
		return q.filter(activo = True)

	def get_context_data(self, **kwargs):
	    context = super(EmpresaBusesListView, self).get_context_data(**kwargs)
	    context['paradas'] = Parada.objects.values('id', 'nombre').all()
	    return context

empresa_list = EmpresaBusesListView.as_view()

class EmpresaBusesCreateView(CreateView):
	model = EmpresaBuses
	template_name = 'buses/empresa_create.html'
	fields = '__all__'
	success_url = reverse_lazy('empresa_list')

empresa_create = EmpresaBusesCreateView.as_view()

class EmpresaBusesUpdateView(UpdateView):
	model = EmpresaBuses
	template_name = 'buses/empresa_create.html'
	fields = '__all__'
	success_url = reverse_lazy('empresa_list')

empresa_update = EmpresaBusesUpdateView.as_view()

class EmpresaBusesDeleteView(UpdateView):
	model = EmpresaBuses
	template_name = 'buses/empresa_create.html'
	success_url = reverse_lazy('empresa_list')

	# SOFT DELETE
	# def delete(self, request, *args, **kwargs):
	#     """
	#     Calls the delete() method on the fetched object and then
	#     redirects to the success URL.
	#     """
	#     self.object = self.get_object()
	#     success_url = self.get_success_url()
	#     self.object.deleted_at = True
	#     self.object.save()
	#     return HttpResponseRedirect(success_url)

# class Login(LoginView):

# 	def get_success_url(self):
#         # Explicitly passed ?next= URL takes precedence
#         ret = (get_next_redirect_url(self.request,
#                                      self.redirect_field_name)
#                or self.success_url)
#         return ret
# logn = 

class EmpresasBusesIndex(ListView):
	model = EmpresaBuses
	template_name = 'buses/empresas.html'

	def get_context_data(self, **kwargs):
		context = super(EmpresasBusesIndex, self).get_context_data(**kwargs)
		context['empresas'] = EmpresaBuses.objects.all()
		# ESTRELLAS DATA
		context['estrellas'] = [1,2,3,4,5]

		return context
		
empresasBusesIndex = EmpresasBusesIndex.as_view()


def getRecorridoByEmpresa(request):

	if request.method == 'POST':
		recorridos = Recorrido.objects.select_related().filter(empresa_bus_id = request.POST.get("id"))
		print vars(recorridos)

		return render(request, 'buses/partials/recorridos.html', {'recorridos': recorridos})
	# return render(request, '/', {'object' : fotosCazaRecompensas})

def calificarEmpresa(request):

	if request.method == 'POST':

		# pprint.pprint(request.user)
		# print vars(request)

		if request.user.is_authenticated():
			# print request.user.id
			calificacion = Clasificacion(
				estrellas = request.POST.get('estrellas'),
				comentario = request.POST.get('comentario'),
				usuario = request.user,
				recorrido = Recorrido.objects.get(id = request.POST.get('id_recorrido'))
				)

			calificacion.save()
			# print vars(calificacion)
			return render(request, 'buses/alerts/success.html', {'msg': 'Recorrido calificado creada exitosamente.'})

		else:
			response = render(request, 'buses/alerts/error.html', {'msg': 'Debes iniciar sesion para poder calificar.'})
			response.status_code = 400
			return response
			# response = JsonResponse({'msg': 'Debes iniciar sesion para poder calificar.'})
			# return response
			
def calificacionesByUsuario(request):

	if request.method == 'GET':
		calificaciones = Clasificacion.objects.select_related().filter(usuario = request.user).all

		return render(request, 'buses/calificaciones.html', {'calificaciones' : calificaciones})
	elif request.method == 'POST':
		detalle = Clasificacion.objects.select_related().filter(id = request.POST.get('id'))
		estrellas = [1,2,3,4,5]

		return render(request, 'buses/partials/calificacion_detalle.html', {'cal_detalle': detalle, 'estrellas' : estrellas})

def borrarCalificacion(request):
	if request.method == 'POST':
		res = Clasificacion.objects.filter(id = request.POST.get('id')).delete()
		calificaciones = Clasificacion.objects.select_related().filter(usuario = request.user).all
		response = {
			'cal' : render_to_string('buses/partials/calificaciones.html', {'calificaciones' : calificaciones, 'token' : request.COOKIES['csrftoken']}),
			'msg' : render_to_string('buses/alerts/success.html', {'msg' : 'La calificacion ha sido eliminada exitosamente.'}),
		}

		return JsonResponse(response)

def getDetalleByCalificacion(request):

	if request.method == 'POST':
		res = Clasificacion.objects.filter(id = request.POST.get('id')).update(estrellas = request.POST.get('estrellas'), comentario = request.POST.get('comentario'))

		return render(request, 'buses/alerts/success.html', {'msg': 'Calificacion editada exitosamente.'})

# /buses/empresas/consulta/ORIGEN/DESTINO/
def recorridosByParadas(request, origen = None, destino = None):

	if request.method == 'GET':
		ids = []
		for i in ParadaRecorrido.objects.raw(""" select pr.id, pr.recorrido_id
				from parada as p, parada_recorrido as pr
				where p.id = pr.`parada_id` and 
				(p.nombre = %s or p.nombre = %s)
				group by recorrido_id
				having count(recorrido_id) > 1 """, [origen, destino]):
			ids.append(i.recorrido_id)

		if len(ids) == 0:	# SI NO HAY RECORRIDOS
			paradas = Parada.objects.values('id', 'nombre').all()
			return render(request, 'buses/empresa_view.html', {'msg_err': 'No hay recorridos con origen y destino elegidos.', 'paradas' : paradas})
		else:
			# recorridos = ParadaRecorrido.objects.select_related().filter(recorrido__in = ids).all()
			recorridos = Recorrido.objects.select_related().filter(id__in = ids).all()
			return render(request, 'buses/recorridos_empresa.html', {'recorridos' : recorridos, 'origen' : origen, 'destino': destino})
	elif request.method == 'POST':
		print "AJAX"
		paradas = ParadaRecorrido.objects.select_related().filter(recorrido = request.POST.get('id')).exclude(parada = request.POST.get('origen')).exclude(parada = request.POST.get('destino'))
		if not paradas:
			response = {
				'res' : 'No hay paradas intermedias.'
			}
		else:
			response = {'res' : render_to_string('buses/partials/paradas_inter.html', {'paradas' : paradas})}

		return JsonResponse(response)
		

			


