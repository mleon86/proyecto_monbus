from django.urls import path
from .views import Datos_ParadaSave, Datos_MapaList, Solic_Asiento, Info_Parada, RaspParada, BorrarSolicAsiento

urlpatterns = [
	path('datos_rasp_consulta/<serial_rasp_parada>/', RaspParada.as_view(), name = 'rasp_parada_consulta'),
	path('info_parada/<nombre>/',Info_Parada.as_view(), name = 'info_parada'),
	path('datos_parada_save/', Datos_ParadaSave.as_view(), name = 'datos_parada_save'),
	path('maps_consulta/<nombre>/', Datos_MapaList.as_view(), name = 'maps_list'),
	path('solic_asiento/<nombre>/', Solic_Asiento.as_view(), name = 'solic_asiento'),
	path('borrar_solic_asiento/<parada>/', BorrarSolicAsiento.as_view(), name = 'borrar_solic_asiento')
	#solicitud_asiento_especial
	]