#from django.shortcuts import render

from rest_framework import generics

from .models import Bus_Datos
from .serializers import Bus_DatosSerializer

# Create your views here.
class Bus_DatosSave(generics.CreateAPIView):
	serializer_class = Bus_DatosSerializer