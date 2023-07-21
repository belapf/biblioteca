from django.shortcuts import render,get_object_or_404,redirect
from django.shortcuts import render
from biblioteca.models import Livro, Genero, Editora
from .forms import LivroForm, GeneroForm, EditoraForm

# Create your views here.


def index(request):
    total_livros = Livro.objects.count()
    total_generos = Genero.objects.count()
    total_editoras = Editora.objects.count()
    context = {
        'total_livros' : total_livros,
        'total_generos' : total_generos,
        'total_editoras' : total_editoras,
    }
    return render(request, "livro/index.html",context)

def livro_criar(request):
    if request.method == 'POST':
        form = LivroForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            form = LivroForm() # Limpar o formulário
    else:
        form = LivroForm()

    return render(request, 'livro/form.html', {'form': form})

def livros_listar(request):
    livros = Livro.objects.all()
    context ={
        'livros':livros
    }
    return render(request, "livro/livros.html",context)

def lista_livros(request):
    livros = Livro.objects.all()
    context ={
        'livros':livros
    }
    return render(request, "livro/lista_livros.html",context)

def detalhe_livros(request,id_livro):
    livros = get_object_or_404(Livro, id=id_livro)
    context={
        'livros' : livros,
    }
    return render(request,'livro\detalhes.html',context) 

def livro_editar(request,id):
    livro = get_object_or_404(Livro,id=id)
   
    if request.method == 'POST':
        form = LivroForm(request.POST,request.FILES,instance=livro)

        if form.is_valid():
            form.save()
            return redirect('livro_listar')
    else:
        form = LivroForm(instance=livro)

    return render(request,'livro/form.html',{'form':form})


def livro_remover(request, id):
    livro = get_object_or_404(Livro, id=id)
    livro.delete()
    return redirect('livro_listar') # procure um url com o nome 'lista_livro'



def genero_listar(request):
    generos = Genero.objects.all()
    context = {
        'generos': generos
    }
    return render (request, 'genero/generos.html', context)

def genero_criar(request):
    if request.method == 'POST':
        form = GeneroForm(request.POST)
        if form.is_valid():
            form.save()
            form = GeneroForm() # Limpar o formulário
    else:
        form = GeneroForm()

    return render(request, 'genero/form.html', {'form': form})

def genero_editar(request,id):
    genero = get_object_or_404(Genero,id=id)
   
    if request.method == 'POST':
        form = GeneroForm(request.POST,instance=genero)

        if form.is_valid():
            form.save()
            return redirect('genero_listar')
    else:
        form = GeneroForm(instance=genero)

    return render(request,'genero/form.html',{'form':form})


def genero_remover(request, id):
    genero = get_object_or_404(Genero, id=id)
    genero.delete()
    return redirect('genero_listar') # procure um url com o nome 'lista_aluno'


def editora_criar(request):
    if request.method == 'POST':
        form = EditoraForm(request.POST)
        if form.is_valid():
            form.save()
            form = EditoraForm() # Limpar o formulário
    else:
        form = EditoraForm()

    return render(request, 'editora/form.html', {'form': form})

def editora_listar(request):
    editoras = Editora.objects.all()
    context ={
        'editoras':editoras
    }
    return render(request, "editora/editoras.html",context)

def editora_editar(request,id):
    editora = get_object_or_404(Editora,id=id)
   
    if request.method == 'POST':
        form = EditoraForm(request.POST,instance=editora)

        if form.is_valid():
            form.save()
            return redirect('editora_listar')
    else:
        form = LivroForm(instance=editora)

    return render(request,'editora/form.html',{'form':form})


def editora_remover(request, id):
    editora = get_object_or_404(Editora, id=id)
    editora.delete()
    return redirect('editora_listar') # procure um url com o nome 'lista_livro'

