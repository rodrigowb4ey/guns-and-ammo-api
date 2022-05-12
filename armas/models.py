from django.db import models
from utils.models import Calibre, Objeto, ObjetoTipo

class Arma(models.Model):
    calibre = models.ForeignKey(Calibre, related_name='calibre', on_delete=models.PROTECT)
    marca = models.CharField(max_length=64, blank=False)
    modelo = models.CharField(max_length=64, blank=False)
    quantidade_de_tiros = models.IntegerField(null=False, blank=False)
    valor_estimado = models.FloatField(null=False, blank=False)
    imagem = models.CharField(max_length=128)
    objeto = models.ForeignKey(Objeto, on_delete=models.CASCADE)

    def __str__(self):
        return self.modelo
    
    def save(self, *args, **kwargs):
        try:
            objeto = Objeto.objects.get(pk=self.objeto.pk)
            self.objeto = objeto
        except Objeto.DoesNotExist:  
            objeto_tipo = ObjetoTipo.objects.get_or_create(tipo_de_objeto='Arma')
            objeto = Objeto.objects.create(objeto_tipo=objeto_tipo[0])
            objeto.save()
            self.objeto = objeto

        return super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.objeto:
            objeto = self.objeto
            objeto.delete()
        return super().delete(*args, **kwargs)
    