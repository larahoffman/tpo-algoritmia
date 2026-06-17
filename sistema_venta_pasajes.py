# Sistema de Venta de Pasajes

# Datos
usuario_admin = "admin"
contrasenia_admin = "Admin2026!"

## Clientes
codigos_clientes = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110]
nombres_clientes = ["Ana Lopez", "Carlos Perez", "María Gomez", "Juan Rodriguez", "Lucía Fernandez", "Pedro Martinez", "Sofía Ramirez", "Diego Sanchez", "Valentina Torres", "Martín Diaz"]
edades_clientes = [25, 42, 31, 55, 19, 36, 28, 47, 22, 60]
tipos_clientes = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]   # 1 regular, 2 frecuente
## Destinos
codigos_destinos = [201, 202, 203, 204, 205, 206, 207, 208, 209, 210]
nombres_destinos = ["Cordoba", "Rosario", "Mendoza", "Bariloche", "Salta", "Ushuaia", "Mar del Plata", "Neuquen", "San Juan", "Tucuman"]
distancias_destinos = [700, 300, 1050, 1600, 1450, 3000, 415, 1150, 1100, 1250]
precios_destinos = [12000, 8000, 15000, 20000, 18000, 30000, 9000, 16000, 15500, 17000]
## Pasajes
codigos_pasajes = [301, 302, 303, 304, 305, 306, 307, 308, 309, 310]
codigos_cliente_pasajes = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110]
codigos_destino_pasajes = [201, 202, 203, 204, 205, 206, 207, 208, 209, 210]
cantidades_pasajes = [2, 1, 3, 2, 1, 4, 2, 1, 2, 3]
medios_pago_pasajes = [2, 1, 3, 2, 1, 3, 2, 1, 3, 2]  # 1 esfectivo, 2 tarjeta, 3 transferencia

#ORDENAR LISTAS

#CLIENTES--> selección
def ordenar_clientes_codigo():

    for i in range(len(codigos_clientes)-1):

        pos_menor = i

        for j in range(i+1, len(codigos_clientes)):

            if codigos_clientes[j] < codigos_clientes[pos_menor]:

                pos_menor = j

        codigos_clientes[i], codigos_clientes[pos_menor] = codigos_clientes[pos_menor], codigos_clientes[i]

        nombres_clientes[i], nombres_clientes[pos_menor] = nombres_clientes[pos_menor], nombres_clientes[i]

        edades_clientes[i], edades_clientes[pos_menor] = edades_clientes[pos_menor], edades_clientes[i]

        tipos_clientes[i], tipos_clientes[pos_menor] = tipos_clientes[pos_menor], tipos_clientes[i]
    

    print("Clientes ordenados por código.")



#DESTINOS--> Burbujeo
def ordenar_destinos_distancia():

    for i in range(len(distancias_destinos)-1):

        for j in range(len(distancias_destinos)-1-i):

            if distancias_destinos[j] > distancias_destinos[j+1]:

                distancias_destinos[j], distancias_destinos[j+1] = distancias_destinos[j+1], distancias_destinos[j]

                codigos_destinos[j], codigos_destinos[j+1] = codigos_destinos[j+1], codigos_destinos[j]

                nombres_destinos[j], nombres_destinos[j+1] = nombres_destinos[j+1], nombres_destinos[j]

                precios_destinos[j], precios_destinos[j+1] = precios_destinos[j+1], precios_destinos[j]

    print("Destinos ordenados por distancia.")


#PASAJES--> Insercion
def ordenar_pasajes_cantidad():

    for i in range(1, len(cantidades_pasajes)):

        cantidad_aux = cantidades_pasajes[i]
        codigo_aux = codigos_pasajes[i]
        cliente_aux = codigos_cliente_pasajes[i]
        destino_aux = codigos_destino_pasajes[i]
        pago_aux = medios_pago_pasajes[i]

        j = i - 1

        while j >= 0 and cantidades_pasajes[j] > cantidad_aux:

            cantidades_pasajes[j+1] = cantidades_pasajes[j]
            codigos_pasajes[j+1] = codigos_pasajes[j]
            codigos_cliente_pasajes[j+1] = codigos_cliente_pasajes[j]
            codigos_destino_pasajes[j+1] = codigos_destino_pasajes[j]
            medios_pago_pasajes[j+1] = medios_pago_pasajes[j]

            j -= 1

        cantidades_pasajes[j+1] = cantidad_aux
        codigos_pasajes[j+1] = codigo_aux
        codigos_cliente_pasajes[j+1] = cliente_aux
        codigos_destino_pasajes[j+1] = destino_aux
        medios_pago_pasajes[j+1] = pago_aux

    print("Pasajes ordenados por cantidad.")


# Funciones
  


     
      
       
        
         
          
           
            
             

