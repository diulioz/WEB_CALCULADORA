from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#Operación por operación
def inicio(request):
    return HttpResponse("<h1>Aplicación Calculadora</h1>")

def suma(request, op1, op2):
    return HttpResponse(op1+op2)

def resta(request, op1, op2):
    return HttpResponse(op1-op2)

def multiplicacion(request, op1, op2):
    return HttpResponse(op1*op2)

def division(request, op1, op2):
    if (op2 != 0):
        return HttpResponse(op1/op2)
    else:
        return HttpResponse("No se puede dividir por 0")


#Todas la operaciones
def calculo(request, signo, op1, op2):
    if signo == "s":
        return HttpResponse(op1+op2)
    if signo == "r":
        return HttpResponse(op1-op2)
    if signo == "m":
        return HttpResponse(op1*op2)
    if signo == "d":
        if (op2 != 0):
            return HttpResponse(op1/op2)
        else:
            return HttpResponse("No se puede dividir por 0")
