from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.empresa_list, name = 'empresa_list'),
	url(r'^crear/$', views.empresa_create, name = 'empresa_create'),
	url(r'^editar/(?P<pk>\d+)/$', views.empresa_update, name = 'empresa_update')
]