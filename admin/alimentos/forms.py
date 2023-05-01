from .models import Porcao
from dal import autocomplete

from django import forms


class PorcaoForm(forms.ModelForm):
    class Meta:
        model = Porcao
        fields = ('__all__')
        widgets = {
            'alimento': autocomplete.ModelSelect2(url='alimento-autocomplete')
        }