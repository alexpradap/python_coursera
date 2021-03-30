def get_precio(producto: dict) -> int:
    return (producto.get("precio"))

def get_producto(producto: dict) -> str:
    return (producto.get("producto"))

def valor_carrito_compras(catalogo: dict) -> float:
    if len(catalogo) > 0:
        key_list = list(catalogo.keys())
        val_list = list(catalogo.values())
        lista_productos = []
        for i in range (0, len(key_list)):
            producto = {"producto": key_list[i].casefold(), "precio": val_list[i]}
            lista_productos.append(producto)
        
        total = 0
        for producto in lista_productos:
            total = total + producto.get("precio")
        return total
    else:
        return 0