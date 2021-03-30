def ordenar_cadena (cadena: str) -> str:
    alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", \
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    x = ""
    for c in alfabeto:
        cc = cadena.count(c)
        if cc > 0:
            for i in range(1, cc + 1):
                x = x + c
    return x