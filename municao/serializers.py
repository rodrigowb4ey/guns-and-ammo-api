from rest_framework import serializers
from municao.models import Municao
from utils.models import Calibre
from utils.serializers import CalibreSerializer, ObjetoSerializer


class MunicaoSerializer(serializers.HyperlinkedModelSerializer):
    objeto = ObjetoSerializer(read_only=True)
    calibre = CalibreSerializer()
    
    class Meta:
        model = Municao
        fields = ['id', 'calibre', 'marca', 'modelo', 'valor_estimado', 'objeto']

    def create(self, validated_data):
        calibre_data = validated_data.pop('calibre')
        desc_calibre = calibre_data['desc_calibre']
        calibre = Calibre.objects.get(desc_calibre=desc_calibre)
        municao = Municao.objects.create(calibre=calibre, **validated_data)
        return municao
