from django.contrib import admin
from .models import Municao


@admin.register(Municao)
class MunicaoAdmin(admin.ModelAdmin):
    pass
