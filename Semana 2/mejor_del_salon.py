def promedio (estudiante: dict) -> float:
    suma = estudiante.get("matematicas") + estudiante.get("español") +\
    estudiante.get("ciencias") + estudiante.get("literatura") + estudiante.get("arte")
    promedio = suma / 5
    return promedio

def get_promedio (estudiante: dict):
    return (estudiante.get("promedio"))

def mejor_del_salon (
estudiante1: dict,
estudiante2: dict,
estudiante3: dict,
estudiante4: dict,
estudiante5: dict
) -> str:
    promEst1 = {
        "nombre": estudiante1.get("nombre"),
        "promedio": promedio(estudiante1)
    }

    promEst2 = {
        "nombre": estudiante2.get("nombre"),
        "promedio": promedio(estudiante2)
    }

    promEst3 = {
        "nombre": estudiante3.get("nombre"),
        "promedio": promedio(estudiante3)
    }

    promEst4 = {
        "nombre": estudiante4.get("nombre"),
        "promedio": promedio(estudiante4)
    }

    promEst5 = {
        "nombre": estudiante5.get("nombre"),
        "promedio": promedio(estudiante5)
    }

    listaPromedio = [promEst1, promEst2, promEst3, promEst4, promEst5]
    listaPromedio.sort(key=get_promedio, reverse=True)

    mejorPromedio = listaPromedio[0].get("promedio")
    listaMejores = []
    for elemento in listaPromedio:
        if (elemento.get("promedio") == mejorPromedio):
            listaMejores.append(elemento.get("nombre").lower())
    
    listaMejores.sort(reverse=False)
    
    return listaMejores[0]