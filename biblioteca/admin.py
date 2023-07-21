from django.contrib import admin
from .models import Livro, Editora, Genero

# Register your models here.

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display=('nome', 'autor', 'numero_paginas', 'ano_publicacao','preco', 'genero', 'editora')

@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display=('nome',)

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display=('nome',)