from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.core.urlresolvers import reverse, reverse_lazy

from .models import EmpresaBuses

# Create your views here.
class EmpresaBusesListView(ListView):
	model = EmpresaBuses
	template_name = 'buses/empresa_view.html'

	# FILTRAR 
	# def get_queryset(self):
	# 	q = super(EmpresaBusesListView, self).get_queryset(self)
	# 	return q.filter(deleted_at = False)

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
