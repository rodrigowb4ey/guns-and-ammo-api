from django.contrib.auth import get_user_model
from rest_framework import serializers
from utils.models import Calibre


User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']

class CalibreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Calibre
        fields = ['id', 'desc_calibre']