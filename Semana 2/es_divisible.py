def es_divisible(n: int, d:int) -> int:
    if (d == 0):
        return 0
    else:
        if (n % (2 * d) == 0):
            return 2
        else:
            if (n % d == 0):
                return 1
            else:
                return 0
