from django.shortcuts import render
from rest_framework import viewsets
from utils import serializers
from utils.models import User, Calibre
from utils.serializers import CalibreSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CalibreViewSet(viewsets.ModelViewSet):
    queryset = Calibre.objects.all()
    serializer_class = CalibreSerializer