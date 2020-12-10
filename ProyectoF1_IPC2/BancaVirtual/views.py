from django.http import HttpResponse
from django.shortcuts import render

# First view

def Registro_view(request, *args, **kwargs):
    return render(request,"RegistroClientes.html", {})
