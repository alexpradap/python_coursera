def upd_ori(oa: int, giro: str) -> int:
    if (giro == "L"):
        g = -1
    if (giro == "H"):
        g = 2
    if (giro == "R"):
        g = 1
    if (giro == "."):
        g = 0

    if (oa == 0 and g == -1):
        return 3
    else:
        if (oa + g > 3):
            return -1 + (oa + g - 3)
        else:
            return oa + g

def movimiento_robot (orientacion_actual: str, giro_1: str, giro_2: str, giro_3: str) -> str:
    brujula = "WNES"

    if (orientacion_actual == "W"):
        oa = 0
    if (orientacion_actual == "N"):
        oa = 1
    if (orientacion_actual == "E"):
        oa = 2
    if (orientacion_actual == "S"):
        oa = 3

    oa = upd_ori(oa, giro_1)
    oa = upd_ori(oa, giro_2)
    oa = upd_ori(oa, giro_3)

    return brujula[oa]
