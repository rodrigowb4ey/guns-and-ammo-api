from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Calibre(models.Model):
    CALIBRE_OPTIONS = (
        ("38", "38"),
        ("380", "380"),
        (".40", ".40"),
        (".45", ".45"),
    )

    desc_calibre = models.CharField(max_length=45, blank=False, choices=CALIBRE_OPTIONS)

    def __str__(self):
        return self.desc_calibre


class ObjetoTipo(models.Model):
    TIPO_OPTIONS = (
        ("Arma", "Arma"),
        ("Munição", "Munição"),
    )

    tipo_de_objeto = models.CharField(max_length=64, blank=False, choices=TIPO_OPTIONS)

    def __str__(self):
        return self.tipo_de_objeto


class Objeto(models.Model):
    id = models.BigAutoField(primary_key=True)
    objeto_tipo = models.ForeignKey(ObjetoTipo, on_delete=models.PROTECT)
