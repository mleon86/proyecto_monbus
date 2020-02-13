from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .views import Bus_DatosSave, RaspberryBusConsulta, Viaje_Inicio_Id_Viaje, Bus_Datos_UpdateList, Bus_DatosUpdate, Bus_DatosUpdateCreate

urlpatterns = [
	path('datos_bus_update_list/', Bus_Datos_UpdateList.as_view(), name = 'datos_bus_list'),
	path('datos_bus_save/', Bus_DatosSave.as_view(), name = 'datos_bus_save'),
	path('datos_bus_update/<viaje_inicio>/', Bus_DatosUpdate.as_view(), name = 'datos_bus_update'),
	path('datos_bus_update/<viaje_inicio>/create/', Bus_DatosUpdateCreate.as_view(), name = 'datos_bus_update_create'),
	path('datos_rasp_consulta/<serial_rasp_bus>/', RaspberryBusConsulta.as_view(), name = 'datos_rasp_consulta'),
	path('inicio_viaje/', Viaje_Inicio_Id_Viaje.as_view(), name = 'inicio_viaje')
	]