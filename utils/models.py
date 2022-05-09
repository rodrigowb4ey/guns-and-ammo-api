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

    desc_calibre = models.CharField(max_length=64, blank=False, choices=CALIBRE_OPTIONS, null=False)