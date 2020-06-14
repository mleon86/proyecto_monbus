from django.urls import path
from .views import Datos_ParadaSave, Datos_MapaList, SolicAsientoListCreate, SolicAsientoDetail, Info_Parada, RaspParada, SolicAsientoUpdateListCreate , SolicAsientoUpdateDetail, SiniestroListCreate

urlpatterns = [
	path('datos_rasp_consulta/<serial_rasp_parada>/', RaspParada.as_view(), name = 'rasp_parada_consulta'),
	path('info_parada/<nombre>/',Info_Parada.as_view(), name = 'info_parada'),
	path('datos_parada_save/', Datos_ParadaSave.as_view(), name = 'datos_parada_save'),
	path('maps_consulta/<nombre>/', Datos_MapaList.as_view(), name = 'maps_list'),
	path('solic_asiento/', SolicAsientoListCreate.as_view(), name = 'solic_asiento_list_create'),
	path('solic_asiento/<nombre>/', SolicAsientoDetail.as_view(), name = 'solic_asiento_detail'),
	path('solic_asiento_update/', SolicAsientoUpdateListCreate.as_view(), name = 'solic_asiento_update'),
	path('solic_asiento_update/<nombre>/', SolicAsientoUpdateDetail.as_view(), name = 'solic_asiento_update_detail'),
	path('siniestro/', SiniestroListCreate.as_view(), name = 'siniestro_list_create'),
	#solicitud_asiento_especial
	]