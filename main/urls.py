"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from operator import index
from django.contrib import admin
from django.urls import path

from biblioteca.views import detalhe_livros,lista_livros, editora_criar, editora_editar, editora_listar, editora_remover, genero_criar, genero_editar, genero_listar, genero_remover, index, livro_criar, livro_editar, livro_remover, livros_listar
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),

    path('',index,name='index'),
    path('lista_livros/',lista_livros,name='lista_livros'),
    path('detalhe/<int:id_livro>',detalhe_livros,name='detalhes'),

    
    path('livro/listar',livros_listar,name='livro_listar'),
    path('livro/',livro_criar,name='livro_criar'),
    path('livro/editar/<int:id>/',livro_editar, name='livro_editar'),
    path('livro/remover/<int:id>/',livro_remover,name='livro_remover'),

    path('genero/',genero_criar,name='genero_criar'),
    path('genero/editar/<int:id>/',genero_editar, name='genero_editar'),
    path('genero/remover/<int:id>/',genero_remover,name='genero_remover'),
    path('genero/listar',genero_listar,name='genero_listar'),

    path('editora/',editora_criar,name='editora_criar'),
    path('editora/editar/<int:id>/',editora_editar, name='editora_editar'),
    path('editora/remover/<int:id>/',editora_remover,name='editora_remover'),
    path('editora/listar',editora_listar,name='editora_listar'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
