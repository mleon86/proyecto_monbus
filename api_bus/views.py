#from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


from .models import Bus_Datos
from .serializers import Bus_DatosSerializer

# Create your views here.
class Bus_DatosSave(generics.CreateAPIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = Bus_DatosSerializer