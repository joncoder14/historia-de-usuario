# servicios.py
# Módulo con funciones de CRUD y estadísticas

# No necesita importar nada porque todo se maneja en memoria

def agregar_producto(inventario, nombre, precio, cantidad):
    """Agrega un producto al inventario"""
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    inventario.append(producto)


def mostrar_inventario(inventario):
    """Muestra todos los productos del inventario"""
    for i, producto in enumerate(inventario):
        print(i, producto)


def buscar_producto(inventario, nombre):
    """Busca un producto por nombre, devuelve el diccionario o None"""
    for producto in inventario:
        if producto["nombre"] == nombre:
            return producto
    return None


def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """Actualiza precio y/o cantidad de un producto existente"""
    producto = buscar_producto(inventario, nombre)
    if producto:
        if nuevo_precio is not None:
            producto["precio"] = nuevo_precio
        if nueva_cantidad is not None:
            producto["cantidad"] = nueva_cantidad
        return True
    return False


def eliminar_producto(inventario, nombre):
    """Elimina un producto del inventario"""
    producto = buscar_producto(inventario, nombre)
    if producto:
        inventario.remove(producto)
        return True
    return False


def calcular_estadisticas(inventario):
    """Calcula unidades totales, valor total, producto más caro y producto con mayor stock"""
    unidades_totales = 0
    valor_total = 0
    producto_mas_caro = None
    producto_mayor_stock = None

    for producto in inventario:
        unidades_totales += producto["cantidad"]
        valor_total += producto["cantidad"] * producto["precio"]

        if producto_mas_caro is None or producto["precio"] > producto_mas_caro["precio"]:
            producto_mas_caro = producto

        if producto_mayor_stock is None or producto["cantidad"] > producto_mayor_stock["cantidad"]:
            producto_mayor_stock = producto

    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": producto_mas_caro,
        "producto_mayor_stock": producto_mayor_stock
    }