def sucesion_fibonacci(cantidad_numeros: int) -> str:
    serie = []
    for i in range (0, cantidad_numeros):
        if (i == 0) or (i == 1):
            serie.append(i)
        else:
            serie.append(serie[i - 1] + serie[i - 2])
    string = ""
    for i in serie:
        if string == "":
            string = str(i)
        else:
            string = string + "," + str(i)
    return string