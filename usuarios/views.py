from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Usuario
from .serializers import UsuarioSerializer

class UsuarioConsulta(generics.ListAPIView):
	permission_classes = ()
	serializer_class = UsuarioSerializer
	def get_queryset(self):
		usuario = self.kwargs['usuario']
		return Usuario.objects.filter(usuario__username=usuario)