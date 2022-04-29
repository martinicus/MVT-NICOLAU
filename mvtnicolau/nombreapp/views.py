from django.http import HttpResponse
from django.shortcuts import render
from .models import Mi_familia
from django.http import HttpResponse

def mi_familia(self):
    mi_familia = Mi_familia(parentaje="hermana", nombre="silvina", apellido="rosas", edad=25, ocupacion="estudiante", email="pepe@gmail.com")
    mi_familia.save()
    texto=f"Parentezco: {mi_familia.parentaje} Nombre: {mi_familia.nombre} Apellido: {mi_familia.apellido} Edad: {mi_familia.edad} Ocupación: {mi_familia.ocupacion} Email: {mi_familia.email}"
    return HttpResponse(texto)