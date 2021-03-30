imagencita = [[(1,2,3),(4,5,6),(7,8,9)],\
          [(7,8,9),(1,2,3),(4,5,6)],\
          [(4,5,6),(7,8,9),(1,2,3)]]

def reflejar_imagen(imagen: list) -> list:
    nueva_lista = []
    for i in range (0, len(imagen)):
        nueva_fila = []
        for j in range (len(imagen[i]) - 1, -1, -1):
            nueva_fila.append(imagen[i][j])
        nueva_lista.append(nueva_fila)
    return nueva_lista

print(reflejar_imagen(imagencita))
