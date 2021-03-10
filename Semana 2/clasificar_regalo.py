def to_backwards(number: int) -> int:
    str_number = str(number)
    l = len(str_number)
    rebmun_rts = ""

    for x in range(l-1, -1, -1):
        rebmun_rts = rebmun_rts + str_number[x]

    return int(rebmun_rts)

def clasificar_regalo (id: int) -> str:
    es_palindromo = False
    if (id == to_backwards(id)):
        es_palindromo = True

    es_par = False
    if (id % 2 == 0):
        es_par = True

    if (es_palindromo == True):
        if (es_par == True):
            return "boy"
        else:
            return "girl"
    else:
        if (es_par == True):
            return "man"
        else:
            return "woman"
