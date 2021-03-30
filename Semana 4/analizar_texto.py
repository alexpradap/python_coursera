def appareances(texto: str, palabra: str) -> tuple:
    count = 0
    first = None
    last = None

    len_texto = len(texto)
    len_palabra = len(palabra)
    for x in range(0, len_texto):
        if palabra == texto[x:x + len_palabra]:
            count = count + 1
            last = x
            if first == None:
                first = last
    return (count, first, last)

def analizar_texto(texto: str, caracteres_permitidos: list) -> dict:
    lista_palabras = []
    ini = 0
    for i in range(0, len(texto)):
        if  caracteres_permitidos.count(texto[i]) == 0:
            lista_palabras.append(texto[ini:i])
            ini = i + 1
        if (i == len(texto) - 1):
            lista_palabras.append(texto[ini:i + 1])
    
    diccionario_palabras = {}

    for palabra in lista_palabras:
        diccionario_palabras[palabra.casefold()] = appareances(texto, palabra)
    
    return diccionario_palabras