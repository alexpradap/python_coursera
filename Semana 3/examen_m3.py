##def funcion(x: int, n: int) -> int:
##    resultado = 1
##    i = n*x
##    while i>= 0:
##        resultado *= i**x
##        i -= 1
##    return resultado
##print(funcion(2,5))


##matriz = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
##
##def funcion(matriz: list) -> int:
##    suma = 0
##    for i in range (0, len(matriz)):
##        for j in range (i, len(matriz[0])):
##            suma = suma + matriz[i][j]
##    return suma
##
##print(funcion(matriz))


def letra_mas_comun(cadena: str) -> str:
    alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    lista=[]
    lista[:0]=cadena
    la_mas = {}
    for c in lista:
        if alfabeto.count(c) > 0:
            repeticiones = lista.count(c)
            if la_mas.get("letra") is None:
                la_mas["letra"] = c
                la_mas["repeticiones"] = repeticiones
            else:
                if repeticiones == la_mas.get("repeticiones"):
                    if alfabeto.index(c) > alfabeto.index(la_mas.get("letra")):
                        la_mas["letra"] = c
                        la_mas["repeticiones"] = repeticiones
                elif repeticiones > la_mas.get("repeticiones"):
                    la_mas["letra"] = c
                    la_mas["repeticiones"] = repeticiones
                else:
                    next
    return la_mas["letra"]

print(letra_mas_comun("ALEXANDERPRADAPEREZ"))


def listar_aeropuertos_sin_salida(vuelos: dict) -> list:
    aeropuertos_salidas_entradas = {}
    for vuelo in vuelos:
        ##{aeropuerto: [salidas,llegadas]}
        if vuelos[vuelo]["origen"] not in aeropuertos_salidas_entradas:
            aeropuertos_salidas_entradas[vuelos[vuelo]["origen"]] = [1, 0]
        else:
            aeropuertos_salidas_entradas[vuelos[vuelo]["origen"]] = \
            [aeropuertos_salidas_entradas[vuelos[vuelo]["origen"]][0] + 1, \
            aeropuertos_salidas_entradas[vuelos[vuelo]["origen"]][1]]
        
        if vuelos[vuelo]["destino"] not in aeropuertos_salidas_entradas:
            aeropuertos_salidas_entradas[vuelos[vuelo]["destino"]] = [0, 1]
        else:
            aeropuertos_salidas_entradas[vuelos[vuelo]["destino"]] = \
            [aeropuertos_salidas_entradas[vuelos[vuelo]["destino"]][0], \
            aeropuertos_salidas_entradas[vuelos[vuelo]["destino"]][1] + 1]

    lista = []
    for aeropuerto in aeropuertos_salidas_entradas:
        if aeropuertos_salidas_entradas[aeropuerto][0] == 0:
            lista.append(aeropuerto)
    
    return lista