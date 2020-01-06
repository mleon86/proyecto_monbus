from django.urls import path
from .views import Datos_ParadaSave

urlpatterns = [
	path('datos_parada_save/', Datos_ParadaSave.as_view(), name = 'datos_parada_save')
	]