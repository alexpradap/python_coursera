#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: alexander prada perez
"""

import calculadora_indices as calc

print("Esta funcion calcula el indice de masa corporal a partir de la altura \
       y el peso de la persona\n")

nombre = input("Por favor escriba su nombre: ")
peso = input("Ingrese su peso en Kilogramos: ")
altura = input("Ingrese su estatura en Metros: ")

imc = calc.calcular_IMC(nombre, int(peso), float(altura))

print("Su Indice de Masa Corporal es: " + str(imc))