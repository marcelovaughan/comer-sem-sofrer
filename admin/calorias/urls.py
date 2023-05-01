
from django.contrib import admin
from django.urls import path

from alimentos.views import AlimentoAutocomplete

urlpatterns = [
    path('admin/', admin.site.urls),

    path(
        r'^alimento-autocomplete/$',
        AlimentoAutocomplete.as_view(),
        name='alimento-autocomplete',
    ),
]
