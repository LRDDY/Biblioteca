from django.contrib import admin
from .models import Cidade, Autor, Editora, Leitor, Livro, Genero

# 1. Definição dos Inlines e Classes Admin
class LivroInline(admin.TabularInline):
    model = Livro
    extra = 1

class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [LivroInline]

# 2. Registros (Apenas UM por modelo)
admin.site.register(Cidade)
admin.site.register(Editora)
admin.site.register(Leitor)
admin.site.register(Genero)

# Registrando os modelos que possuem configurações customizadas
admin.site.register(Livro) 
admin.site.register(Autor, AutorAdmin)