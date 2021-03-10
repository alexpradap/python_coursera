import math

def vel_en_caida_libre(altura: float) -> float:
    v0: float = 0
    Acc: float = 9.8
    return round(math.sqrt((v0 ** 2) + 2 * Acc * altura), 2)
