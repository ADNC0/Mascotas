from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Count
from .models import Persona, Mascota, Adopcion


# ===== PERSONA =====
def persona(request):
    listado = Persona.objects.all()
    return render(request, "persona.html", {'personas': listado})


def nuevaPersona(request):
    return render(request, "nuevaPersona.html")


def guardarPersona(request):
    nombre = request.POST["nombre_per"]
    apellido = request.POST["apellido_per"]
    telefono = request.POST.get("telefono_per")
    correo = request.POST["correo_per"]
    direccion = request.POST.get("direccion_per")
    documento = request.FILES.get("documento_per")

    Persona.objects.create(
        nombre_per=nombre,
        apellido_per=apellido,
        telefono_per=telefono,
        correo_per=correo,
        direccion_per=direccion,
        documento_per=documento
    )
    messages.success(request, "Persona guardada exitosamente")
    return redirect('/persona')


def eliminarPersona(request, id):
    persona = Persona.objects.get(id_per=id)
    persona.delete()
    messages.success(request, "Persona eliminada correctamente")
    return redirect('/persona')


def editarPersona(request, id):
    personaEditar = Persona.objects.get(id_per=id)
    return render(request, "editarPersona.html", {'personaEditar': personaEditar})


def procesarEdicionPersona(request, id):
    persona = Persona.objects.get(id_per=id)
    persona.nombre_per = request.POST["nombre_per"]
    persona.apellido_per = request.POST["apellido_per"]
    persona.telefono_per = request.POST.get("telefono_per")
    persona.correo_per = request.POST["correo_per"]
    persona.direccion_per = request.POST.get("direccion_per")
    persona.documento_per = request.FILES.get("documento_per", persona.documento_per)
    persona.save()
    messages.success(request, "Persona actualizada exitosamente")
    return redirect('/persona')


# ===== MASCOTA =====
def mascota(request):
    listado = Mascota.objects.all()
    return render(request, "mascota.html", {'mascotas': listado})


def nuevaMascota(request):
    return render(request, "nuevaMascota.html")


def guardarMascota(request):
    Mascota.objects.create(
        numero_serie_mas=request.POST["numero_serie_mas"],
        nombre_mas=request.POST["nombre_mas"],
        especie_mas=request.POST["especie_mas"],
        raza_mas=request.POST.get("raza_mas"),
        sexo_mas=request.POST["sexo_mas"],
        edad_mas=request.POST["edad_mas"],
        peso_mas=request.POST["peso_mas"],
        foto_mas=request.FILES.get("foto_mas"),
        historial_mas=request.POST.get("historial_mas"),
        estado_mas=request.POST["estado_mas"]
    )
    messages.success(request, "Mascota guardada exitosamente")
    return redirect('/mascota')


def eliminarMascota(request, id):
    mascota = Mascota.objects.get(id_mas=id)
    mascota.delete()
    messages.success(request, "Mascota eliminada correctamente")
    return redirect('/mascota')


def editarMascota(request, id):
    mascotaEditar = Mascota.objects.get(id_mas=id)
    return render(request, "editarMascota.html", {'mascotaEditar': mascotaEditar})


def procesarEdicionMascota(request, id):
    mascota = Mascota.objects.get(id_mas=id)
    mascota.numero_serie_mas = request.POST["numero_serie_mas"]
    mascota.nombre_mas = request.POST["nombre_mas"]
    mascota.especie_mas = request.POST["especie_mas"]
    mascota.raza_mas = request.POST.get("raza_mas")
    mascota.sexo_mas = request.POST["sexo_mas"]
    mascota.edad_mas = request.POST["edad_mas"]
    mascota.peso_mas = request.POST["peso_mas"]
    mascota.estado_mas = request.POST["estado_mas"]
    mascota.historial_mas = request.POST.get("historial_mas")
    mascota.foto_mas = request.FILES.get("foto_mas", mascota.foto_mas)
    mascota.save()
    messages.success(request, "Mascota actualizada exitosamente")
    return redirect('/mascota')


# ===== ADOPCION =====
def adopcion(request):
    listado = Adopcion.objects.select_related('persona', 'mascota')
    return render(request, "adopcion.html", {'adopciones': listado})


def nuevaAdopcion(request):
    personas = Persona.objects.all()
    mascotas = Mascota.objects.filter(estado_mas="Disponible")
    return render(request, "nuevaAdopcion.html", {'personas': personas, 'mascotas': mascotas})


def guardarAdopcion(request):
    persona_id = request.POST["persona"]
    mascota_id = request.POST["mascota"]
    documento = request.FILES.get("documento_ado")
    observacion = request.POST.get("observacion_ado")

    Adopcion.objects.create(
        persona_id=persona_id,
        mascota_id=mascota_id,
        documento_ado=documento,
        observacion_ado=observacion
    )

    Mascota.objects.filter(id_mas=mascota_id).update(estado_mas="Adoptada")
    messages.success(request, "Adopción guardada exitosamente")
    return redirect('/adopcion')


def eliminarAdopcion(request, id):
    adopcion = Adopcion.objects.get(id_ado=id)
    adopcion.delete()
    messages.success(request, "Adopción eliminada correctamente")
    return redirect('/adopcion')


def editarAdopcion(request, id):
    adopcionEditar = Adopcion.objects.get(id_ado=id)
    personas = Persona.objects.all()
    mascotas = Mascota.objects.all()
    return render(request, "editarAdopcion.html", {
        'adopcionEditar': adopcionEditar,
        'personas': personas,
        'mascotas': mascotas
    })


def procesarEdicionAdopcion(request, id):
    adopcion = Adopcion.objects.get(id_ado=id)
    adopcion.persona_id = request.POST["persona"]
    adopcion.mascota_id = request.POST["mascota"]
    adopcion.observacion_ado = request.POST.get("observacion_ado")
    adopcion.documento_ado = request.FILES.get("documento_ado", adopcion.documento_ado)
    adopcion.save()
    messages.success(request, "Adopción actualizada exitosamente")
    return redirect('/adopcion')
