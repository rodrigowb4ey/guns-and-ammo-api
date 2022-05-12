from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from armas.models import Arma
from armas.serializers import ArmaSerializer


class ArmaViewSet(viewsets.ModelViewSet):
    queryset = Arma.objects.all()
    serializer_class = ArmaSerializer
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["marca", "modelo"]
    ordering_fields = ["quantidade_de_tiros", "valor_estimado"]
    filterset_fields = ["calibre", "objeto"]
