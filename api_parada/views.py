#from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Datos_Parada
from .serializers import Datos_ParadaSerializer

# Create your views here.
class Datos_ParadaSave(generics.CreateAPIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = Datos_ParadaSerializer