def login(usuario, contrasenia):
    acceso = False
    intentos = 0
    while (usuario != usuario_admin or contrasenia != contrasenia_admin) and intentos < 3:
        print("Error! Usuario o contraseña incorrectos. Intente nuevamente.")
        usuario = input("Ingrese su usuario: ")
        contrasenia = input("Ingrese su contraseña: ")
        intentos += 1
    if usuario != usuario_admin or contrasenia != contrasenia_admin:
        print("Demasiados intentos fallidos. Saliendo del sistema.")
        return acceso
    else:
        acceso = True
    return acceso

# Función para validar que el número ingresado sea un entero mayor o igual a un mínimo establecido
def pedir_entero_minimo(mensaje, minimo):
    numero = int(input(mensaje))
    while numero < minimo:
        print("Error. Ingrese un numero mayor o igual a", minimo)
        numero = int(input(mensaje))
    return numero

# Busca si existe el codigo en la lista y en caso de que si, devuelve la posicion 
def buscar_codigo(lista_codigos, codigo): #BUSQUEDA SECUENCIAL
    pos = -1
    i = 0
    while i < len(lista_codigos) and pos == -1:
        if lista_codigos[i] == codigo:
            pos = i
        i = i + 1
    return pos

def buscar_codigo_cliente(codigo): #BUSQUEDA BINARIA

    izquierda = 0
    derecha = len(codigos_clientes) - 1

    while izquierda <= derecha:

        medio = (izquierda + derecha) // 2

        if codigos_clientes[medio] == codigo:
            return medio

        elif codigo < codigos_clientes[medio]:
            derecha = medio - 1

        else:
            izquierda = medio + 1

    return -1

def existe_codigo(lista_codigos, codigo):
    pos = buscar_codigo(lista_codigos, codigo)
    if pos == -1:
        return False
    else:
        return True
    

def es_entero(var_str):
    try:
        var_int = int(var_str)
        res = True
    except:
        res = False
    return res

def nombre_cliente_existente(nombre):
    for i in range(len(nombres_clientes)):
        if nombres_clientes[i].lower()==nombre.lower():
            return True
    return False



def agregar_cliente():
    print("--------------- Agregar un Cliente Nuevo ---------------")
     
    codigo_cliente_nuevo=int(input("Ingrese el código del cliente que desea agregar: "))
    while buscar_codigo(codigo_cliente_nuevo) !=-1:
        print ("ERROR! Ese código ya se encuentra registrado.")
        codigo_cliente_nuevo=int(input("Ingrese otro código: "))

    nombre_cliente_nuevo= input("Ingrese el nombre del cliente: ")
    while nombre_cliente_nuevo=="":
        print("ERROR! Nombre vacío o ya existente.")

        nombre_cliente_nuevo=input("Ingrese otro nombre: ")

    edad_cliente_nuevo=int(input("Ingrese la edad del cliente: "))
    while edad_cliente_nuevo <=0:
        print("ERROR! Edad inválida.")
        edad_cliente_nuevo=int(input("Ingrese la edad del cliente: "))

    edad_cliente_nuevo=int(input("Ingrese la edad del cliente: "))

    tipo_cliente_nuevo=int(input("Ingrese tipo (1=Regular/2=Frecuente): "))
    while tipo_cliente_nuevo !=1 and tipo_cliente_nuevo !=2:
        print("ERROR! Debe ingresar 1 o 2.")
        tipo_cliente_nuevo=int(input("Ingrese tipo (1=Regular/2=Frecuente): "))

    codigos_clientes.append(codigo_cliente_nuevo)
    nombres_clientes.append(nombre_cliente_nuevo)
    edades_clientes.append(edad_cliente_nuevo)
    tipos_clientes.append(tipo_cliente_nuevo)

    print("Cliente agregado correctamente.")


def modificar_cliente():
    print("------------------- Modificar Cliente ------------------")
    cliente_a_modificar = es_entero(input("Ingrese el codigo del cliente a modificar: "))# primero validamos que sea un código de tipo válido (número)
    existe_cliente = existe_codigo(codigos_clientes, cliente_a_modificar) # validamos que exista el cliente en nuestra lista
    if existe_cliente:
        posicion = buscar_codigo(codigos_clientes, cliente_a_modificar) # obtenemos la posicion del codigo de cliente existente
        print("Cliente", codigos_clientes[posicion])

        print("Nombre actual:", nombres_clientes[posicion])
        nombre_nuevo = input("Nuevo nombre: ")
        # Valida que no se ingrese un texto vacío
        while nombre_nuevo == "":
            print("ERROR! No puede ingresar un nombre vacío")
            nombre_nuevo = input("Nuevo nombre: ")
        nombres_clientes[posicion] = nombre_nuevo

        print("Edad actual:", edades_clientes[posicion])
        edad_nueva = es_entero(input("Nueva edad: "))
        # Valida que se ingrese una edad positiva
        while edad_nueva <= 0:
            print("ERROR! Edad inválida")
            edad_nueva = es_entero(input("Nueva edad: "))
        edades_clientes[posicion] = edad_nueva
        
        print("Tipo de cliente:", tipos_clientes[posicion])
        tipo_cliente_nuevo = es_entero(input("Nuevo tipo de cliente (1=Regular/2=Frecuente): "))
        # Valida que se ingrese un tipo de cliente valido (1 o 2)
        while tipo_cliente_nuevo != 1 or tipo_cliente_nuevo != 2:
            print("ERROR! Debe ingresar 1 o 2.")
            tipo_cliente_nuevo = es_entero(input("Nuevo tipo de cliente (1=Regular/2=Frecuente): "))
        tipos_clientes[posicion] = tipo_cliente_nuevo
    else:
        print("No existe el cliente ingresado")


