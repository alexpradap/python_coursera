"""
Ejercicio nivel 2: Agenda de peliculas.
Módulo de cálculos.

Temas:
* Variables.
* Tipos de datos.
* Expresiones aritmeticas.
* Instrucciones basicas y consola.
* Dividir y conquistar: funciones y paso de parametros.
* Especificacion y documentacion.
* Instrucciones condicionales.
* Diccionarios.
@author: Cupi2

NOTA IMPORTANTE PARA TENER EN CUENTA EN TODAS LAS FUNCIONES DE ESTE MODULO:
        Los diccionarios de pelicula tienen las siguientes parejas de clave-valor:
            - nombre (str): Nombre de la pelicula agendada.
            - genero (str): Generos de la pelicula separados por comas.
            - duracion (int): Duracion en minutos de la pelicula
            - anio (int): Anio de estreno de la pelicula
            - clasificacion (str): Clasificacion de restriccion por edad
            - hora (int): Hora de inicio de la pelicula
            - dia (str): Indica que día de la semana se planea ver la película
"""
import datetime

def crear_pelicula(nombre: str, genero: str, duracion: int, anio: int, 
                  clasificacion: str, hora: int, dia: str) -> dict:
    """Crea un diccionario que representa una nueva película con toda su información 
       inicializada.
    Parámetros:
        nombre (str): Nombre de la pelicula agendada.
        genero (str): Generos de la pelicula separados por comas.
        duracion (int): Duracion en minutos de la pelicula
        anio (int): Anio de estreno de la pelicula
        clasificacion (str): Clasificacion de restriccion por edad
        hora (int): Hora a la cual se planea ver la pelicula, esta debe estar entre 
                    0 y 2359
        dia (str): Dia de la semana en el cual se planea ver la pelicula.
    Retorna:
        dict: Diccionario con los datos de la pelicula
    """    
    return {"nombre": nombre, "genero": genero, "duracion": duracion, "anio": anio, \
    "clasificacion": clasificacion, "hora": hora, "dia": dia}

def encontrar_pelicula(nombre_pelicula: str, p1: dict, p2: dict, p3: dict, p4: dict,  p5: dict) -> dict:
    """Encuentra en cual de los 5 diccionarios que se pasan por parametro esta la 
       pelicula cuyo nombre es dado por parametro.
       Si no se encuentra la pelicula se debe retornar None.
    Parametros:
        nombre_pelicula (str): El nombre de la pelicula que se desea encontrar.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: Diccionario de la pelicula cuyo nombre fue dado por parametro. 
        None si no se encuentra una pelicula con ese nombre.
    """
    lista_peliculas = [p1, p2, p3, p4, p5]
    pelicula_encontrada = None
    for pelicula in lista_peliculas:
        if (pelicula.get("nombre") == nombre_pelicula):
            pelicula_encontrada = pelicula
            break
    return pelicula_encontrada

def get_duracion(pelicula: dict) -> str:
    return pelicula.get("duracion")

def encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> dict:
    """Encuentra la pelicula de mayor duracion entre las peliculas recibidas por
       parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: El diccionario de la pelicula de mayor duracion
    """
    peliculas_por_duracion = [p1, p2, p3, p4, p5]
    peliculas_por_duracion.sort(key=get_duracion, reverse=True)
    return peliculas_por_duracion[0]

def duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> str:
    """Calcula la duracion promedio de las peliculas que entran por parametro. 
       Esto es, la duración total de todas las peliculas dividida sobre el numero de peliculas. 
       Retorna la duracion promedio en una cadena de formato 'HH:MM' ignorando los posibles decimales.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        str: la duracion promedio de las peliculas en formato 'HH:MM'
    """
    suma = p1.get("duracion") + p2.get("duracion") + p3.get("duracion") + p4.get("duracion") + p5.get("duracion")
    promedio = suma / 5
    promedio_horas = int(promedio / 60)
    promedio_minutos = promedio % 60
    return str(promedio_horas) + ":" + str(promedio_minutos)

def encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict, anio: int) -> str:
    """Busca entre las peliculas cuales tienen como anio de estreno una fecha estrictamente
       posterior a la recibida por parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
        anio (int): Anio limite para considerar la pelicula como estreno.
    Retorna:
        str: Una cadena con el nombre de la pelicula estrenada posteriormente a la fecha recibida. 
        Si hay mas de una pelicula, entonces se retornan los nombres de todas las peliculas 
        encontradas separadas por comas. Si ninguna pelicula coincide, retorna "Ninguna".
    """
    estrenos = "Ninguna"
    lista_peliculas = [p1, p2, p3, p4, p5]
    for pelicula in lista_peliculas:
        if (pelicula.get("anio") > anio):
            if (estrenos == "Ninguna"):
                estrenos = pelicula.get("nombre")
            else:
                estrenos = estrenos + "," + pelicula.get("nombre")
    return estrenos

def cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> int:
    """Indica cuantas peliculas de clasificación '18+' hay entre los diccionarios recibidos.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        int: Numero de peliculas con clasificacion '18+'
    """
    peliculas_18_plus = 0
    lista_peliculas = [p1, p2, p3, p4, p5]
    for pelicula in lista_peliculas:
        if (pelicula.get("clasificacion") == "18+"):
            peliculas_18_plus = peliculas_18_plus + 1
    return peliculas_18_plus

def evaluar_conflicto(hora: int, dia: str, duracion: int, peli: dict) -> bool:
    conflicto = False
    
    lista_dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    
    today = datetime.date.today()
    next_week_start = today + datetime.timedelta(days = 7 - today.weekday())
    
    str_hora = str(hora)
    if hora < 1000:
        str_hora = "0" + str_hora
    nvo_inicio = datetime.datetime(\
        next_week_start.year,\
        next_week_start.month,\
        next_week_start.day + lista_dias.index(dia),\
        int(str_hora[0:2]),\
        int(str_hora[2:4]))
    nvo_fin = nvo_inicio + datetime.timedelta(minutes = duracion)

    peli_hora = str(peli.get("hora"))
    if peli.get("hora") < 1000:
        peli_hora = "0" + peli_hora

    peli_inicio = datetime.datetime(\
        next_week_start.year,\
        next_week_start.month,\
        next_week_start.day + lista_dias.index(peli.get("dia")),\
        int(peli_hora[0:2]),\
        int(peli_hora[2:4]))
    peli_fin = peli_inicio + datetime.timedelta(minutes = peli.get("duracion"))

    if (nvo_inicio >= peli_inicio and nvo_inicio <= peli_fin) or \
        (nvo_fin >= peli_inicio and nvo_fin <= peli_fin):
        conflicto = True
    
    return conflicto

def reagendar_pelicula(peli:dict, nueva_hora: int, nuevo_dia: str, 
                       control_horario: bool, p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->bool: 
    """Verifica si es posible reagendar la pelicula que entra por parametro. Para esto verifica
       si la nueva hora y el nuevo dia no entran en conflicto con ninguna otra pelicula, 
       y en caso de que el usuario haya pedido control horario verifica que se cumplan 
       las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula a reagendar
        nueva_hora (int): Nueva hora a la cual se quiere ver la pelicula
        nuevo_dia (str): Nuevo dia en el cual se quiere ver la pelicula
        control_horario (bool): Representa si el usuario quiere o no controlar
                                el horario de las peliculas.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        bool: True en caso de que se haya podido reagendar la pelicula, False de lo contrario.
    """

    pasa_preferencias = True

    if (control_horario):
        if (peli.get("genero").find("Documental") != -1 and nueva_hora >= 2200):
            pasa_preferencias = False

        if (peli.get("genero").find("Drama") != -1 and nuevo_dia == "Viernes"):
            pasa_preferencias = False

        weekdays_too_late = ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves"]
        weekdays_too_early = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
        
        if ((nuevo_dia in weekdays_too_late and nueva_hora >= 2300) or \
        (nuevo_dia in weekdays_too_early and nueva_hora <= 600)):
            pasa_preferencias = False
        
    pasa_conflictos = True
    lista_peliculas = [p1, p2, p3, p4, p5]
    for pelicula in lista_peliculas:
        if (evaluar_conflicto(nueva_hora, nuevo_dia, peli.get("duracion"), pelicula)):
            pasa_conflictos = False
            break

    return pasa_preferencias and pasa_conflictos
    
def decidir_invitar(peli: dict, edad_invitado: int, autorizacion_padres: bool)->bool:
    """Verifica si es posible invitar a la persona cuya edad entra por parametro a ver la 
       pelicula que entra igualmente por parametro. 
       Para esto verifica el cumplimiento de las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula que se desea ver con el invitado
        edad_invitado (int): Edad del invitado con quien se desea ver la pelicula
        autorizacion_padres (bool): Indica si el invitado cuenta con la autorizacion de sus padres 
        para ver la pelicula
    Retorna:
        bool: True en caso de que se pueda invitar a la persona, False de lo contrario.
    """

    if edad_invitado >= 18:
        return True
    else:
        if peli.get("genero").find("Terror") != -1 and edad_invitado >= 15:
            return True
        else:
            if edad_invitado <= 10 and peli.get("genero").find("Familiar") != -1:
                return True
            else:
                if peli.get("genero").find("Documental") != -1:
                    return True
                else:
                    if autorizacion_padres:
                        return True
                    else:
                        return False