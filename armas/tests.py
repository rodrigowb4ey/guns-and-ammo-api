import json
from django.urls import reverse
from django.test import TestCase
from django.core import serializers
from rest_framework import status
from rest_framework.test import APIClient, APITestCase, APIRequestFactory
from .views import ArmaViewSet
from .models import Arma
from utils.models import Calibre, ObjetoTipo
from utils.serializers import CalibreSerializer


class ArmaTests(APITestCase):
    def setUp(self):
        self.objeto_tipo = ObjetoTipo.objects.create(tipo_de_objeto='Arma')
        self.calibre = Calibre.objects.create(desc_calibre='38')
    
    def test_create_arma(self):
        url = reverse('arma-list')
        calibre_serialized = CalibreSerializer(self.calibre).data
        arma_data = {
            'calibre': calibre_serialized,
            'marca': 'Teste',
            'modelo': 'Testando',
            'quantidade_de_tiros': 10,
            'valor_estimado': 5000.0,
            'imagem': 'test'
        }
        response = self.client.post(url, arma_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)       

    def test_read_arma(self):
        url = reverse('arma-list')
        response = self.client.get(url, None, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_arma(self):
        pass

    def test_delete_arma(self):
        pass
