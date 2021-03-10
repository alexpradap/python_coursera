#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: alexander prada perez
"""

"""
Esta funcion calcula el indice de masa corporal a partir de la altura y
el peso de la persona
"""
def calcular_IMC(nombre, peso, altura):
    return peso / (altura ** 2)

"""
Esta funcion calcula el porcentaje de grasa de una persona a partir del peso,
la altura, la edad y el genero
"""
def calcular_porcentaje_grasa(nombre, peso, altura, edad, valor_genero):
    imc = calcular_IMC(nombre, peso, altura)
    return 1.2 * imc + 0.23 * edad - 5.4 - valor_genero

"""
Esta funcion calcula la cantidad de calorias consumidas en reposo a partir
del peso, la altura, la edad y el genero
"""
def calcular_calorias_en_reposo(nombre, peso, altura, edad, valor_genero):
    return (10 * peso) + (6.25 * (altura * 100)) - (5 * edad) + valor_genero

"""
Esta funcion calcula la cantidad de calorias consumidas durante la actividad
fisica a partir del peso, la altura, la edad, el genero y el tipo de
actividad
"""
def calcular_calorias_en_actividad(nombre, peso, altura, edad, valor_genero, valor_actividad):
    tmb = calcular_calorias_en_reposo(nombre, peso, altura, edad, valor_genero)
    return tmb * valor_actividad

"""
Esta funcion calcula el rango de calorias recomendado, que una pesona debe
consumir diariamente si desea adelgazar
"""
def consumo_calorias_recomendado_para_adelgazar(nombre, peso, altura, edad, valor_genero):
    tmb = calcular_calorias_en_reposo(nombre, peso, altura, edad, valor_genero)
    minimo = tmb * 0.8
    maximo = tmb * 0.85
    return "Para adelgazar es recomendado que consumas entre: " + str(minimo) \
        + " y " + str(maximo) + " calorias al dia."