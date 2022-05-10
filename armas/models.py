from django.db import models
from utils.models import Calibre, Objeto, ObjetoTipo

class Arma(models.Model):
    calibre = models.ForeignKey(Calibre, on_delete=models.PROTECT)
    marca = models.CharField(max_length=64, blank=False)
    modelo = models.CharField(max_length=64, blank=False)
    quantidade_de_tiros = models.IntegerField(null=False, blank=False)
    valor_estimado = models.FloatField(null=False, blank=False)
    imagem = models.CharField(max_length=128)
    objeto = models.ForeignKey(Objeto, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        objeto_tipo = ObjetoTipo.objects.get(pk=1)
        objeto = Objeto.objects.create(objeto_tipo=objeto_tipo)
        objeto.save()
        self.objeto = objeto
        return super().save(*args, **kwargs)
    