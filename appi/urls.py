
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.landing,name='landing'),
    path('inicio/',views.inicio,name='inicio'),
    path('registrar/',views.showFormRegister,name='form-register'),
    path('personas-register/',views.storePersona,name='personas.store'),
    path('register-ventas/',views.storeventas,name='venta.persona'),
    path('persona-ventas/',views.showventas,name='persona.venta'),
    path('lista-clientes/',views.listaclientes,name='personas.list'), 
    path('historial-ventas',views.historial_ventas,name="ventas.list"),  
    path('login/',views.showlogin,name='login-form'),
    path('login1/',views.startsession,name='login'),
    path('singup/',views.showsingup,name='signup'),
    path('logout/',views.showlogout,name='logout'),
    path('edit/',views.showedit,name="update"),
    path('projects-edit/<int:Persona_codigo>/',views.showconfirmEdit,name="projects.edit"),
    path('projects-update/<int:Persona_codigo>/',views.updateProject,name="projects.update"),
]
   


