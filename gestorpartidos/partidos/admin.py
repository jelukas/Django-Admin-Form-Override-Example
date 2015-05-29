from django.contrib import admin
from partidos.models import Partido, Equipo
from .forms import PartidoForm


class PartidoAdmin(admin.ModelAdmin):
    form = PartidoForm


class EquipoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Partido, PartidoAdmin)
admin.site.register(Equipo, EquipoAdmin)
