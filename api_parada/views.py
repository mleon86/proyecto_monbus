#from django.shortcuts import render

from rest_framework import generics

from .models import Datos_Parada
from .serializers import Datos_ParadaSerializer

# Create your views here.
class Datos_ParadaSave(generics.CreateAPIView):
	serializer_class = Datos_ParadaSerializer