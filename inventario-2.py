#creo la lista vacia 
inventario = []
#variable de control
active = True
#funcion para agregar un producto
def agregar_producto(lista):
    #pido los datos y los valido
     nombre = input("ingrese el nombre del producto: ")
     #bucle para volver a pedir en caso de que sean invalidos
     p = True
     while p:
            try:
                precio = float(input("ingrece el precio: "))
                cantidad = int(input("ingrese la cantidad: "))
                #rompo el bucle
                p = False
            except:
                print("ingrese una opcion valida")
            producto = {"nombre":nombre, "precio":precio ,"cantidad":cantidad }
            inventario.append(producto)
            #retorno el producto
            return producto
#funcion para mostrar el inventario
def mostrar_inventario(lista):
    #condicion si la lista esta vacia
     if not lista:
            print("el inventario esta vacio")
    #recorro la lista para mostarar su contenido
     for p in lista:
            print("nombre :", p["nombre"])
            print("cantida :", p["cantidad"])
            print("precio :", p["precio"])
            print("____")
#funcion para calcular las estadisticas
def calcular_estadistica(lista):
    #variables contenedoras para llevar un contador
     total_todo = 0
     total_cantidad = 0
     #recorro la lista
     for p in lista:
        #calculo precio por cantidad y el resultado lo sumo con la variable y despues lo guardo
            total_todo += p["precio"] * p["cantidad"]
        #sumo la cantidad de numero que hay en cantidad con la variable y despues lo guardo
            total_cantidad += p["cantidad"]
     print("total de todoo es: ",total_todo,  "\ncantidad total de productos registrados: ",total_cantidad)


#bucle de menu hasta que el usuario desee salir 

while active:
    print("""que desea hacer ?
    1. agregar producto
    2. mostrar inventario
    3. calcular estadisticas
    4. salir""")
    #validacion de datos
    try:
        opcion = int(input("ingrese el numero de la opcion que desea hacer: "))
        #condicion si el usuario desea salir se rompe
        if opcion == 4:
            active = False
        #condicion si elige agregar y luego llama la funcion y agrega en la lista
        elif opcion == 1:
            agregar_producto(inventario)
        #condicion si elige mostrar inventario llama la funcion y muetra la lista
        elif opcion == 2:
            mostrar_inventario(inventario)
           
        #condicion si elige calcular estadistica llama la funcion, calcula y muestra las estadisticas
        elif opcion == 3:
            calcular_estadistica(inventario)
        #si el usuario elige una opcion que no esta en el menu
        else:
            print("debes eligir un numero que este dentro de las opciones")
    #si los datos son invalidos muestra el mensaje y se repite el ciclo
    except:
        print("invalido intenta de nuevo, solo puedes ingresar el numero de la opcion")