from django.shortcuts import render
from .forms import pacienteForm

# Create your views here.

def mainPage(request):
    form = pacienteForm
    return render(request, 'aplicacionTurnos/mainPage.html',{'form':form})