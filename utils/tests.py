from django.urls import reverse
from rest_framework.test import APITestCase
from utils.models import Calibre, ObjetoTipo
from utils.serializers import CalibreSerializer


class ObjetoTests(APITestCase):
    def setUp(self):
        self.objeto_tipo = ObjetoTipo.objects.create(tipo_de_objeto='Munição')
        self.calibre = Calibre.objects.create(desc_calibre='38')

    def test_creating_municao_instantiates_objeto(self):
        url = reverse('municao-list')
        calibre_serialized = CalibreSerializer(self.calibre).data
        municao_data = {
            'calibre': calibre_serialized,
            'marca': 'OutroTeste',
            'modelo': 'Testing',
            'valor_estimado': 6000.0
        }
        response = self.client.post(url, municao_data, format='json')
        objeto = response.data['objeto']['objeto_tipo']
        self.assertEqual(objeto, 'Munição')

    def test_creating_arma_instantiates_objeto(self):
        url = reverse('arma-list')
        calibre_serialized = CalibreSerializer(self.calibre).data
        arma_data = {
            'calibre': calibre_serialized,
            'marca': 'OutroTeste',
            'modelo': 'Testing',
            'quantidade_de_tiros': 30,
            'valor_estimado': 6000.0,
            'imagem': 'teste'
        }
        response = self.client.post(url, arma_data, format='json')
        objeto = response.data['objeto']['objeto_tipo']
        self.assertEqual(objeto, 'Arma')


