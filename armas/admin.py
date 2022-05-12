from django.contrib import admin
from .models import Arma


@admin.register(Arma)
class ArmaAdmin(admin.ModelAdmin):
    pass
