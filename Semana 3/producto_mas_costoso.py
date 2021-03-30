def get_precio(producto: dict) -> int:
    return (producto.get("precio"))

def get_producto(producto: dict) -> str:
    return (producto.get("producto"))

def producto_mas_costoso(catalogo: dict) -> str:
    if len(catalogo) > 0:
        key_list = list(catalogo.keys())
        val_list = list(catalogo.values())
        lista_productos = []
        for i in range (0, len(key_list)):
            producto = {"producto": key_list[i].casefold(), "precio": val_list[i]}
            lista_productos.append(producto)
        
        lista_productos.sort(key = get_precio, reverse = True)
        mayor_valor = lista_productos[0].get("precio")

        cloned_list = lista_productos.copy()
        for producto in cloned_list:
            if producto.get("precio") < mayor_valor:
                lista_productos.remove(producto)
        
        if len(lista_productos) > 1:
            lista_productos.sort(key = get_producto, reverse = False)
        return lista_productos[0].get("producto")
    else:
        return "No hay productos en el carrito"