from .models import Alimento

from dal import autocomplete

class AlimentoAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Alimento.objects.none()

        qs = Alimento.objects.all()

        if self.q:
            qs = qs.filter(descricaoAlimento__icontains=self.q)

        return qs
