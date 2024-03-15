from django.shortcuts import render
import requests
from .models import log
# Create your views here.

#VIEWS USUARIOS
def lista_usuarios(request):
    URL_API = 'https://jsonplaceholder.typicode.com/users'
    try:
        response = requests.get(URL_API)
        if(response.status_code == 200):
            usuarios = response.json()
            log.objects.create(
                url = URL_API,
                status_code = str(response.status_code)
            )
        else:
            print(f"Error en la solicutud : {response.status_code}")
            usuarios = []
    except:
        print(f"Error en la solicutud: {response.status_code}")
        usuarios = []
    return render(request, 'lista_usuarios.html', {'usuarios': usuarios})

def lista_publicaciones(request, id):
    URL_API = 'https://jsonplaceholder.typicode.com/posts?userId='+str(id)
    try:
        response = requests.get(URL_API)
        if(response.status_code == 200):
            publicaciones = response.json()
            log.objects.create(
                url = URL_API,
                status_code = str(response.status_code)
            )
        else:
            print(f"Error en la solicutud : {response.status_code}")
            publicaciones = []
    except:
        print(f"Error en la solicutud: {response.status_code}")
        publicaciones = []
    return render(request, 'lista_publicaciones.html', {'publicaciones': publicaciones})

def lista_albumes(request, id):
    URL_API = 'https://jsonplaceholder.typicode.com/albums?userId='+str(id)
    try:
        response = requests.get(URL_API)
        if(response.status_code == 200):
            albumes = response.json()
            log.objects.create(
                url = URL_API,
                status_code = str(response.status_code)
            )
        else:
            print(f"Error en la solicutud : {response.status_code}")
            albumes = []
    except:
        print(f"Error en la solicutud: {response.status_code}")
        albumes = []
    return render(request, 'lista_albumes.html', {'albumes': albumes})

def ver_fotos(request, id):
    URL_API = 'https://jsonplaceholder.typicode.com/photos?albumId='+str(id)
    try:
        response = requests.get(URL_API)
        if(response.status_code == 200):
            fotos = response.json()
            log.objects.create(
                url = URL_API,
                status_code = str(response.status_code)
            )

        else:
            print(f"Error en la solicutud : {response.status_code}")
            fotos = []
    except:
        print(f"Error en la solicutud: {response.status_code}")
        fotos = []
    return render(request, 'ver_fotos.html', {'fotos': fotos})

def lista_logs(request):
    logs = log.objects.all()
    return render(request, 'lista_logs.html', {'logs':logs})