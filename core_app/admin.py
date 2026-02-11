from django.contrib import admin

from .models import UnidadeSaude

@admin.register(UnidadeSaude)
class UnidadeSaudeAdmin(admin.ModelAdmin):
    # Colunas que vão aparecer na listagem
    list_display = ('nome', 'pacientes_em_espera', 'ultima_atualizacao')
    
    # Permite editar o número de pacientes diretamente na lista sem clicar na unidade
    list_editable = ('pacientes_em_espera',)
    
    # Adiciona uma barra de pesquisa por nome
    search_fields = ('nome',)