def eliminar_cliente():

    print("------------------- Eliminar Cliente ------------------")

    codigo = pedir_entero_minimo("Ingrese el código del cliente a eliminar: ", 1)

    posicion_cliente = buscar_codigo(codigos_clientes, codigo)

    if posicion_cliente != -1:

        # Verificar si tiene pasajes asociados
        tiene_pasajes = False

        for i in range(len(codigos_cliente_pasajes)):
            if codigos_cliente_pasajes[i] == codigo:
                tiene_pasajes = True

        if tiene_pasajes:
            print("ERROR! No se puede eliminar el cliente porque tiene pasajes asociados.")

        else:
            # Eliminar de todas las listas paralelas
            codigos_clientes.pop(posicion_cliente)
            nombres_clientes.pop(posicion_cliente)
            edades_clientes.pop(posicion_cliente)
            tipos_clientes.pop(posicion_cliente)

            print("Cliente eliminado correctamente.")

    else:
        print("ERROR! No existe un cliente con ese código.")

def listar_clientes():

    ordenar_clientes_codigo()

    print("\n--------------- LISTADO DE CLIENTES ---------------")

    for i in range(len(codigos_clientes)):

        print("----------------------------------------")
        print("Código:", codigos_clientes[i])
        print("Nombre:", nombres_clientes[i])
        print("Edad:", edades_clientes[i])

        if tipos_clientes[i] == 1:
            print("Tipo: Regular")
        else:
            print("Tipo: Frecuente")

    print("----------------------------------------")

def estadistica_destino_pago():
    matriz = []

    # Crear una fila por cada destino
    for i in range(len(codigos_destinos)):
        matriz.append([0, 0, 0])

    # Cargar los datos en la matriz
    for i in range(len(codigos_pasajes)):
        codigo_destino = codigos_destino_pasajes[i]
        cantidad = cantidades_pasajes[i]
        medio_pago = medios_pago_pasajes[i]

        posicion_destino = buscar_codigo(
            codigos_destinos,
            codigo_destino
        )

        if posicion_destino != -1 and medio_pago >= 1 and medio_pago <= 3:
            matriz[posicion_destino][medio_pago - 1] += cantidad

    # Mostrar la matriz
    print("\nCantidad de pasajes vendidos por destino y medio de pago")
    print("----------------------------------------------------------")
    print("Destino\t\tEfectivo\tTarjeta\t\tTransferencia")

    for i in range(len(matriz)):
        print(
            nombres_destinos[i], "\t\t",
            matriz[i][0], "\t\t",
            matriz[i][1], "\t\t",
            matriz[i][2]
        )

def estadistica_tipo_cliente():

    cantidad_regulares = 0
    cantidad_frecuentes = 0

    for i in range(len(codigos_pasajes)):

        codigo_cliente = codigos_cliente_pasajes[i]
        cantidad = cantidades_pasajes[i]

        posicion_cliente = buscar_codigo(codigos_clientes, codigo_cliente)

        if posicion_cliente != -1:

            tipo_cliente = tipos_clientes[posicion_cliente]

            if tipo_cliente == 1:
                cantidad_regulares += cantidad

            elif tipo_cliente == 2:
                cantidad_frecuentes += cantidad

    print("\nCantidad de pasajes por tipo de cliente")
    print("----------------------------------------")
    print("Clientes regulares:", cantidad_regulares)
    print("Clientes frecuentes:", cantidad_frecuentes) 

def estadistica_pasajes_destino():

    total_pasajes_destino = []

    # inicializar en 0
    for i in range(len(codigos_destinos)):
        total_pasajes_destino.append(0)

    # recorrer pasajes
    for i in range(len(codigos_pasajes)):

        codigo_destino = codigos_destino_pasajes[i]
        cantidad = cantidades_pasajes[i]

        posicion_destino = buscar_codigo(codigos_destinos, codigo_destino)

        if posicion_destino != -1:
            total_pasajes_destino[posicion_destino] += cantidad

    print("\nCantidad de pasajes vendidos por destino")
    print("-----------------------------------------")

    for i in range(len(codigos_destinos)):

        print("Destino:", nombres_destinos[i])
        print("Cantidad de pasajes vendidos:", total_pasajes_destino[i])
        print("----------------------------------")

