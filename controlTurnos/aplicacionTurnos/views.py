from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, authenticate
from .forms import *

"ABM Paciente"
def nuevoPaciente(request):
    pacientes = Paciente.objects.order_by('apellido')
    if request.method == 'POST':
        form = pacienteForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/nuevoPaciente')
    else:
        form = pacienteForm()
    return render(request, 'aplicacionTurnos/nuevoPaciente.html', {'form': form, 'pacientes':pacientes})


def editarPaciente(request, pk):
    paciente = Paciente.objects.get(pk=pk)
    if request.method == 'POST':
        form = pacienteForm(request.POST, instance = paciente)
        if 'eliminar' in request.POST:
            paciente.delete()
            return redirect('/nuevoPaciente')
        elif form.is_valid():
            form.save(commit=True)
            return redirect('/nuevoPaciente')
    else:
        form = pacienteForm(instance = paciente)
    return render(request, 'aplicacionTurnos/editarPaciente.html',{'form':form})

"ABM Medico"
def nuevoMedico(request):
    medicos = Medico.objects.order_by('apellido')
    if request.method == 'POST':
        form = medicoForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/nuevoMedico')
    else:
        form = medicoForm()
    return render(request, 'aplicacionTurnos/nuevoMedico.html',{'form':form, 'medicos':medicos})

def editarMedico(request, pk):
    medico = Medico.objects.get(pk=pk)
    if request.method == 'POST':
        form = medicoForm(request.POST, instance = medico)
        if 'eliminar' in request.POST:
            medico.delete()
            return redirect('/nuevoMedico')
        elif form.is_valid():
            form.save(commit=True)
            return redirect('/nuevoMedico')
    else:
        form = medicoForm(instance = paciente)
    return render(request, 'aplicacionTurnos/editarMedico.html',{'form':form})

"ABM Tratamiento"
def nuevoTratamiento(request):
    tratamientos = Tratamiento.objects.all().order_by('nombre')
    if request.method == 'POST':
        form = tratamientoForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/nuevoTratamiento')
    else:
        form = tratamientoForm()
    return render(request, 'aplicacionTurnos/nuevoTratamiento.html',{'form':form, 'tratamientos':tratamientos})

def editarTratamiento(request, pk):
    tratamiento = Tratamiento.objects.get(pk=pk)
    if request.method == 'POST':
        form = tratamientoForm(request.POST, instance = tratamiento)
        if 'eliminar' in request.POST:
            tratamiento.delete()
            return redirect('/nuevoTratamiento')
        elif form.is_valid():
            form.save(commit=True)
            return redirect('/nuevoTratamiento')
    else:
        form = tratamientoForm(instance = tratamiento)
    return render(request, 'aplicacionTurnos/editarTratamiento.html',{'form':form})

"ABM obraSocial"

def nuevoObraSocial(request):
    obrasSociales = ObraSocial.objects.all().order_by('nombre')
    if request.method == 'POST':
        form = obraSocialForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/nuevoObraSocial')
    else:
        form = obraSocialForm()
    return render(request, 'aplicacionTurnos/nuevoObraSocial.html',{'form':form, 'obrasSociales':obrasSociales})

def editarObraSocial(request, pk):
    obraSocial = ObraSocial.objects.get(pk=pk)
    if request.method == 'POST':
        form = obraSocialForm(request.POST, instance = obraSocial)
        if 'eliminar' in request.POST:
            obraSocial.delete()
            return redirect('/editarObraSocial')
        elif form.is_valid():
            form.save(commit=True)
            return redirect('/editarObraSocial')
    else:
        form = obraSocialForm(instance = obraSocial)
    return render(request, 'aplicacionTurnos/editarObraSocial.html',{'form':form})

"ABM Especialidad"

def nuevoEspecialidad(request):
    especialidades = Especialidad.objects.all().order_by('nombre')
    if request.method == 'POST':
        form = especialidadForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/nuevoEspecialidad')
    else:
        form = especialidadForm()
    return render(request, 'aplicacionTurnos/nuevoEspecialidad.html',{'form':form, 'especialidades':especialidades})

def editarEspecialidad(request, pk):
    especialidad = Especialidad.objects.get(pk=pk)
    if request.method == 'POST':
        form = especialidadForm(request.POST, instance = especialidad)
        if 'eliminar' in request.POST:
            especialidad.delete()
            return redirect('/editarEspecialidad')
        elif form.is_valid():
            form.save(commit=True)
            return redirect('/editarEspecialidad')
    else:
        form = especialidadForm(instance = especialidad)
    return render(request, 'aplicacionTurnos/editarEspecialidad.html',{'form':form})

"""Login with Model User of django"""
class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated():
            return redirect('/nuevoMedico')
        else:
            form = LoginForm()
            return render(request, 'aplicacionTurnos/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=User.objects.get(username= request.POST['username']), password=request.POST['password'])
            login(request, user)
            return redirect('/nuevoMedico')
        else:
            return render(request, 'aplicacionTurnos/login.html', {'form': form})
