def encontrar_mayor (entrada: list) -> int:
    if (len(entrada) == 0):
        return -1
    else:
        entrada.sort(reverse = True)
        return entrada[0]