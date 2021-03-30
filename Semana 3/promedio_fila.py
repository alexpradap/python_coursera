def promedio_fila(matriz: list, fila: int) -> float:
    if fila < 1 or fila > len(matriz):
        return -1
    else:
        if len(matriz[fila - 1]) > 0:
            sum_notas = 0
            contador = 0
            for i in matriz[fila - 1]:
                if i != 0:
                    sum_notas = sum_notas + i
                    contador = contador + 1
            
            return round(sum_notas / contador, 2)
        else:
            return 0