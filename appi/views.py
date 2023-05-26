from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .models import  Persona,usuario


def landing(request):
    return render(request,'user/inicio.html')

def inicio(request):
    return render(request,'user/inicio.html')

def home(requets):
    return render(requets,'projects.user/inicio.html')

def registrar(request):
    return render(request,'projects/listaclientes.html')

def singup(request):
    return(request,'projects/singup.html')

@login_required
def listaclientes(request):
    Personas=Persona.objects.all()
    return render(request,'projects/listaclientes.html',{
        "Personas":Personas
         })

def showpromocionar(request):
    return render(request,'user/promocionar.html')


def showlogin(request):
    return render(request,'user/login.html')

@login_required
def startsession(request):
    user=authenticate(request=request,username=request.POST['username'],password=request.POST['password']) 
    if(user is None):
        messages.add_message(request=request, level=messages.ERROR, messages='wrong credentials, try again')
        return redirect('Login')
    else:
        login(request,user)
        return redirect('projects.listaclientes')
    
@login_required        
def showsingup(request):
   return render(request,'user/singup.html')

@login_required
def showFormRegister(request):
    return render(request,'user/promocionar.html')

@login_required
def signup(request):
    usuario1=usuario.objects.create_user(
       username=request.POST["username"],
       email=request.POST["email"],
       password=request.POST["password"],
       first_name=request.POST["nombre"],
       last_name=request.POST["lastname"],
    )
    usuario1.save()
    login(request,usuario1)
    return usuario1

@login_required
def storePersona(request):
    """
    Registrar el usuario
    """
    usuario1=User.objects.create_user(
       username=request.POST["username"],
       email=request.POST["email"],
       password=request.POST["password"],
       first_name=request.POST["nombre"],
       last_name=request.POST["apellido"],
    )
    usuario1.save()
    login(request,usuario1)

    """
    Registrar la persona
    """
    variable1=Persona.objects.create(
        codigo = request.POST ["codigo"],
        nombre = request.POST ["nombre"],
        apellido = request.POST ["apellido"],
        direccion = request.POST ["direccion"],
        telefono = request.POST ["telefono"],
        email = request.POST ["email"],
        username = request.POST ["username"],
        password = request.POST["password"],
        tipoPersona_id = request.POST["tipoPersona_id"],
        user_id =usuario1.id
    )
    variable1.save()
    return render(request,'user/promocionar.html')

@login_required
def updateProject(request,persona_codigo):
    Persona=get_object_or_404(Persona,codigo=persona_codigo)
    Persona.nombre=request.POST["nombre"]
    Persona.apellido=request.POST["apellido"]
    Persona.direcccion=request.POST["direccion"]
    Persona.telefono=request.POST["telefono"]
    Persona.save()
    return redirect("projects.listaclientes")



def showconfirmEdit(request,persona_codigo):
    persona1=get_object_or_404(Persona,codigo=persona_codigo)
    return render(request,'projects/edit.html',{
        'persona1':persona1
    })

def Destroy(requets,persona_codigo):
    persona1=get_object_or_404(Persona,codigo=persona_codigo)
    persona1.delete()
    return redirect(requets,'listaclientes.html')

def showconfirdelete(requets,persona_codigo):
    persona1=get_object_or_404(Persona,codigo=persona_codigo)
    return render (requets,'projects/delete.html',{
        'persona1':persona1
    })

