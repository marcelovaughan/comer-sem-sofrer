from django.contrib import admin
from django.contrib.admin import AdminSite

from .forms import PorcaoForm

# Register your models here.
from .models import Alimento, Refeicao, Porcao

admin.site.site_header = 'Calorias - Comer sem sofrer'

class MyAdminSite(AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = 'Calorias'

    # Text to put in each page's <h1> (and above login form).
    site_header = 'Calorias - ADMIN'

    # Text to put at the top of the admin index page.
    index_title = 'Painel'


admin_site = MyAdminSite()


@admin.register(Alimento)
class AlimentoAdmin(admin.ModelAdmin):
    search_fields = ("descricaoAlimento", "categoria",)

    list_display = ("descricaoAlimento", "energiaKcal", "proteina", "carboidrato", "lipideos",)



@admin.register(Porcao)
class PorcaoAdmin(admin.ModelAdmin):
    search_fields = ("alimento", "refeicao",)

    list_display = ("refeicao", "alimento", "unidade_medida", "quantidade",)

    autocomplete_fields = ['alimento']


class PorcaoRefeicaoInlines(admin.TabularInline):
    model = Porcao
    extra = 0

    form = PorcaoForm

    fields = ('quantidade', 'unidade_medida', 'alimento', )


@admin.register(Refeicao)
class RefeicaoAdmin(admin.ModelAdmin):
    search_fields = ("nome", "author", "horario",)

    # autocomplete_fields = ['alimentos']

    list_display = ("nome", "horario", "author", "created_at",)

    inlines = [PorcaoRefeicaoInlines,]