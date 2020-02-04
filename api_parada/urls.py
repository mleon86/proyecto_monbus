from django.urls import path
from .views import Datos_ParadaSave, Datos_MapaList

urlpatterns = [
	path('datos_parada_save/', Datos_ParadaSave.as_view(), name = 'datos_parada_save'),
	path('maps_consulta/<nombre>/', Datos_MapaList.as_view(), name = 'maps_list')

	]