from rest_framework import serializers
from armas.models import Arma
from utils.models import Calibre
from utils.serializers import ObjetoSerializer, CalibreSerializer


class ArmaSerializer(serializers.HyperlinkedModelSerializer):
    objeto = ObjetoSerializer(read_only=True)
    calibre = CalibreSerializer()

    class Meta:
        model = Arma
        fields = [
            "url",
            "id",
            "calibre",
            "marca",
            "modelo",
            "quantidade_de_tiros",
            "valor_estimado",
            "imagem",
            "objeto",
        ]

    def create(self, validated_data):
        calibre_data = validated_data.pop("calibre")
        desc_calibre = calibre_data["desc_calibre"]
        calibre = Calibre.objects.filter(desc_calibre=desc_calibre).first()
        arma = Arma.objects.create(calibre=calibre, **validated_data)
        return arma

    def update(self, instance, validated_data):
        calibre_data = validated_data.pop("calibre")
        new_calibre = Calibre.objects.filter(
            desc_calibre=calibre_data["desc_calibre"]
        ).first()
        instance.calibre = new_calibre
        instance.marca = validated_data.get("marca", instance.marca)
        instance.modelo = validated_data.get("modelo", instance.modelo)
        instance.quantidade_de_tiros = validated_data.get(
            "quantidade_de_tiros", instance.quantidade_de_tiros
        )
        instance.valor_estimado = validated_data.get(
            "valor_estimado", instance.valor_estimado
        )
        instance.imagem = validated_data.get("imagem", instance.imagem)
        instance.save()
        return instance