def estadistica_medio_pago():

    cantidad_pago = [0, 0, 0]

    for i in range(len(codigos_pasajes)):

        medio_pago = medios_pago_pasajes[i]

        cantidad_pago[medio_pago - 1] += 1

    print("\nCantidad de pasajes vendidos por medio de pago")
    print("---------------------------------------------")
    print("Efectivo:", cantidad_pago[0])
    print("Tarjeta:", cantidad_pago[1])
    print("Transferencia:", cantidad_pago[2])
    print("----------------------------------")

def agregar_destino():

    print("--------------- Agregar un Destino Nuevo ---------------")

    codigo_destino_nuevo = pedir_entero_minimo(
        "Ingrese el código del destino: ", 1
    )

    while buscar_codigo(codigos_destinos, codigo_destino_nuevo) != -1:
        print("ERROR! Ese código ya existe.")
        codigo_destino_nuevo = pedir_entero_minimo(
            "Ingrese otro código: ", 1
        )

    nombre_destino_nuevo = input("Ingrese nombre del destino: ")

    while nombre_destino_nuevo == "":
        print("ERROR! Nombre vacío.")
        nombre_destino_nuevo = input("Ingrese otro nombre: ")

    distancia_destino_nuevo = pedir_entero_minimo(
        "Ingrese distancia (km): ", 1
    )

    precio_destino_nuevo = pedir_entero_minimo(
        "Ingrese precio base: ", 1
    )

    codigos_destinos.append(codigo_destino_nuevo)
    nombres_destinos.append(nombre_destino_nuevo)
    distancias_destinos.append(distancia_destino_nuevo)
    precios_destinos.append(precio_destino_nuevo)

    print("Destino agregado correctamente.")

def eliminar_destino():

    print("------------------- Eliminar Destino ------------------")

    codigo = pedir_entero_minimo(
        "Ingrese código del destino a eliminar: ", 1
    )

    posicion_destino = buscar_codigo(codigos_destinos, codigo)

    if posicion_destino != -1:

        tiene_pasajes = False

        for i in range(len(codigos_destino_pasajes)):
            if codigos_destino_pasajes[i] == codigo:
                tiene_pasajes = True

        if tiene_pasajes:
            print("ERROR! No se puede eliminar porque tiene pasajes asociados.")

        else:
            codigos_destinos.pop(posicion_destino)
            nombres_destinos.pop(posicion_destino)
            distancias_destinos.pop(posicion_destino)
            precios_destinos.pop(posicion_destino)

            print("Destino eliminado correctamente.")

    else:
        print("ERROR! No existe un destino con ese código.")

def estadistica_pasaje_destino():

    cantidad_pasajes_destino = []

    # Inicializar lista en 0
    for i in range(len(codigos_destinos)):
        cantidad_pasajes_destino.append(0)

    # Recorrer todos los pasajes
    for i in range(len(codigos_pasajes)):

        codigo_destino = codigos_destino_pasajes[i]
        cantidad = cantidades_pasajes[i]

        posicion_destino = buscar_codigo(codigos_destinos, codigo_destino)

        if posicion_destino != -1:
            cantidad_pasajes_destino[posicion_destino] += cantidad

    print("\nCantidad de pasajes vendidos por destino")
    print("-----------------------------------------")

    for i in range(len(codigos_destinos)):

        print("Destino:", nombres_destinos[i])
        print("Cantidad de pasajes vendidos:", cantidad_pasajes_destino[i])
        print("----------------------------------")

def modificar_destino():

    print("------------------- Modificar Destino ------------------")

    codigo = pedir_entero_minimo(
        "Ingrese código del destino a modificar: ", 1
    )

    posicion = buscar_codigo(codigos_destinos, codigo)

    if posicion != -1:

        print("Nombre actual:", nombres_destinos[posicion])
        nuevo_nombre = input("Nuevo nombre: ")

        while nuevo_nombre == "":
            print("ERROR! Nombre vacío.")
            nuevo_nombre = input("Nuevo nombre: ")

        print("Distancia actual:", distancias_destinos[posicion])
        nueva_distancia = pedir_entero_minimo(
            "Nueva distancia: ", 1
        )

        print("Precio actual:", precios_destinos[posicion])
        nuevo_precio = pedir_entero_minimo(
            "Nuevo precio: ", 1
        )

        nombres_destinos[posicion] = nuevo_nombre
        distancias_destinos[posicion] = nueva_distancia
        precios_destinos[posicion] = nuevo_precio

        print("Destino modificado correctamente.")

    else:
        print("ERROR! No existe ese destino.")

