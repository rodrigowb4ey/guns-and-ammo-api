from django import views
from django.shortcuts import render
from rest_framework import viewsets
from utils import serializers
from utils.models import ObjetoTipo, User, Calibre, Objeto
from utils.serializers import CalibreSerializer, ObjetoSerializer, ObjetoTipoSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CalibreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Calibre.objects.all()
    serializer_class = CalibreSerializer

class ObjetoTipoViewSet(viewsets.ModelViewSet):
    queryset = ObjetoTipo.objects.all()
    serializer_class = ObjetoTipoSerializer

class ObjetoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Objeto.objects.all()
    serializer_class = ObjetoSerializer