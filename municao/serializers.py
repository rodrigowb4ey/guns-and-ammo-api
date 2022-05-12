from rest_framework import serializers
from municao.models import Municao
from utils.models import Calibre
from utils.serializers import CalibreSerializer, ObjetoSerializer


class MunicaoSerializer(serializers.HyperlinkedModelSerializer):
    objeto = ObjetoSerializer(read_only=True)
    calibre = CalibreSerializer()

    class Meta:
        model = Municao
        fields = [
            "url",
            "id",
            "calibre",
            "marca",
            "modelo",
            "valor_estimado",
            "objeto",
        ]

    def create(self, validated_data):
        calibre_data = validated_data.pop("calibre")
        desc_calibre = calibre_data["desc_calibre"]
        calibre = Calibre.objects.filter(desc_calibre=desc_calibre).first()
        municao = Municao.objects.create(calibre=calibre, **validated_data)
        return municao

    def update(self, instance, validated_data):
        calibre_data = validated_data.pop("calibre")
        new_calibre = Calibre.objects.filter(
            desc_calibre=calibre_data["desc_calibre"]
        ).first()
        instance.calibre = new_calibre
        instance.marca = validated_data.get("marca", instance.marca)
        instance.modelo = validated_data.get("modelo", instance.modelo)
        instance.valor_estimado = validated_data.get(
            "valor_estimado", instance.valor_estimado
        )
        instance.save()
        return instance