def listar_destinos():

    ordenar_destinos_distancia()

    print("\n--------------- LISTADO DE DESTINOS ---------------")

    for i in range(len(codigos_destinos)):

        print("----------------------------------------")
        print("Código:", codigos_destinos[i])
        print("Nombre:", nombres_destinos[i])
        print("Distancia:", distancias_destinos[i], "km")
        print("Precio base:", precios_destinos[i], "ARS")

def agregar_pasaje():
    print("--------------- Agregar un Pasaje Nuevo ---------------")
    codigo_pasaje_nuevo=int(input("Ingrese el código del pasaje que desea agregar: "))
                        
    while buscar_codigo(codigos_pasajes, codigo_pasaje_nuevo) !=-1:
        print ("ERROR! Ese código ya se encuentra registrado.")
    codigo_pasaje_nuevo=int(input("Ingrese otro código: "))
    codigo_cliente_pasaje_nuevo=int(input("Ingrese el código del cliente para este pasaje: "))
    
    while buscar_codigo(codigos_clientes, codigo_cliente_pasaje_nuevo) ==-1:
        print ("ERROR! No existe un cliente con ese código.")
    codigo_cliente_pasaje_nuevo=int(input("Ingrese otro código de cliente: "))
    codigo_destino_pasaje_nuevo=int(input("Ingrese el código del destino para este pasaje: "))
                        
    while buscar_codigo(codigos_destinos, codigo_destino_pasaje_nuevo) ==-1:
        print ("ERROR! No existe un destino con ese código.")        
    codigo_destino_pasaje_nuevo=int(input("Ingrese otro código de destino: "))
    cantidad_pasaje_nuevo=int(input("Ingrese la cantidad de pasajes a comprar: "))
                        
    while cantidad_pasaje_nuevo <=0:
        print("ERROR! Cantidad inválida.")
    cantidad_pasaje_nuevo=int(input("Ingrese la cantidad de pasajes a comprar: "))
    medio_pago_pasaje_nuevo=int(input("Ingrese el medio de pago (1=Efectivo/2=Tarjeta/3=Transferencia): "))
                        
    while medio_pago_pasaje_nuevo !=1 and medio_pago_pasaje_nuevo !=2 and medio_pago_pasaje_nuevo !=3:
        print("ERROR! Debe ingresar 1, 2 o 3.")
    medio_pago_pasaje_nuevo=int(input("Ingrese el medio de pago (1=Efectivo/2=Tarjeta/3=Transferencia): "))
    codigos_pasajes.append(codigo_pasaje_nuevo)
    codigos_cliente_pasajes.append(codigo_cliente_pasaje_nuevo)
    codigos_destino_pasajes.append(codigo_destino_pasaje_nuevo)
    cantidades_pasajes.append(cantidad_pasaje_nuevo)
    medios_pago_pasajes.append(medio_pago_pasaje_nuevo)
    print("Pasaje agregado correctamente.")

def eliminar_pasaje():
    print("------------------- Eliminar Pasaje ------------------")
    pasaje_a_eliminar = int(input("Ingrese el código del pasaje a eliminar: "))
    codigo = pedir_entero_minimo("Código de pasaje a eliminar: ", 1)
    posicion_pasaje = buscar_codigo(pasaje_a_eliminar, codigo)
                        
    if posicion_pasaje != -1:
    # Eliminar pasaje de las listas
        codigos_pasajes.pop(posicion_pasaje)
        codigos_cliente_pasajes.pop(posicion_pasaje)
        codigos_destino_pasajes.pop(posicion_pasaje)
        cantidades_pasajes.pop(posicion_pasaje)
        medios_pago_pasajes.pop(posicion_pasaje)
        print("Pasaje eliminado exitosamente.")
                        
    elif posicion_pasaje == -1: 
        print("Error. No existe un pasaje con ese código.")
    else:
        print("Error. Ingrese un número válido.")

def modificar_pasaje():
    print("------------------- Modificar Pasaje ------------------")
    pasaje_a_modificar = es_entero(input("Ingrese el codigo del pasaje a modificar: "))# primero validamos que sea un código de tipo válido (número)
    existe_pasaje = existe_codigo(codigos_pasajes, pasaje_a_modificar) # validamos que exista el pasaje en nuestra lista
    if existe_pasaje:
        posicion = buscar_codigo(codigos_pasajes, pasaje_a_modificar) # obtenemos la posicion del codigo de pasaje existente
        print("Pasaje", codigos_pasajes[posicion])
        # Validar que no ingresen un texto vacío
        print("Código cliente actual:", codigos_cliente_pasajes[posicion])
        codigos_cliente_pasajes[posicion] = es_entero(input("Nuevo código cliente: "))
        print("Código destino actual:", codigos_destino_pasajes[posicion])
        codigos_destino_pasajes[posicion] = es_entero(input("Nuevo código destino: "))
        print("Cantidad actual:", cantidades_pasajes[posicion])
        cantidades_pasajes[posicion] = es_entero(input("Nueva cantidad: "))
        print("Medio de pago actual:", medios_pago_pasajes[posicion])
        medios_pago_pasajes[posicion] = es_entero(input("Nuevo medio de pago: "))
    else:
        print("No existe el pasaje ingresado")

