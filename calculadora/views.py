from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#Operación por operación
def inicio(request):
    str = """<h1>Aplicación Calculadora</h1> <h3>DAVID CRIOLLO</h3><h3>VANESSA GUSTIN</h3> <h3>JUAN CAMILO INSUASTY</h3> <h3>COMO USAR: </h3>
    <h3>FORMA 1: Después de la direccón y puerto del servidor escribir 'calculadora/operacion/operador1/operador2, donde operación pueder ser: </h3>
    <h3>sumar     restar    multiplicar   dividir</h3>
    <h3>EJEMPLO: 'http://127.0.0.1:8000/calculadora/suma/2/3 </h3>
    <h3>FORMA 2: Después de la direccón y puerto del servidor escribir 'calculadora/calcular/letra/operador1/operador2, donde letra puede ser: </h3>
    <h3>s: suma     r: resta    m: multiplicación   d: división</h3>
    <h3>EJEMPLO: 'http://127.0.0.1:8000/calculadora/calcular/d/100/20 </h3>"""
    return HttpResponse(str)

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
