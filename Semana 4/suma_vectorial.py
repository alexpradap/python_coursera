def suma_vectorial(vector_1: tuple, vector_2: tuple) -> tuple:
    vector_resultado =[]
    for i in range(0, len(vector_1)):
        vector_resultado.append(vector_1[i] + vector_2[i])
    return tuple(vector_resultado)