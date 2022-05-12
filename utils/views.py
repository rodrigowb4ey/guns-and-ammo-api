from rest_framework import viewsets
from utils.models import ObjetoTipo, Calibre, Objeto
from utils.serializers import (
    CalibreSerializer,
    ObjetoSerializer,
    ObjetoTipoSerializer,
    UserSerializer,
)


class CalibreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Calibre.objects.all()
    serializer_class = CalibreSerializer


class ObjetoTipoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ObjetoTipo.objects.all()
    serializer_class = ObjetoTipoSerializer


class ObjetoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Objeto.objects.all()
    serializer_class = ObjetoSerializer
