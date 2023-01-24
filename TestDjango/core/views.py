from urllib import request
from django.shortcuts import render
from .models import Vehiculo, Categoria

# Create your views here.


def home(request):
    return render(request, 'home.html')

def contacto(request):
    return render(request, 'contacto.html')

def vehiculos(request):
    vVehiculos = Vehiculo.objects.all()
    contexto = {'nombre' : 'Jorge Acuña', 'vehiculos' : vVehiculos}
    return render(request, 'vehiculos.html' , contexto)




