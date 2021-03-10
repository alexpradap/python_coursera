#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: alexander prada perez
"""

import calculadora_indices as calc

print("Esta funcion calcula la tasa metabolica basal\n")

nombre = input("Por favor escriba su nombre: ")
peso = input("Ingrese su peso en Kilogramos: ")
altura = input("Ingrese su estatura en Metros: ")
edad = input("Ingrese su edad en años: ")
genero = input("Ingrese M para Masculino o F para Femenino: ")

if genero == "M":
    genero = 5
else:
    if genero == "F":
        genero = -161
    else:
        print("Genero incorrecto, se realizara el calculo con M")
        genero = 5

tmb = calc.calcular_calorias_en_reposo(nombre, int(peso), float(altura), int(edad), genero)

print("Su consumo calorico en reposo es: " + str(tmb))