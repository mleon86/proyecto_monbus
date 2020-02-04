from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .views import Bus_DatosSave, RaspberryBusConsulta, Viaje_Inicio_Id_Viaje

urlpatterns = [
	path('datos_bus_save/', Bus_DatosSave.as_view(), name = 'datos_bus_save'),
	path('datos_rasp_consulta/<serial>/', RaspberryBusConsulta.as_view(), name = 'datos_rasp_consulta'),
	path('inicio_viaje/', Viaje_Inicio_Id_Viaje.as_view(), name = 'inicio_viaje')
	]