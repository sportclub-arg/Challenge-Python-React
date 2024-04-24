from rest_framework import viewsets
from .serializer import UsuarioSerializer
from .models import Usuario
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

# Create your views here.
