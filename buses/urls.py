from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.empresa_list, name = 'empresa_list'),
	url(r'^crear/$', views.empresa_create, name = 'empresa_create'),
	url(r'^editar/(?P<pk>\d+)/$', views.empresa_update, name = 'empresa_update'),
	url(r'^empresas/$', views.empresasBusesIndex, name = 'empresas_buses_index'),
	url(r'^empresas/recorridos/$', views.getRecorridoByEmpresa, name = 'get_recorrido_by_empresa'),
	url(r'^empresas/calificar/$', views.calificarEmpresa, name = 'calificar_empresa'),
	url(r'^usuario/calificaciones/$', views.calificacionesByUsuario, name = 'calificaciones_by_usuario'),
	url(r'^usuario/calificaciones/editar/$', views.getDetalleByCalificacion, name = 'get_detalle_by_calificacion'),
	url(r'^usuario/calificaciones/borrar/$', views.borrarCalificacion, name = 'borrar_calificacion'),
]