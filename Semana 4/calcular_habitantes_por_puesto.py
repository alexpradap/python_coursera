import pandas as pd

def calcular_habitantes_por_puesto(poblacion: pd.DataFrame, universidades: pd.DataFrame) -> \
pd.DataFrame:
    resultado_dict = {"Pais": [], "habitantes_por_puesto": []}
    for index, row in poblacion.iterrows():
        universidades_filtrado = universidades.loc[universidades["country"] == row["Pais"]]
        nro_filas = len(universidades_filtrado.index)
        if nro_filas > 0:
            resultado_dict["Pais"].append(row["Pais"])
            total_estudiantes_universitarios = universidades_filtrado["num_students"].sum()
            resultado_dict["habitantes_por_puesto"].append(\
                round(row["Poblacion"] / total_estudiantes_universitarios, 1)\
            )
    resultado = pd.DataFrame(resultado_dict, columns =  ["Pais", "habitantes_por_puesto"])
    resultado = resultado.sort_values(by = ["habitantes_por_puesto"], ascending = [True])
    return resultado
