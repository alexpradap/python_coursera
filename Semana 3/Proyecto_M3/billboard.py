import csv 

def cargar_canciones(archivo: str) -> list:
    with open(archivo) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        lista_canciones = []
        for row in csv_reader:
            cancion = {}
            if line_count != 0:
                cancion = {"posicion": row[0], \
                "nombre_cancion": row[1], \
                "nombre_artista": row[2], \
                "anio": int(row[3]), \
                "letra": row[4]}
                lista_canciones.append(cancion)
            line_count += 1
    return lista_canciones    


def retornar_cancion(lista_canciones: list, nombre_cancion: str, anio: int) -> dict:
    cancion = None
    for elemento in lista_canciones:
        if elemento.get("nombre_cancion") == nombre_cancion and elemento.get("anio") == anio:
                cancion = elemento
                break
        else:
            continue
    return cancion

def retornar_canciones_anio(lista_canciones: list, anio: int) -> list:
    canciones = []
    for cancion in lista_canciones:
        if cancion.get("anio") == anio:
                cancion.pop("letra")
                canciones.append(cancion)
        else:
            continue
    return canciones

def retornar_canciones_artista_periodo(lista_canciones: list, nombre_artista: str, anio_ini: int, anio_fin: int) -> list:
    canciones_artista = []
    for cancion in lista_canciones:
        if cancion.get("nombre_artista") == nombre_artista and \
        cancion.get("anio") >= anio_ini and \
        cancion.get("anio") <= anio_fin:
            cancion.pop("letra")
            canciones_artista.append(cancion)
        else:
            continue
    return canciones_artista

def retornar_canciones_artista(lista_canciones: list, nombre_artista: str) -> list:
    canciones_artista = []
    for cancion in lista_canciones:
        if cancion.get("nombre_artista") == nombre_artista:
            cancion.pop("letra")
            canciones_artista.append(cancion)
        else:
            continue
    return canciones_artista

def retornar_artistas_cancion(lista_canciones: list, nombre_cancion: str) -> list:
    artistas_cancion = []
    for cancion in lista_canciones:
        if cancion.get("nombre_cancion") == nombre_cancion:
            artistas_cancion.append(cancion.get("nombre_artista"))
        else:
            continue
    return artistas_cancion

def cantidad_canciones_por_artista(lista_canciones: list, cantidad_minima: int) -> dict:
    canciones_por_artista = {}
    for cancion in lista_canciones:
        if cancion.get("nombre_artista") in canciones_por_artista:
            canciones_por_artista[cancion.get("nombre_artista")] = canciones_por_artista.get(cancion.get("nombre_artista")) + 1
        else:
            canciones_por_artista[cancion.get("nombre_artista")] = 1
    
    canciones_por_artista_copy = canciones_por_artista.copy()
    for artista, num_canciones in canciones_por_artista.items():
        if num_canciones <= cantidad_minima:
            canciones_por_artista_copy.pop(artista)
    
    return canciones_por_artista_copy

def get_num_canciones(artista: dict) -> int:
    return artista.get("num_canciones")

def get_artista(canciones_por_artista: list, nombre_artista: str) -> dict:
    artista = None
    for element in canciones_por_artista:
        if element.get("nombre_artista") == nombre_artista:
            artista = element
            break
    return artista

def artista_mas_canciones(lista_canciones: list) -> dict:
    canciones_por_artista = []
    for cancion in lista_canciones:
        este_artista = get_artista(canciones_por_artista, cancion.get("nombre_artista"))
        if este_artista is None:
            canciones_por_artista.append({"nombre_artista": cancion.get("nombre_artista"), "num_canciones": 1})
        else:
            este_artista["num_canciones"] = este_artista["num_canciones"] + 1
    canciones_por_artista.sort(key=get_num_canciones, reverse=True)
    return {canciones_por_artista[0].get("nombre_artista"): canciones_por_artista[0].get("num_canciones")}

def canciones_de_un_artista(lista_canciones: list) -> dict:
    artistas = {}
    for cancion in lista_canciones:
        if cancion.get("nombre_artista") in artistas:
            if artistas[cancion.get("nombre_artista")].count(cancion.get("nombre_cancion")) == 0:
                artistas[cancion.get("nombre_artista")].append(cancion.get("nombre_cancion"))
        else:
            artistas[cancion.get("nombre_artista")] = [cancion.get("nombre_cancion")]
    return artistas

def promedio_canciones(lista_canciones: list) -> float:
    artistas = []
    canciones = []
    for cancion in lista_canciones:
        if artistas.count(cancion.get("nombre_artista")) == 0:
            artistas.append(cancion.get("nombre_artista"))
        if canciones.count(cancion.get("nombre_cancion")) == 0:
            canciones.append(cancion.get("nombre_cancion"))
    return len(canciones) / len(artistas)

print(cantidad_canciones_por_artista(cargar_canciones("billboard.csv"), 10))