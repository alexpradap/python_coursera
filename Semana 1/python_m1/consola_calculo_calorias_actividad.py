#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: alexander prada perez
"""

import calculadora_indices as calc

print("Esta funcion calcula el consumo calorico en actividad\n")

nombre = input("Por favor escriba su nombre: ")
peso = input("Ingrese su peso en Kilogramos: ")
altura = input("Ingrese su estatura en Metros: ")
edad = input("Ingrese su edad en años: ")
genero = input("Ingrese M para Masculino o F para Femenino: ")
actividad = input("Ingrese la frecuencia con la que realiza actividad \
fisica de acuerdo a la siguiente tabla: \n \
P: Poco o Ningun Ejercicio \n \
L: Se ejercita entre 1 y 2 días a la semana \n \
M: Se ejercita ente 3 y 5 días a la semana \n \
D: Se ejercita de 6 a 7 días a la semana \n \
A: Se ejercita todos los días mañana y tarde \n \
")

if actividad == "P":
    actividad = 1.2
elif actividad == "L":
    actividad = 1.375
elif actividad == "M":
    actividad = 1.55
elif actividad == "D":
    actividad = 1.72
elif actividad == "A":
    actividad = 1.9
else:
    print("Frecuencia incorrecta, se realizara el calculo con P")
    actividad = 1.2
    
if genero == "M":
    genero = 5
else:
    if genero == "F":
        genero = -161
    else:
        print("Genero incorrecto, se realizara el calculo con M")
        genero = 5

cca = calc.calcular_calorias_en_actividad(nombre, int(peso), float(altura), int(edad), genero, actividad)

print("Su consumo calorico en actividad es de: " + str(cca))