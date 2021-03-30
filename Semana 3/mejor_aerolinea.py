def mejor_aerolinea(vuelos: dict) -> str:
    lista_vuelos = list(vuelos.values())
    aerolineas_por_retraso = {}
    
    for vuelo in lista_vuelos:
        if aerolineas_por_retraso.get(vuelo.get("aerolinea")) is None:
            aerolineas_por_retraso[vuelo.get("aerolinea")] = vuelo.get("retraso")
        else:
            acumulado = aerolineas_por_retraso.get(vuelo.get("aerolinea"))
            aerolineas_por_retraso[vuelo.get("aerolinea")] = acumulado + vuelo.get("retraso")

    dict(sorted(aerolineas_por_retraso.items(), key=lambda item: item[1]))
    keys_view = aerolineas_por_retraso.keys()
    keys_iterator = iter(keys_view)
    first_key = next(keys_iterator)
    return first_key
