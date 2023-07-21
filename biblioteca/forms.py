from django.forms import ModelForm
from django import forms
from .models import Livro, Editora, Genero

class LivroForm(ModelForm):
    class Meta:
        model = Livro
        fields = '__all__'
        widgets = {
            'nome_livro' : forms.TextInput(attrs={'class': 'form-control' }),
            'autor' : forms.TextInput(attrs={'class': 'form-control' }),
            'editora': forms.Select(attrs={'class': 'form-control' }),
            'preco': forms.TextInput(attrs={'class': 'form-control' }),
            'genero': forms.Select(attrs={'class': 'form-control' }),
            'imagem': forms.FileInput(attrs={'class':'form-control'}),
            'numero_paginas' : forms.TextInput(attrs={'class': 'form-control' }),
            'ano_publicacao' : forms.TextInput(attrs={'class': 'form-control' }),
                 
        }

class EditoraForm(ModelForm):
    class Meta: 
        model = Editora
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control' }),
        }  

class GeneroForm(ModelForm):
    class Meta: 
        model = Genero
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control' }),
        }  

