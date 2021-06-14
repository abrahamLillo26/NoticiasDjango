from django.shortcuts import render

# Create your views here.
def home(request):

    return render(request, 'miApp/home.html')


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

