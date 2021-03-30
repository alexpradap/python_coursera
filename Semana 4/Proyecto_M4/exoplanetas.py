import pandas as pd
import matplotlib.pyplot as plt
import math as m
import numpy as np
import csv

plt.rcParams.update({'font.size': 12})

def cargar_datos(nombre_archivo:str)->pd.DataFrame:
    """ Carga los datos de un archivo csv y retorna el DataFrame con la informacion.
    Parametros:
        nombre_archivo (str): El nombre del archivo CSV que se debe cargar
    Retorno:
        (DataFrame) : El DataFrame con todos los datos contenidos en el archivo
    """
    return pd.read_csv(nombre_archivo)

def histograma_descubrimiento(datos:pd.DataFrame)->None:
    """ Calcula y despliega un histograma con 30 grupos (bins) en el que debe
        aparecer la cantidad de planetas descubiertos por anho.
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
    """
    descubrimientos_por_anio = datos["DESCUBRIMIENTO"]
    histograma = descubrimientos_por_anio.plot(kind="hist", xlim=(1988, 2018), figsize=(8, 4), bins=30, \
        title="Cantidad de planetas descubiertos por año")
    histograma.set_xlabel("Año")
    histograma.set_ylabel("Número de descubrimientos")
    plt.show()

def estado_publicacion_por_descubrimiento(datos:pd.DataFrame)->None:
    """ Calcula y despliega un BoxPlot donde aparecen la cantidad de planetas
        descubiertos por anho, agrupados de acuerdo con el tipo de publicacion.
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
    """
    descubrimientos_por_anio = datos[["DESCUBRIMIENTO", "ESTADO_PUBLICACION"]]
    descubrimientos_por_anio.boxplot(by="ESTADO_PUBLICACION", rot=90, figsize=(8, 6))
    plt.title("Cantidad de planetas descubiertos por año")
    plt.xlabel("Año")
    plt.ylabel("Estado publicación")
    plt.show()

def deteccion_por_descubrimiento(datos:pd.DataFrame)->None:
    """ Calcula y despliega un BoxPlot donde aparecen la cantidad de planetas
        descubiertos por anho, agrupados de acuerdo con el tipo de deteccion
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
    """
    descubrimientos_por_deteccion = datos[["DESCUBRIMIENTO", "TIPO_DETECCION"]]
    descubrimientos_por_deteccion.boxplot(by="TIPO_DETECCION", rot=90, figsize=(8, 6))
    plt.title("Cantidad de planetas descubiertos por tipo de detección")
    plt.xlabel("Año")
    plt.ylabel("Tipo de detección")
    plt.show()

def deteccion_y_descubrimiento(datos:pd.DataFrame,anho:int)->None:
    """ Calcula y despliega un diagrama de pie donde aparecen la cantidad de
        planetas descubiertos en un anho particular, clasificados de acuerdo
        con el tipo de publicacion.
        Si el anho es 0, se muestra la información para todos los planetas.
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
        anho (int): el anho para el que se quieren analizar los planetas descubiertos
                    o 0 para indicar que deben ser todos los planetas.
    """
    descubrimientos_por_anio = datos[["TIPO_DETECCION", "DESCUBRIMIENTO"]]
    descubrimientos_agrupado = descubrimientos_por_anio.groupby(["TIPO_DETECCION"])["DESCUBRIMIENTO"].count()
    if (anho == 0):
        descubrimientos_agrupado.plot.pie(subplots = True, figsize = (8, 6), autopct = '%1.0f%%')
        plt.title("Planetas descubiertos por año")
        plt.ylabel("Tipo de descubrimiento")
    else:
        descubrimientos_por_anio = datos[["TIPO_DETECCION", "DESCUBRIMIENTO"]]
        descubrimientos_anio = descubrimientos_por_anio[datos["DESCUBRIMIENTO"] == anho]
        descubrimientos_agrupado = descubrimientos_anio.groupby(["TIPO_DETECCION"])["DESCUBRIMIENTO"].count()
        descubrimientos_agrupado.plot.pie(subplots = True, figsize = (8, 6), autopct = '%1.0f%%')
        plt.title("Planetas descubiertos en el año: " + str(anho))
        plt.ylabel("Tipo de descubrimiento")
    plt.show()

