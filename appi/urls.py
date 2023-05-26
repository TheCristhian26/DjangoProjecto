
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.landing,name='landing'),
    path('inicio/',views.inicio,name='inicio'),
    path('registrar/',views.showFormRegister,name='form-register'),
    path('personas-register/',views.storePersona,name="personas.store"),
    path('lista-clientes/',views.listaclientes,name='personas.list'),   
    path('login/',views.showlogin,name='login-form'),
    path('login1/',views.startsession,name='login'),
    path('singup/',views.showsingup,name='signup'),
    path('projects-edit/<int:persona_codigo>/',views.showconfirmEdit,name="projects.edit"),
    path('projects-update/<int:persona_codigo>/',views.updateProject,name="projects.update"),
]
   