def listar_pasajes():
    ordenar_pasajes_cantidad()
    print("\n--------------- LISTADO DE PASAJES ---------------")
    for i in range(len(codigos_pasajes)):
        print("----------------------------------------")
        print("Código:", codigos_pasajes[i])
        print("Código cliente:", codigos_cliente_pasajes[i])
        print("Código destino:", codigos_destino_pasajes[i])
        print("Cantidad:", cantidades_pasajes[i])
    
    if medios_pago_pasajes[i] == 1:
        print("Medio de pago: Efectivo")
    
    elif medios_pago_pasajes[i] == 2:
        print("Medio de pago: Tarjeta")
    elif medios_pago_pasajes[i] == 3:
        print("Medio de pago: Transferencia")
        print("----------------------------------------")
                            
def buscar_cliente_menu():
    print("------------------- Buscar Cliente ------------------")
    codigo_a_buscar = int(input("Ingrese el código del cliente a buscar: "))
    posicion_cliente = calculo_binario_cliente(codigo_a_buscar)

    if posicion_cliente != -1:
        print("Cliente encontrado:")
        print("------------------------")
        print("Código:", codigos_clientes[posicion_cliente])
        print("Nombre:", nombres_clientes[posicion_cliente])
        print("Edad:", edades_clientes[posicion_cliente])
        if tipos_clientes[posicion_cliente] == 1:
            print("Tipo: Regular")
        else:
            print("Tipo: Frecuente")
        print("------------------------")
    else:
        print("No se encontró un cliente con ese código.")

def calculo_binario_cliente(codigo_a_buscar):
    izquierda = 0
    derecha = len(codigos_clientes) - 1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        
        if codigos_clientes[medio] == codigo_a_buscar:
            return medio
        elif codigo_a_buscar < codigos_clientes[medio]:
            derecha = medio - 1
        else:
            izquierda = medio + 1
    return -1
    
def buscar_destino_menu():
    print("------------------- Buscar Destino ------------------")
    print("1. Buscar por código")
    print("2. Buscar por nombre")
    print("3. Volver al menú principal")
    print("---------------------------------")
    
    opcion_busqueda = int(input("Seleccione una opción de búsqueda: "))

    if opcion_busqueda == 1:
        codigo_a_buscar = int(input("Ingrese el código del destino a buscar: "))
        posicion_destino = buscar_codigo(codigos_destinos, codigo_a_buscar)

        if posicion_destino != -1:
            mostrar_datos_destino(posicion)
        else:
            print("No se encontró un destino con ese código.")
        
    elif opcion_busqueda == 2:
        nombre_a_buscar = input("Ingrese el nombre del destino a buscar: ")
        encontrado = False

        for i in range(len(nombres_destinos)):
            if nombres_destinos[i].lower() == nombre_a_buscar.lower():
                mostrar_datos_destino(i)
                encontrado = True

        if not encontrado:
            print("No se encontró un destino con ese nombre.")

    else:
        print("Opción inválida")

def mostrar_datos_destino(posicion):
    print("\n[ Destino Encontrado ]")
    print("----------------------------------------")
    print("Código:", codigos_destinos[posicion])
    print("Nombre:", nombres_destinos[posicion])
    print("Distancia:", distancias_destinos[posicion], "km")
    print("Precio base: $", precios_destinos[posicion])
    print("----------------------------------------")


def buscar_pasaje_menu():
    print("------------------- Buscar Pasaje ------------------")
    codigo_a_buscar = int(input("Ingrese el código del pasaje a buscar: "))
    posicion_pasaje = buscar_codigo(codigos_pasajes, codigo_a_buscar) #busqueda secuencial

    if posicion_pasaje != -1:
        print("Pasaje encontrado:")
        print("------------------------")
        print("Código:", codigos_pasajes[posicion_pasaje])
        print("Cliente:", nombres_clientes[buscar_codigo(codigos_clientes, codigos_cliente_pasajes[posicion_pasaje])])
        print("Código cliente:", codigos_cliente_pasajes[posicion_pasaje])
        print("Código destino:", codigos_destino_pasajes[posicion_pasaje])
        print("Cantidad:", cantidades_pasajes[posicion_pasaje])
        if medios_pago_pasajes[posicion_pasaje] == 1:
            print("Medio de pago: Efectivo")
        elif medios_pago_pasajes[posicion_pasaje] == 2:
            print("Medio de pago: Tarjeta")
        elif medios_pago_pasajes[posicion_pasaje] == 3:
            print("Medio de pago: Transferencia")
        print("------------------------")
    else:
        print("No se encontró un pasaje con ese código.")

    
    
    
#PASAJES

