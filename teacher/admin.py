from django.contrib import admin
from .models import Professor,Aula

# Register your models here.
@admin.register(Professor)


class ProfAdmin (admin.ModelAdmin):
    list_display = ("nome", "valor_hora", "descricao", "foto")

@admin.register(Aula)
class AulaAdmin(admin.ModelAdmin):
    list_display = ('nome','email','professor')