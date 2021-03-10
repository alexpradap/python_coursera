#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: alexander prada perez
"""

import calculadora_indices as calc

print("Esta funcion calcula el porcentaje de grasa corporal\n")

nombre = input("Por favor escriba su nombre: ")
peso = input("Ingrese su peso en Kilogramos: ")
altura = input("Ingrese su estatura en Metros: ")
edad = input("Ingrese su edad en años: ")
genero = input("Ingrese M para Masculino o F para Femenino: ")

if genero == "M":
    genero = 10.8
else:
    if genero == "F":
        genero = 0
    else:
        print("Genero incorrecto, se realizara el calculo con M")
        genero = 10.8

pgc = calc.calcular_porcentaje_grasa(nombre, int(peso), float(altura), int(edad), genero)

print("Su Porcentaje de Grasa Corporal es: " + str(pgc))