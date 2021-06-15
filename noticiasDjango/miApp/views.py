from django.db.models.fields import files
from django.shortcuts import render, redirect, get_object_or_404
from .models import Noticias
from .forms import NoticiaForm


# Create your views here.
def home(request):
    noticias = Noticias.objects.all()
    data = {
        'noticias': noticias
    }
    return render(request, 'miApp/home.html', data)


def contacto(request):

    return render(request, 'miApp/contacto.html')
    

def login(request):

    return render(request, 'miApp/login.html')


def quienessomos(request):

    return render(request, 'miApp/quienessomos.html')


def sismos(request):

    return render(request, 'miApp/sismos.html')


def tarjetaNoticia(request):

    return render(request, 'miApp/tarjetaNoticia.html')


def agregarNoticia(request):

    data = {
        'form': NoticiaForm()
    }

    if request.method == 'POST':
        formulario = NoticiaForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado correctamente"
        else:
            data["mensaje"] = " no guardado"

    return render(request, 'miApp/crudNoticia/agregarNoticia.html', data)



def listarNoticias(request):

    noticias = Noticias.objects.all()

    data = {
        'noticias': noticias
    }
    
    return render(request, 'miApp/crudNoticia/listarNoticias.html', data)



def modificarNoticia(request, id):
    noticia = get_object_or_404(Noticias, id=id)

    data = {
        'form': NoticiaForm(instance=noticia)
    }

    if request.method == 'POST':
        formulario = NoticiaForm(data=request.POST, instance=noticia, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listarNoticias")
        
    return render(request, 'miApp/crudNoticia/modificarNoticia.html', data)


def eliminarNoticia(request, id):
    noticia = get_object_or_404(Noticias, id=id)
    noticia.delete()
    return redirect(to="listarNoticias")
