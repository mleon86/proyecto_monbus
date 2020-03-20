from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .views import Bus_DatosSave, RaspberryBusConsulta, Viaje_Inicio_Id_Viaje, Bus_DatosUpdate, Bus_DatosUpdateCreate, PrepararAsiento, ConsultaItinerario

urlpatterns = [
	path('datos_bus_save/', Bus_DatosSave.as_view(), name = 'datos_bus_save'),#historico
	path('datos_bus_update/<viaje_inicio>/', Bus_DatosUpdate.as_view(), name = 'datos_bus_update'),#para actualizar
	path('datos_bus_update/<viaje_inicio>/create/', Bus_DatosUpdateCreate.as_view(), name = 'datos_bus_update_create'),#primera creacion
	path('datos_rasp_consulta/<serial_rasp_bus>/', RaspberryBusConsulta.as_view(), name = 'datos_rasp_consulta'),
	path('inicio_viaje/', Viaje_Inicio_Id_Viaje.as_view(), name = 'inicio_viaje'),
	path('preparar_asiento/<viaje_inicio>/', PrepararAsiento.as_view(), name = 'preparar_asiento'),
	path('consulta_itinerario/<linea_id>/', ConsultaItinerario.as_view(), name = 'consulta_itinerario')
	#preparacion_para_asiento
	]