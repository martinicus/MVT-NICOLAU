import imp
from django.http import HttpResponse
from django.template import loader
import datetime


def disenio(self):
    nom="Rodrigo"
    ape="Nicolau"
    diccionario={"nombre":nom, "apellido":ape}
    plantilla=loader.get_template("template1.html")
    documento=plantilla.render(diccionario)
    
    return HttpResponse(documento)



