from django.contrib import admin
from partidos.models import Partido, Equipo
from .forms import PartidoForm, PartidoChangeListForm


class PartidoAdmin(admin.ModelAdmin):
    form = PartidoForm
    list_display = ('__str__', 'ganador',)
    list_editable = ('ganador',)

    def get_changelist_form(self, request, **kwargs):
        return PartidoChangeListForm


class EquipoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Partido, PartidoAdmin)
admin.site.register(Equipo, EquipoAdmin)
