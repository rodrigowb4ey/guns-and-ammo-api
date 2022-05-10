from django.shortcuts import render
from rest_framework import viewsets
from municao.models import Municao
from municao.serializers import MunicaoSerializer


class MunicaoViewSet(viewsets.ModelViewSet):
    queryset = Municao.objects.all()
    serializer_class = MunicaoSerializer