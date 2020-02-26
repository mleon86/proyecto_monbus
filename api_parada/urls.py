from django.urls import path
from .views import Datos_ParadaSave, Datos_MapaList, Solic_Asiento

urlpatterns = [
	path('datos_parada_save/', Datos_ParadaSave.as_view(), name = 'datos_parada_save'),
	path('maps_consulta/<nombre>/', Datos_MapaList.as_view(), name = 'maps_list'),
	path('solic_asiento/<nombre>/', Solic_Asiento.as_view(), name = 'solic_asiento')
	#solicitud_asiento_especial
	]