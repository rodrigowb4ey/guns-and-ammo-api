from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Arma
from utils.models import Calibre, ObjetoTipo
from utils.serializers import CalibreSerializer


class ArmaTests(APITestCase):
    def setUp(self):
        self.objeto_tipo = ObjetoTipo.objects.create(tipo_de_objeto='Arma')
        self.calibre = Calibre.objects.create(desc_calibre='38')
        self.calibre_updated = Calibre.objects.create(desc_calibre='.40')
        arma_data = {
            'calibre': self.calibre,
            'marca': 'OutroTeste',
            'modelo': 'Testing',
            'quantidade_de_tiros': 15,
            'valor_estimado': 6000.0,
            'imagem': 'test'
        }
        self.exemplo_arma = Arma.objects.create(**arma_data)
    
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
        url = '/armas/1/'
        calibre_serialized = CalibreSerializer(self.calibre_updated).data
        arma_data = {
            'calibre': calibre_serialized,
            'marca': 'Teste',
            'modelo': 'Testando',
            'quantidade_de_tiros': 10,
            'valor_estimado': 5000.0,
            'imagem': 'test'
        }
        response = self.client.put(url, arma_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_arma(self):
        url = '/armas/1/'
        response = self.client.delete(url, None)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
