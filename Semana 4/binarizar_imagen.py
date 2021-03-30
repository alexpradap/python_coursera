imagencita = [[(1,2,3),(4,5,6),(7,8,9)],\
          [(7,8,9),(1,2,3),(4,5,6)],\
          [(4,5,6),(7,8,9),(1,2,3)]]

def binarizar_imagen(imagen: list, umbral: float) -> list:
    for i in range (0, len(imagen)):
        for j in range (0, len(imagen[i])):
            if imagen[i][j][0] + imagen[i][j][1] + imagen[i][j][2] / 3 >= umbral:
                imagen[i][j] = (1, 1, 1)
            else:
                imagen[i][j] = (0, 0, 0)
    return imagen

print(binarizar_imagen(imagencita, 5))
