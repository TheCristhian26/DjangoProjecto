
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.landing,name='user/inicio.html'),
    path('inicio/',views.inicio,name='user/inicio.html'),
    path('registrar/',views.showFormRegister,name='form-register'),
    path('personas-register/',views.storePersona,name="personas.store"),
    path('register/',views.listaclientes,name='projects/listaclientes.html'),   
    path('login/',views.showlogin,name='user/login.html'),
    path('login1/',views.startsession,name='login'),
    path('singup/',views.showsingup,name='signup'),
]
   


