from django.shortcuts import render

# Create your views here.

def formulario(request):
    return render(request, 'formulario.html')