from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from municao.models import Municao
from municao.serializers import MunicaoSerializer


class MunicaoViewSet(viewsets.ModelViewSet):
    queryset = Municao.objects.all()
    serializer_class = MunicaoSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['marca', 'modelo']
    ordering_fields = ['valor_estimado']
    filterset_fields = ['calibre', 'objeto']