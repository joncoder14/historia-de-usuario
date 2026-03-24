#variable de control para el bucle
active = True

#bucle para volver a pedir datos hasta que sea valido
while active:
  #pedir dato al usuario
    nombre = input("Ingrese el nombre del producto: ")

    # validar cantidad
    c = True
    while c:
        try:
          #pedir dato
            cantidad = int(input("Ingrese cantidad: "))
            #cumplir una condicion
            if cantidad >= 0:
              #rompe el bucle
                c = False
            #si no se cumple la condicion
            else:
                print("La cantidad no puede ser negativa.")
        #si los datos son invalidos
        except:
            print("Debe ingresar un número entero válido.")

    # validar precio
    p = True
    while p:
        try:
          #pedir dato
            precio = float(input("Ingrese el precio: "))
            #cumplir una condicion
            if precio >= 0:
              #rompe el bucle
                p = False
            #si la condicion no se cumple
            else:
                print("El precio no puede ser negativo.")
        #si los datos son invalidos
        except:
            print("Debe ingresar un número válido.")

    #rompe el bucle principal
    active = False

#calcula el costo total
costo_total = precio * cantidad
#muestra todos los datos
print("Producto:", nombre)
print("Precio:", precio)
print("Cantidad:", cantidad)
print("Costo total:", costo_total)
#este pequeño programa pide los datos de un producto al usuario luego pida la cantida que desea llevar se encarga de validar los datos y que la cantidad sea mayor a cero luego calcula el costo total y muestra en pantalla todos los datos