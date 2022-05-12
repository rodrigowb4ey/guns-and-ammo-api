from django.core.management import BaseCommand
from utils.models import Calibre, ObjetoTipo
from utils.initial_data import calibre_data, objeto_tipo_data


def pre_populate_calibre_tables():
    for data in calibre_data:
        try:
            calibre = Calibre.objects.get(desc_calibre=data.get('desc_calibre'))
        except:
            calibre = Calibre.objects.create(**data)

        print("Calibre: ", calibre)


def pre_populate_objeto_tipo_tables():
    for data in objeto_tipo_data:
        try:
            objeto_tipo = ObjetoTipo.objects.get(tipo_de_objeto=data.get('tipo_de_objeto'))
        except:
            objeto_tipo = ObjetoTipo.objects.create(**data)

        print("Tipo de objeto: ", objeto_tipo)


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        pre_populate_calibre_tables()
        pre_populate_objeto_tipo_tables()
