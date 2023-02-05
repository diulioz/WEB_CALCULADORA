from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio),
    #OPERACIONES POR SEPARADO
    path('sumar/<int:op1>/<int:op2>', views.suma),
    path('restar/<int:op1>/<int:op2>', views.resta),
    path('multiplicar/<int:op1>/<int:op>', views.multiplicacion),
    path('dividir/<int:op1>/<int:op2>', views.division),
    #OPERACIONES JUNTAS
    path('calcular/<str:signo>/<int:op1>/<int:op2>', views.calculo),
]