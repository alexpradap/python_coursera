def buscar_elemento(entrada: list, buscado: int) -> int:
    try:
        indice = entrada.index(buscado)
    except:
        indice = -1
    return indice