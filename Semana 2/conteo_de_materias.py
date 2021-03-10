def conteo_de_materias(nombre_materia_1: str, nombre_materia_2: str, nombre_materia_3: str) -> int:
    materias_favoritas = 0
    if (nombre_materia_1.find("programacion") != -1 or
        nombre_materia_1.find("matematica") != -1 or
        nombre_materia_1.find("filosofia") != -1 or
        nombre_materia_1.find("literatura") != -1):
        materias_favoritas = materias_favoritas + 1

    if (nombre_materia_2.find("programacion") != -1 or
        nombre_materia_2.find("matematica") != -1 or
        nombre_materia_2.find("filosofia") != -1 or
        nombre_materia_2.find("literatura") != -1):
        materias_favoritas = materias_favoritas + 1

    if (nombre_materia_3.find("programacion") != -1 or
        nombre_materia_3.find("matematica") != -1 or
        nombre_materia_3.find("filosofia") != -1 or
        nombre_materia_3.find("literatura") != -1):
        materias_favoritas = materias_favoritas + 1

    return materias_favoritas
