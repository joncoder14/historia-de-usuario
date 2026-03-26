# app.py
# Archivo principal con el menú
# Importamos todas las funciones de los módulos

from servicios import agregar_producto, mostrar_inventario, buscar_producto, actualizar_producto, eliminar_producto, calcular_estadisticas
from archivos import guardar_csv, cargar_csv

# Inventario inicial vacío
inventario = []
seguir = True

while seguir:
    print("""Menu:
    1. Agregar
    2. Mostrar
    3. Buscar
    4. Actualizar
    5. Eliminar
    6. Estadísticas
    7. Guardar CSV
    8. Cargar CSV
    9. Salir""")

    try:
        opcion = int(input("Ingrese una opción: "))
        
        if opcion == 1:
            # Agregar producto
            correcto = True
            while correcto:
                nombre = input("Ingrese el nombre del producto: ").lower().strip()
                if nombre == "":
                    print("Debes ingresar un nombre")
                else:
                    correcto = False
            v = True
            while v:
                try:
                    cantidad = int(input("Ingrese la cantidad: "))
                    precio = float(input("Ingrese el precio: "))
                except:
                    print("Inválido, intenta de nuevo")
                    continue
                if precio < 0 or cantidad < 0:
                    print("No puede ingresar números negativos")
                else:
                    v = False
            agregar_producto(inventario, nombre, precio, cantidad)

        elif opcion == 2:
            # Mostrar inventario
            mostrar_inventario(inventario)

        elif opcion == 3:
            # Buscar producto
            n = True
            while n:
                nombre = input("Ingrese el nombre del producto: ").lower().strip()
                if nombre == "":
                    print("Debes ingresar un nombre")
                else:
                    n = False
            producto = buscar_producto(inventario, nombre)
            if producto:
                print(producto)
            else:
                print("Producto no encontrado")

        elif opcion == 4:
            # Actualizar producto
            a = True
            while a:
                nombre = input("Ingrese el nombre del producto: ").lower().strip()
                if nombre == "":
                    print("Debes ingresar un nombre")
                else:
                    a = False
            a2 = True
            while a2:
                try:
                    nuevo_precio = float(input("Ingrese el nuevo precio: "))
                    nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
                except:
                    print("Inválido, intenta de nuevo")
                    continue
                if nuevo_precio < 0 or nueva_cantidad < 0:
                    print("No puede ingresar números negativos")
                else:
                    a2 = False
            actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad)

        elif opcion == 5:
            # Eliminar producto
            e = True
            while e:
                nombre = input("Ingrese el nombre del producto: ").lower().strip()
                if nombre == "":
                    print("Debes ingresar un nombre")
                else:
                    e = False
            eliminado = eliminar_producto(inventario, nombre)
            if eliminado:
                print("Producto eliminado")
            else:
                print("No se encontró el producto")

        elif opcion == 6:
            # Estadísticas
            estadisticas = calcular_estadisticas(inventario)
            print("Unidades totales:", estadisticas["unidades_totales"])
            print("Valor total:", estadisticas["valor_total"])
            if estadisticas["producto_mas_caro"]:
                print("Producto más caro:", estadisticas["producto_mas_caro"]["nombre"])
            if estadisticas["producto_mayor_stock"]:
                print("Producto con mayor stock:", estadisticas["producto_mayor_stock"]["nombre"])

        elif opcion == 7:
            # Guardar CSV
            ruta = input("Ingrese la ruta o nombre del archivo CSV: ").strip()
            guardar_csv(inventario, ruta)

        elif opcion == 8:
            # Cargar CSV
            ruta = input("Ingrese la ruta o nombre del archivo CSV a cargar: ").strip()
            inventario_cargado = cargar_csv(ruta)
            if inventario_cargado:
                opcion_sobrescribir = input("¿Sobrescribir inventario actual? (S/N): ").upper()
                if opcion_sobrescribir == "S":
                    inventario = inventario_cargado
                    print("Inventario reemplazado con éxito")
                else:
                    # Fusionar inventario
                    for prod in inventario_cargado:
                        existente = buscar_producto(inventario, prod["nombre"])
                        if existente:
                            existente["cantidad"] += prod["cantidad"]
                            if existente["precio"] != prod["precio"]:
                                existente["precio"] = prod["precio"]
                        else:
                            inventario.append(prod)
                    print("Inventario fusionado con éxito")

        elif opcion == 9:
            print("Saliendo...")
            seguir = False
        else:
            print("Debes elegir una opción del menú")
    except:
        print("Inválido, intenta de nuevo")