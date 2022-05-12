from rest_framework import viewsets
from armas.models import Arma
from armas.serializers import ArmaSerializer


class ArmaViewSet(viewsets.ModelViewSet):
    queryset = Arma.objects.all()
    serializer_class = ArmaSerializer