def cantidad_y_tipo_deteccion(datos:pd.DataFrame)->None:
    """ Calcula y despliega un diagrama de lineas donde aparece una linea por
        cada tipo de deteccion y se muestra la cantidad de planetas descubiertos
        en cada anho, para ese tipo de deteccion.
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
    """
    descubrimientos_por_tipo = datos[["TIPO_DETECCION","DESCUBRIMIENTO"]]
    descubrimientos_agrupado = descubrimientos_por_tipo.groupby(["TIPO_DETECCION"])

    diccionario_grupos = {}
    for name, group in descubrimientos_agrupado:
        group = group.groupby(["DESCUBRIMIENTO"])["TIPO_DETECCION"].count()
        diccionario_grupos[name] = group

    new_df = pd.DataFrame(diccionario_grupos)
    new_df.plot(figsize=(8, 6))
    plt.title("Planetas descubiertos por tipo de detección")
    plt.xlabel("Año")
    plt.ylabel("Planetas descubiertos")
    plt.show()

def masa_promedio_y_tipo_deteccion(datos:pd.DataFrame)->None:
    """ Calcula y despliega un diagrama de lineas donde aparece una linea por
        cada tipo de detección y se muestra la masa promedio de los planetas descubiertos
        en cada anho, para ese tipo de deteccion.
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
    """
    descubrimientos_por_anio = datos[["TIPO_DETECCION", "DESCUBRIMIENTO", "MASA"]]
    descubrimientos_agrupado = descubrimientos_por_anio.groupby(["TIPO_DETECCION"])
    diccionario_grupos = {}
    for name, group in descubrimientos_agrupado:
        group = group.groupby(["DESCUBRIMIENTO"])["MASA"].mean()
        diccionario_grupos[name] = group
    new_df = pd.DataFrame(diccionario_grupos)
    new_df.plot(figsize=(8, 6))
    plt.title("Planetas descubiertos por tipo de detección")
    plt.xlabel("Año")
    plt.ylabel("Planetas descubiertos")
    plt.show()

def masa_planetas_vs_masa_estrellas(datos: pd.DataFrame)->None:
    """ Calcula y despliega un diagrama de dispersión donde en el eje x se
        encuentra la masa de los planetas y en el eje y se encuentra el logaritmo
        de la masa de las estrellas. Cada punto en el diagrama correspondera
        a un planeta y estara ubicado de acuerdo con su masa y la masa de la
        estrella más cercana.
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
    """
    datos_masa_estrellas = datos[["MASA_ESTRELLA", "MASA"]]
    datos_masa_estrellas.plot.scatter(x="MASA", y="MASA_ESTRELLA", logy=True, figsize=(8, 6))
    plt.title("Tamaño Planetas vs Tamaño Estrellas")
    plt.xlabel("Planeta")
    plt.ylabel("Estrella Log(Planeta)")
    plt.show()

def graficar_cielo(datos:pd.DataFrame)->list:
    """ Calcula y despliega una imagen donde aparece un pixel por cada planeta,
        usando colores diferentes que dependen del tipo de detección utilizado
        para descubirlo.
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
    Retorno:
        Una matriz de pixeles con la representacion del cielo
    """
    pass

def filtrar_imagen_cielo(imagen:list)->None:
    """ Le aplica a la imagen un filtro de convolucion basado en la matriz
        [[-1,-1,-1],[-1,9,-1],[-1,-1,-1]]
    Parametros:
        imagen (list): una matriz con la imagen del cielo
    """
    pass



