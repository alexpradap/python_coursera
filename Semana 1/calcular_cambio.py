def calcular_cambio(cambio):
    if (cambio >= 500):
        A = int(cambio/500)
    else:
        A = 0

    resto = cambio % 500
    if (resto >= 200):
        B = int(resto/200)
    else:
        B = 0

    resto = resto % 200
    if (resto >= 100):
        C = int(resto/100)
    else:
        C = 0

    resto = resto % 100
    if (resto >= 50):
        D = int(resto/50)
    else:
        D = 0

    return (str(A) + "," + str(B) + "," + str(C) + "," + str(D))