def agregar_pasaje():

    print("--------------- Agregar Pasaje ---------------")

    codigo_pasaje_nuevo = int(input("Ingrese código del pasaje: "))

    while buscar_codigo(codigos_pasajes, codigo_pasaje_nuevo) != -1:
        print("ERROR! Ese código ya existe.")
        codigo_pasaje_nuevo = int(input("Ingrese otro código: "))

    codigo_cliente = int(input("Ingrese código del cliente: "))

    while buscar_codigo(codigos_clientes, codigo_cliente) == -1:
        print("ERROR! Cliente inexistente.")
        codigo_cliente = int(input("Ingrese otro código de cliente: "))

    codigo_destino = int(input("Ingrese código del destino: "))

    while buscar_codigo(codigos_destinos, codigo_destino) == -1:
        print("ERROR! Destino inexistente.")
        codigo_destino = int(input("Ingrese otro código de destino: "))

    cantidad = int(input("Ingrese cantidad de pasajes: "))

    while cantidad <= 0:
        print("ERROR! Cantidad inválida.")
        cantidad = int(input("Ingrese cantidad de pasajes: "))

    medio_pago = int(input("Ingrese medio de pago (1=Efectivo / 2=Tarjeta / 3=Transferencia): "))

    while medio_pago < 1 or medio_pago > 3:
        print("ERROR! Medio de pago inválido.")
        medio_pago = int(input("Ingrese medio de pago (1/2/3): "))

    codigos_pasajes.append(codigo_pasaje_nuevo)
    codigos_cliente_pasajes.append(codigo_cliente)
    codigos_destino_pasajes.append(codigo_destino)
    cantidades_pasajes.append(cantidad)
    medios_pago_pasajes.append(medio_pago)

    print("Pasaje agregado correctamente.")

def eliminar_pasaje():

    print("--------------- Eliminar Pasaje ---------------")

    codigo = int(input("Ingrese código del pasaje a eliminar: "))

    posicion = buscar_codigo(codigos_pasajes, codigo)

    if posicion != -1:

        codigos_pasajes.pop(posicion)
        codigos_cliente_pasajes.pop(posicion)
        codigos_destino_pasajes.pop(posicion)
        cantidades_pasajes.pop(posicion)
        medios_pago_pasajes.pop(posicion)

        print("Pasaje eliminado correctamente.")

    else:
        print("ERROR! Pasaje no encontrado.")

def modificar_pasaje():

    print("--------------- Modificar Pasaje ---------------")

    codigo = int(input("Ingrese código del pasaje: "))

    posicion = buscar_codigo(codigos_pasajes, codigo)

    if posicion != -1:

        nueva_cantidad = int(input("Ingrese nueva cantidad de pasajes: "))

        while nueva_cantidad <= 0:
            print("ERROR! Cantidad inválida.")
            nueva_cantidad = int(input("Ingrese nueva cantidad: "))

        nuevo_medio = int(input("Ingrese nuevo medio de pago (1/2/3): "))

        while nuevo_medio < 1 or nuevo_medio > 3:
            print("ERROR! Medio inválido.")
            nuevo_medio = int(input("Ingrese nuevo medio de pago: "))

        cantidades_pasajes[posicion] = nueva_cantidad
        medios_pago_pasajes[posicion] = nuevo_medio

        print("Pasaje modificado correctamente.")

    else:
        print("ERROR! Pasaje no encontrado.")

def listar_pasajes():

    print("\n--------------- LISTADO DE PASAJES ---------------")

    for i in range(len(codigos_pasajes)):

        posicion_cliente = buscar_codigo(codigos_clientes, codigos_cliente_pasajes[i])
        posicion_destino = buscar_codigo(codigos_destinos, codigos_destino_pasajes[i])

        print("----------------------------------")
        print("Código de pasaje:", codigos_pasajes[i])

        if posicion_cliente != -1:
            print("Cliente:", nombres_clientes[posicion_cliente])

        if posicion_destino != -1:
            print("Destino:", nombres_destinos[posicion_destino])

        print("Cantidad:", cantidades_pasajes[i])

        if medios_pago_pasajes[i] == 1:
            print("Medio de pago: Efectivo")

        elif medios_pago_pasajes[i] == 2:
            print("Medio de pago: Tarjeta")

        else:
            print("Medio de pago: Transferencia")





#LOGIN    

print("--------------- Sistema de Venta de Pasajes ---------------")
print("--------------------- Inicio de sesión --------------------")

user = input("Ingrese su usuario: ")
password = input("Ingrese su contraseña: ")

