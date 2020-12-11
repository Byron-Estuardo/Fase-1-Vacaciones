from django.http import HttpResponse
from django.shortcuts import render

# First view

def Registro_view(Request):
    return render(Request,"RegistroClientes.html")
