def hacer_la_vaca(salon: list, vaca: str) -> list:
    mayor_aporte = {"valor": 0, "i": -1,  "j": -1}
    valor_vaca = 0
    for i in salon:
        for j in i:
            valor_vaca = valor_vaca + j
            if j > mayor_aporte.get("valor"):
                mayor_aporte["valor"] = j
                mayor_aporte["i"] = salon.index(i)
                mayor_aporte["j"] = i.index(j)
    
    if (vaca == "botella") and (valor_vaca >= 120000):
        return ["Hay vaca", mayor_aporte.get("i"), mayor_aporte.get("j")]
    elif (vaca == "pastel") and (valor_vaca >= 35000):
        return ["Hay vaca", mayor_aporte.get("i"), mayor_aporte.get("j")]
    else:
        return ["No Alcanza", mayor_aporte.get("i"), mayor_aporte.get("j")]