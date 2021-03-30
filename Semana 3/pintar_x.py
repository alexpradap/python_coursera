def hacer_operacion(operacion: str, numero: int) -> int:
    if operacion == "+":
        return numero + numero
    elif operacion == "-":
        return numero - numero
    elif operacion == "*":
        return numero * numero
    elif operacion == "/":
        return numero / numero
    else:
        return -1

def pintar_x(matriz: list, operacion: str) -> list:
    retroceso_j = len(matriz) - 1
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz[i])):
            if i == j:
                matriz[i][j] = hacer_operacion(operacion, matriz[i][j])
                if j != retroceso_j:
                    matriz[i][retroceso_j] = hacer_operacion(operacion, matriz[i][retroceso_j])
                retroceso_j = retroceso_j - 1
    return matriz

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(pintar_x(matriz, "+"))