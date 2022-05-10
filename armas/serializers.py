from rest_framework import serializers
from armas.models import Arma


class ArmaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Arma
        fields = ['id', 'calibre', 'marca', 'modelo', 'quantidade_de_tiros', 'valor_estimado', 'imagem', 'objeto_id']