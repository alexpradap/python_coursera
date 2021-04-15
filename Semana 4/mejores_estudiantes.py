import pandas as pd

estudiantes_dict = {'nombre': ['Alexander Prada','Marcela Plazas','Camilo Prada','Rafael Zapata','Wilson López','Benito Camelo','Alí Kate','Sandra Huelvas'],
         'matematicas': [1.0,3.5,4.8,2.9,3.0,4.2,0.0,3.7],
         'ingles': [3.7,4.8,3.5,1.0,2.9,3.0,4.2,0.0],
         'ciencias': [4.8,3.7,3.0,1.0,2.9,3.5,0.0,4.2],
         'literatura': [3.7,4.8,1.0,3.0,3.5,2.9,4.2,0.0],
         'arte': [0.0,4.2,2.9,3.5,3.0,1.0,4.2,3.7]
        }

estudiantes = pd.DataFrame(estudiantes_dict, columns =  ['nombre','matematicas','ingles','ciencias','literatura', 'arte'])

def mejores_estudiantes (estudiantes: pd.DataFrame) -> pd.DataFrame:
    top_25 = int(len(estudiantes) / 4)
    new_column = estudiantes.loc[: , "matematicas":"arte"]
    estudiantes['promedio'] = new_column.mean(axis=1)
    filtered_df = estudiantes.sort_values(by=["promedio"], ascending=[False]).head(top_25)
    return filtered_df[['nombre', 'promedio']]

print(mejores_estudiantes(estudiantes))