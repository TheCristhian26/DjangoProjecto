
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
    path('login1/',views.startSession,name='login'),
    path('singup/',views.showsingup,name='signup'),
    path('logout/',views.showlogout,name='logout'),
    path('edit/',views.showedit,name="update"),
    path('masinfo/',views.showiinfo,name='contactanos-form'),
    path('project-edit/<int:persona_codigo>/',views.showUpdateProjectForm, name="projects.edit"),
    path('project-update/<int:persona_codigo>/',views.updateProject, name="projects.update"),
    path('project-delete/<int:persona_codigo>/',views.confirmDeleteProject, name="projects.delete"),
    path('projects-destroy/<int:persona_codigo>/',views.destroyProject, name="projects.destroy"),
    path('task-store/',views.storeventas, name="tasks.store"),
    path('task-edit/<int:persona_codigo>/',views.showUpdateTaskForm, name="tasks.edit"),
    path('task-update/<int:persona_codigo>/',views.updateTask, name="tasks.update"),
    path('task-delete/<int:task_id>/',views.confirmDeleteTask, name="tasks.delete"),
    path('task-destroy/<int:persona_codigo>/',views.destroyTask, name="tasks.destroy"),
]
   


