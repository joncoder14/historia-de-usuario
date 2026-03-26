# archivos.py
# Módulo para guardar y cargar inventario en CSV

import csv
from servicios import buscar_producto  # Para fusionar inventarios al cargar CSV

def guardar_csv(inventario, ruta):
    """Guarda el inventario en un archivo CSV"""
    if not inventario:
        print("Inventario vacío, no se puede guardar.")
        return
    try:
        with open(ruta, "w", newline="", encoding="utf-8") as archivo:
            campos = ["nombre", "precio", "cantidad"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            for producto in inventario:
                escritor.writerow(producto)
        print(f"Inventario guardado en: {ruta}")
    except Exception as e:
        print("Error al guardar el archivo:", e)


def cargar_csv(ruta):
    """Carga un inventario desde un archivo CSV y devuelve la lista de productos"""
    inventario_cargado = []
    errores = 0
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            if lector.fieldnames != ["nombre", "precio", "cantidad"]:
                print("El archivo CSV no tiene encabezado válido.")
                return []
            for fila in lector:
                try:
                    nombre = fila["nombre"]
                    precio = float(fila["precio"])
                    cantidad = int(fila["cantidad"])
                    if precio < 0 or cantidad < 0:
                        raise ValueError
                    inventario_cargado.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
                except:
                    errores += 1
        if errores > 0:
            print(f"{errores} filas inválidas omitidas")
        return inventario_cargado
    except FileNotFoundError:
        print("Archivo no encontrado.")
    except UnicodeDecodeError:
        print("Error de codificación en el archivo.")
    except Exception as e:
        print("Error al leer el archivo:", e)
    return []