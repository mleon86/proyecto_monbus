from django.urls import path
from .views import UsuarioConsulta

urlpatterns = [
	path('consulta_id/<usuario>/', UsuarioConsulta.as_view(), name = 'consulta_id'),
	#logueo
	]