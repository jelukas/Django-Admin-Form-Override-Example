from django import forms
from .models import Partido, Equipo


class PartidoForm(forms.ModelForm):

    class Meta:
        model = Partido
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PartidoForm, self).__init__(*args, **kwargs)
        # Solo podemos selecionar un ganador que sea el local o el visitante
        self.fields['ganador'].queryset = Equipo.objects.filter(id__in=(self.instance.local_id, self.instance.visitante_id))
