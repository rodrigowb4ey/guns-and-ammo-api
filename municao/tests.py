from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Municao
from utils.models import Calibre, ObjetoTipo
from utils.serializers import CalibreSerializer


class MunicaoTests(APITestCase):
    def setUp(self):
        self.objeto_tipo = ObjetoTipo.objects.create(tipo_de_objeto="Munição")
        self.calibre = Calibre.objects.create(desc_calibre="38")
        self.calibre_updated = Calibre.objects.create(desc_calibre=".40")
        municao_data = {
            "calibre": self.calibre,
            "marca": "OutroTeste",
            "modelo": "Testing",
            "valor_estimado": 6000.0,
        }
        self.exemplo_municao = Municao.objects.create(**municao_data)

    def test_create_municao(self):
        url = reverse("municao-list")
        calibre_serialized = CalibreSerializer(self.calibre).data
        municao_data = {
            "calibre": calibre_serialized,
            "marca": "Teste",
            "modelo": "Testando",
            "valor_estimado": 5000.0,
        }
        response = self.client.post(url, municao_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_read_municao(self):
        url = reverse("municao-list")
        response = self.client.get(url, None, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_municao(self):
        url = f"/municao/{self.exemplo_municao.pk}/"
        calibre_serialized = CalibreSerializer(self.calibre_updated).data
        municao_data = {
            "calibre": calibre_serialized,
            "marca": "Teste",
            "modelo": "Testando",
            "valor_estimado": 5000.0,
        }
        response = self.client.put(url, municao_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_municao(self):
        url = f"/municao/{self.exemplo_municao.pk}/"
        response = self.client.delete(url, None)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
