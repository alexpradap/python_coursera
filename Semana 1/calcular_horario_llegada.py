def calcular_horario_llegada(hora_salida, minuto_salida, segundo_salida, duracion_horas, duracion_minutos, duracion_segundos):
    segundos_llegada = segundo_salida + duracion_segundos
    if (segundos_llegada > 60):
        minutos_llegada = int(segundos_llegada / 60)
        segundos_llegada = segundos_llegada % 60
    else:
        minutos_llegada = 0

    minutos_llegada = minutos_llegada + minuto_salida + duracion_minutos
    if (minutos_llegada > 60):
        hora_llegada = int(minutos_llegada / 60)
        minutos_llegada = minutos_llegada % 60
    else:
        hora_llegada = 0

    hora_llegada = hora_llegada + hora_salida + duracion_horas
    if (hora_llegada > 24):
        hora_llegada = hora_llegada % 24
    if (hora_llegada == 24):
        hora_llegada = 0

    return (str(hora_llegada) + ":" + str(minutos_llegada) + ":" + str(segundos_llegada))
