from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .views import Bus_DatosSave, RaspberryBusConsulta

urlpatterns = [
	path('datos_bus_save/', Bus_DatosSave.as_view(), name = 'datos_bus_save'),
	path('datos_rasp_consulta/<serial>/', RaspberryBusConsulta.as_view(), name = 'datos_rasp_consulta')
	]