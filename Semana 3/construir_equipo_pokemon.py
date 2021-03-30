def sum_est(pokemon: dict) -> int:
    return pokemon["ataque"] + pokemon["defensa"] + pokemon["ataque_especial"] +\
    pokemon["defensa_especial"] + pokemon["velocidad"] + pokemon["vida"]

def construir_equipo_pokemon(Cantidad: int, Lista_pkmn: list) -> list:
    lista_equipo = []
    for pokemon in Lista_pkmn:
        if sum_est(pokemon) >= 600:
            lista_equipo.append(pokemon["nombre"])
        if len(lista_equipo) == Cantidad:
            break
    
    if len(lista_equipo) == Cantidad:
        return lista_equipo
    else:
        return None
