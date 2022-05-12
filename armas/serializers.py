from rest_framework import serializers
from drf_writable_nested.mixins import NestedUpdateMixin
from armas.models import Arma
from utils.models import Calibre
from utils.serializers import ObjetoSerializer, CalibreSerializer


class ArmaSerializer(serializers.HyperlinkedModelSerializer, NestedUpdateMixin):
    objeto = ObjetoSerializer(read_only=True)
    calibre = CalibreSerializer()
    
    class Meta:
        model = Arma
        fields = ['url', 'id', 'calibre', 'marca', 'modelo', 'quantidade_de_tiros', 'valor_estimado', 'imagem', 'objeto']

    def create(self, validated_data):
        calibre_data = validated_data.pop('calibre')
        desc_calibre = calibre_data['desc_calibre']
        calibre = Calibre.objects.get(desc_calibre=desc_calibre)
        arma = Arma.objects.create(calibre=calibre, **validated_data)
        return arma
