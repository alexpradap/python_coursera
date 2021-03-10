def calcular_costo_boletas(cantidad_boletas: int, tipo_sala: str, hora_pico: bool, pago_tarjeta_cinema: bool, reserva: bool) -> int:
    sala1 = {"sala": "Dinamix", "precio": 18800}
    sala2 = {"sala": "3D", "precio": 15500}
    sala3 = {"sala": "2D", "precio": 11300}

    salas = [sala1, sala2, sala3]

    precio_base = next(item for item in salas if item["sala"] == tipo_sala).get("precio")
    
    precio = precio_base
    if hora_pico:
        if tipo_sala in ["3D", "2D"]:
            precio = precio + (precio_base * 0.25)
        elif tipo_sala == "Dinamix":
            precio = precio + (precio_base * 0.50)
    else:
        precio = precio - (precio_base * 0.10)
        if cantidad_boletas >= 3:
            precio = precio - 500

    if pago_tarjeta_cinema:
        precio = precio - (precio_base * 0.05)

    if reserva:
        precio = precio + 2000

    return round(precio * cantidad_boletas)