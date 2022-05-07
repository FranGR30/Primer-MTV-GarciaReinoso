from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.template import Template, Context
from datetime import date, time, datetime
from .models import Familiar

# Create your views here.
def list_familiar(request):
    familiars = Familiar.objects.all()
    context = {'familiars':familiars}
    return render(request,'Template.html',context)

def create_familiar(request):
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    edad = request.POST['edad']
    fechaDeNacimiento = request.POST['fechaDeNacimiento']
    familiar = Familiar(nombre=nombre,apellido=apellido,edad=edad,fechaDeNacimiento=fechaDeNacimiento)
    familiar.save()
    return redirect('/Familiares/')

def delete_familiar(request,id):
    familiar = Familiar.objects.get(id = id)
    familiar.delete()
    return redirect('/Familiares/')