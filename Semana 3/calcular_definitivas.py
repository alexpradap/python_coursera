def calcular_definitivas (estudiantes: list) -> list:
    for estudiante in estudiantes:
        if estudiante["nota"] >= 4.5:
            estudiante["nota"] = 5.0
        elif estudiante["nota"] >= 3.5 and estudiante["nota"] < 4.5:
            estudiante["nota"] = 4.0
        elif estudiante["nota"] >= 2.5 and estudiante["nota"] < 3.5:
            estudiante["nota"] = 3.0
        else:
            estudiante["nota"] = 1.5
    return estudiantes