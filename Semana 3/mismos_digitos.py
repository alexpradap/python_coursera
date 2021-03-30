def mismos_digitos(a: int, b: bool) -> bool:
    a_str = str(a)
    a_digits = []
    for c in a_str:
        if not (c in a_digits):
            a_digits.append(c)

    b_str = str(b)
    b_digits = []
    for c in b_str:
        if not (c in b_digits):
            b_digits.append(c)

    return set(a_digits) == set(b_digits)