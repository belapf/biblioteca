from django.db import models

# Create your models here.


class Genero(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome 

class Editora(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome 

class Livro(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=200)
    numero_paginas = models.CharField(max_length=200)
    ano_publicacao = models.CharField(max_length=200)
    preco= models.CharField(max_length=100)
    genero = models.ForeignKey(Genero,on_delete=models.CASCADE)
    editora = models.ForeignKey(Editora,on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='livros', null=True, blank=True)
