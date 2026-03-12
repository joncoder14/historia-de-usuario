active = True

while active:
    nombre = input("Ingrese el nombre del producto: ")

    # validar cantidad
    while True:
        try:
            cantidad = int(input("Ingrese cantidad: "))
            if cantidad >= 0:
                break
            else:
                print("La cantidad no puede ser negativa.")
        except:
            print("Debe ingresar un número entero válido.")

    # validar precio
    while True:
        try:
            precio = float(input("Ingrese el precio: "))
            if precio >= 0:
                break
            else:
                print("El precio no puede ser negativo.")
        except:
            print("Debe ingresar un número válido.")

    active = False


costo_total = precio * cantidad

print("Producto:", nombre)
print("Precio:", precio)
print("Cantidad:", cantidad)
print("Costo total:", costo_total)