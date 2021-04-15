import pandas as pd
import math

boxes = {'MODELO': ['Bus urbano #27','Silla tipo bar','Piano','Fuente con flores','Bus urbano #27','Puesto de Yogurth','Playground','Bus urbano #27'],
         'USUARIO': ['Ted Mosby','Art Vandelay','Art Vandelay','Michael','Mark Brendanawicz','Michael','Mark Brendanawicz','LeCorbusier_2020'],
         'PAGO': [24.99,4.99,4.99,0,12,0,14,0],
         'ESTRELLAS': [5,3.5,3.5,5,4,5,4.5,1],
         'COMENTARIO': [True,False,False,True,True,True,True,True]
        }

df = pd.DataFrame(boxes, columns =  ['MODELO','USUARIO','PAGO','ESTRELLAS','COMENTARIO'])

def calcular_estadisticas_original(descargas: pd.DataFrame) -> pd.DataFrame:
    indexes = []
    data = {'CANTIDAD': [], 'PROMEDIO': [], 'MAXIMO': [], 'MINIMO': [], 'ESTRELLAS': [], 'DESV. ESTRELLAS': [], 'COMENTARIOS': []}

    modelos = descargas.MODELO.unique()
    modelos.sort()
    
    for modelo in modelos:
        selected_rows = descargas.loc[descargas['MODELO'] == modelo].loc[descargas['PAGO'] > 0]

        num_rows = len(selected_rows)
        if num_rows > 0:
            indexes.append(modelo)
            data['CANTIDAD'].append(num_rows)
            #data['PROMEDIO'].append(round(selected_rows['PAGO'].mean(), 2))
            data['PROMEDIO'].append(round(descargas.groupby('MODELO')['PAGO'].mean()[modelo], 2))
            data['MAXIMO'].append(selected_rows['PAGO'].max())
            data['MINIMO'].append(selected_rows['PAGO'].min())
            data['ESTRELLAS'].append(round(selected_rows['ESTRELLAS'].mean(), 2))
            
            desv_estrellas = selected_rows['ESTRELLAS'].std()
            data['DESV. ESTRELLAS'].append(round(desv_estrellas, 2) if not math.isnan(desv_estrellas) else 0.0)
            
            data['COMENTARIOS'].append(len(selected_rows[selected_rows['COMENTARIO'] == True]))
            
    return pd.DataFrame(data, columns = ['CANTIDAD', 'PROMEDIO', 'MAXIMO', 'MINIMO', 'ESTRELLAS', 'DESV. ESTRELLAS', 'COMENTARIOS'], index = indexes)

def calcular_estadisticas(descargas: pd.DataFrame) -> pd.DataFrame:
    indexes = []
    data = {}

    selected_rows = descargas.loc[descargas['PAGO'] > 0]
    modelos = selected_rows.MODELO.unique()
    grouped_rows = selected_rows.groupby('MODELO')
    data['CANTIDAD'] = grouped_rows['MODELO'].count()
    data['PROMEDIO'] = grouped_rows['PAGO'].mean()
    data['MAXIMO'] = grouped_rows['PAGO'].max()
    data['MINIMO'] = grouped_rows['PAGO'].min()
    data['ESTRELLAS'] = grouped_rows['ESTRELLAS'].mean()
    data['DESV. ESTRELLAS'] = grouped_rows['ESTRELLAS'].std().fillna(0)
    data['COMENTARIOS'] = selected_rows.loc[selected_rows['COMENTARIO'] == True].groupby('MODELO')['MODELO'].count()
    
    return pd.DataFrame(data, columns = ['CANTIDAD', 'PROMEDIO', 'MAXIMO', 'MINIMO', 'ESTRELLAS', 'DESV. ESTRELLAS', 'COMENTARIOS'], index = modelos).fillna(0).round(2).sort_index()

print(calcular_estadisticas(df))