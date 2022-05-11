from django.db import models
from utils.models import Calibre, Objeto, ObjetoTipo

class Municao(models.Model):
    calibre = models.ForeignKey(Calibre, on_delete=models.PROTECT)
    marca = models.CharField(max_length=64, blank=False)
    modelo = models.CharField(max_length=64, blank=False)
    valor_estimado = models.FloatField(null=False, blank=False)
    objeto = models.ForeignKey(Objeto, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        objeto_tipo = ObjetoTipo.objects.get(tipo_de_objeto='Munição')
        objeto = Objeto.objects.create(objeto_tipo=objeto_tipo)
        objeto.save()
        self.objeto = objeto
        return super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.objeto:
            objeto = self.objeto
            objeto.delete()
        return super().delete(*args, **kwargs)
    