from django.urls import path
from . import views

urlpatterns = [

    path('dashboard/', views.dashboard, name='dashboard'),

    # PERSONAS
    path('', views.persona),
    path('persona', views.persona),
    path('nuevaPersona', views.nuevaPersona),
    path('guardarPersona', views.guardarPersona),
    path('eliminarPersona/<id>', views.eliminarPersona),
    path('editarPersona/<id>', views.editarPersona),
    path('procesarEdicionPersona/<int:id>/', views.procesarEdicionPersona, name='procesarEdicionPersona'),


    # MASCOTAS
    path('mascota', views.mascota),
    path('nuevaMascota', views.nuevaMascota),
    path('guardarMascota', views.guardarMascota),
    path('eliminarMascota/<id>', views.eliminarMascota),
    path('editarMascota/<id>', views.editarMascota),
    path('procesarEdicionMascota/<id>', views.procesarEdicionMascota),

    # ADOPCIONES
    path('adopcion', views.adopcion),
    path('nuevaAdopcion', views.nuevaAdopcion),
    path('guardarAdopcion', views.guardarAdopcion),
    path('eliminarAdopcion/<id>', views.eliminarAdopcion),
    path('editarAdopcion/<id>', views.editarAdopcion),
    path('procesarEdicionAdopcion/<id>', views.procesarEdicionAdopcion),
]
