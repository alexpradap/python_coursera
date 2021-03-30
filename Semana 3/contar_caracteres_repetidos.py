def contar_caracteres_repetidos (cadena: str) -> int:
    alfabeto = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", \
    "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]
    x = 0
    for c in alfabeto:
        if cadena.count(c) > 1:
            x = x +1
    return x