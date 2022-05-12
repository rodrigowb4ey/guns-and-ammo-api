from django.contrib.auth import get_user_model
from rest_framework import serializers
from utils.models import Calibre, Objeto, ObjetoTipo


User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email"]


class CalibreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Calibre
        fields = ["id", "desc_calibre"]


class ObjetoTipoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ObjetoTipo
        fields = ["id", "tipo_de_objeto"]


class ObjetoSerializer(serializers.HyperlinkedModelSerializer):
    objeto_tipo = serializers.StringRelatedField()

    class Meta:
        model = Objeto
        fields = ["id", "objeto_tipo"]
