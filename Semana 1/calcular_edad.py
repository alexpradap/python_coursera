def calcular_edad(dia_nacio: int, mes_nacio: int, anio_nacio: int, dia_actual: int, mes_actual: int, anio_actual: int) -> str:
    dias_edad: int
    meses_edad: int
    anios_edad: int

    if  (anio_actual == anio_nacio and mes_actual == mes_nacio):
        anios_edad = 0
        meses_edad = 0
        dias_edad = dia_actual - dia_nacio
    else:
        if (mes_actual > mes_nacio):
            anios_edad = anio_actual - anio_nacio
            meses_edad = mes_actual - mes_nacio
        else:
            anios_edad = anio_actual - anio_nacio - 1
            meses_edad = (12 - mes_nacio) + mes_actual

        if (dia_actual > dia_nacio):
            dias_edad = dia_actual - dia_nacio
        else:
            meses_edad = meses_edad - 1
            dias_edad = (30 - dia_nacio) + dia_actual

    return(str(anios_edad) + "," + str(meses_edad) + "," + str(dias_edad))


print(calcular_edad(20, 11, 1986, 16, 10, 1987))
print(calcular_edad(20, 11, 1986, 21, 12, 1986))
