from rest_framework import serializers
from municao.models import Municao


class MunicaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Municao
        fields = ['id', 'calibre', 'marca', 'modelo', 'valor_estimado', 'objeto_id']