#MENÚ
if login(user, password):
    print("--------------- Sistema de Venta de Pasajes ---------------")
    print("Bienvenido,", usuario_admin)
    opcion_menu = 0
    opcion_menu_clientes = 0
    print('''
        ---------------------------------
        |    Menú principal             |
        |    1. Gestión de clientes     |
        |    2. Gestión de destinos     |
        |    3. Gestión de pasajes      |
        |    4. Búsqueda                |
        |    5. Estadística             |
        |    6. Salir                   |
        ---------------------------------
            '''
        )
    opcion_menu = es_entero(input("Seleccione una opción: "))
    while opcion_menu != 6:
        if opcion_menu == 1:
            print('''
                -------------------------------------
                |    Gestión de clientes            |
                |    1. Agregar cliente             |
                |    2. Eliminar cliente            |
                |    3. Modificar datos cliente     |
                |    4. Ver listado clientes        |
                |    5. Volver al menú principal    |
                -------------------------------------
                '''
                )

            opcion_menu_clientes= es_entero(input("Seleccione una opción: "))
            while opcion_menu_clientes != 5:
                if opcion_menu_clientes == 1:
                    agregar_cliente()
                elif opcion_menu_clientes == 2:
                    eliminar_cliente()
                elif opcion_menu_clientes == 3:
                    modificar_cliente()    
                elif opcion_menu_clientes == 4:
                    listar_clientes()
                else:
                    print("Opción inválida")
                    opcion_menu_clientes= es_entero(input("Seleccione una opción: "))
            # aca falta volver a llamar al menu
                
        # DESTINOS
        elif opcion_menu == 2:

            opcion_destinos = 0

            while opcion_destinos != 5:

                print('''
                -------------------------------------
                |      Gestión de Destinos          |
                | 1. Agregar destino                |
                | 2. Eliminar destino               |
                | 3. Modificar destino              |
                | 4. Listar destinos                |
                | 5. Volver al menú principal       |
                -------------------------------------
                ''')

                opcion_destinos = int(input("Seleccione una opción: "))

                if opcion_destinos == 1:
                    agregar_destino()

                elif opcion_destinos == 2:
                    eliminar_destino()

                elif opcion_destinos == 3:
                    modificar_destino()

                elif opcion_destinos == 4:
                    listar_destinos()
                
                else:
                        print ("Opción inválida")
                        opcion_menu_clientes= int(input("Seleccione una opción: "))
                

        # PASAJES
        elif opcion_menu == 3:

            opcion_pasajes = 0

            while opcion_pasajes != 5:

                print('''
                -------------------------------------
                |      Gestión de Pasajes           |
                | 1. Agregar pasaje                 |
                | 2. Eliminar pasaje                |
                | 3. Modificar pasaje               |
                | 4. Listar pasajes                 |
                | 5. Volver al menú principal       |
                -------------------------------------
                ''')

                opcion_pasajes = int(input("Seleccione una opción: "))

                if opcion_pasajes == 1:
                    agregar_pasaje()

                elif opcion_pasajes == 2:
                    eliminar_pasaje()

                elif opcion_pasajes == 3:
                    modificar_pasaje()

                elif opcion_pasajes == 4:
                    listar_pasajes()
        
                else:
                    print ("Opción inválida")
                    opcion_menu_clientes= int(input("Seleccione una opción: "))

        # BUSQUEDAS
        elif opcion_menu == 4:

            opcion_busquedas = 0

            while opcion_busquedas != 4:

                print('''
                -------------------------------------
                |           Búsquedas               |
                | 1. Buscar cliente                 |
                | 2. Buscar destino                 |
                | 3. Buscar pasaje                  |
                | 4. Volver al menú principal       |
                -------------------------------------
                ''')

                opcion_busquedas = int(input("Seleccione una opción: "))

                if opcion_busquedas == 1:
                    buscar_cliente_menu()

                elif opcion_busquedas == 2:
                    buscar_destino_menu()

                elif opcion_busquedas == 3:
                    buscar_pasaje_menu()

                else:
                    print ("Opción inválida")
                    opcion_menu_clientes= int(input("Seleccione una opción: "))


        # ESTADISTICAS
        elif opcion_menu == 5:
            opcion_estadisticas = 0

            while opcion_estadisticas != 2:

                    print('''
                    -----------------------------
                    |      Estadísticas           |
                    | 1. Ver estadística          |
                    | 2. Volver al menú principal |
                    -----------------------------
                    ''')

                    opcion_estadisticas = int(input("Seleccione una opción: "))

                    if opcion_estadisticas == 1:
                        estadistica_destino_pago()
                
                    elif opcion_estadisticas == 2: 
                        estadistica_tipo_cliente()
                        
                    elif opcion_estadisticas == 3:
                        estadistica_pasaje_destino()
                        
                    elif opcion_estadisticas == 4:
                        estadistica_medio_pago() 

                    else:
                        print ("Opción inválida")
                        opcion_menu_clientes= int(input("Seleccione una opción: "))
            else:
                print()
                opcion_menu = es_entero(input("Seleccione una opción: "))
            #SALIDA
        if opcion_menu == 6:
            print("\nGracias por utilizar el sistema.")
            print("Cerrando programa...")
            print("Programa finalizado.")