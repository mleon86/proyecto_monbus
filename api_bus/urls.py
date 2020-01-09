from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .views import Bus_DatosSave

urlpatterns = [
	path('datos_bus_save/', Bus_DatosSave.as_view(), name = 'datos_bus_save')
	]