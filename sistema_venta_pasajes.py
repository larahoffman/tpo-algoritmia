# Sistema de Venta de Pasajes
import random
# Variables globales
usuario_admin = "admin"
contrasenia_admin = "Admin2026!"
cantidad_registros = 10000 # puede ser modificado en un futuro
## Clientes
codigos_clientes = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110]
nombres_clientes = ["Ana Lopez", "Carlos Perez", "María Gomez", "Juan Rodriguez", "Lucía Fernandez", "Pedro Martinez", "Sofía Ramirez", "Diego Sanchez", "Valentina Torres", "Martín Diaz"]
edades_clientes = [25, 42, 31, 55, 19, 36, 28, 47, 22, 60]
tipos_clientes = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]   # 1 regular, 2 frecuente
## Destinos
codigos_destinos = [201, 202, 203, 204, 205, 206, 207, 208, 209, 210]
nombres_destinos = ["Cordoba", "Rosario", "Mendoza", "Bariloche", "Salta", "Ushuaia", "Mar del Plata", "Neuquen", "San Juan", "Tucuman"]
distancias_destinos = [700.0, 300.0, 1050.0, 1600.0, 1450.0, 3000.0, 415.0, 1150.0, 1100.0, 1250.0]
precios_destinos = [12000, 8000, 15000, 20000, 18000, 30000, 9000, 16000, 15500, 17000]
## Pasajes
codigos_pasajes = [301, 302, 303, 304, 305, 306, 307, 308, 309, 310]
codigos_cliente_pasajes = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110]
codigos_destino_pasajes = [201, 202, 203, 204, 205, 206, 207, 208, 209, 210]
cantidades_pasajes = [2, 1, 3, 2, 1, 4, 2, 1, 2, 3]
medios_pago_pasajes = [2, 1, 3, 2, 1, 3, 2, 1, 3, 2]  # 1 efectivo, 2 tarjeta, 3 transferencia

# Funciones

## Auxiliares
def es_entero(var_str):
    try:
        var_int = int(var_str)
        res = True
    except:
        res = False
    return res

def es_flotante(var_str):
    try:
        var_float = float(var_str)
        res = True
    except:
        res = False
    return res

# Busca si existe el codigo en la lista y en caso de que si, devuelve la posicion y, sino, deuvelve -1
def buscar_codigo(lista_codigos, codigo): #BUSQUEDA SECUENCIAL
    pos = -1
    i = 0
    while i < len(lista_codigos) and pos == -1:
        if lista_codigos[i] == codigo:
            pos = i
        i = i + 1
    return pos

def pedir_entero_minimo(mensaje, minimo):
    valido = False
    while not valido:
        dato = input(mensaje)
        if not es_entero(dato):
            print("ERROR! Debe ingresar un número entero.")
        else:
            numero = int(dato)
            if numero < minimo:
                print("Error. Ingrese un numero mayor o igual a", minimo)
            else:
                valido = True
    return numero

def pedir_flotante_minimo(mensaje, minimo):
    valido = False
    while not valido:
        dato = input(mensaje)
        if not es_flotante(dato):
            print("ERROR! debe ingresar un número decimal")
        else:
            numero = float(dato)
            if numero < minimo:
                print("Error. Ingrese un numero mayor o igual a", minimo)
            else:
                valido = True
    return numero
    
def pedir_entero(mensaje, minimo, maximo):
    valido = False
    while not valido:
        dato = input(mensaje)
        if not es_entero(dato):
            print("ERROR! Debe ingresar un número entero.")
        else:
            numero = int(dato)
            if numero < minimo or numero > maximo:
                print("Error. Ingrese un numero entre", minimo, "y", maximo)
            else:
                valido = True
    return numero

## Inicio de sesión
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

## Menús
def menu_principal():
    opcion_menu = 0
    while opcion_menu != 6:
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
        ''')
        opcion_menu = pedir_entero("Seleccione una opción: ", 1, 6)
        if opcion_menu == 1:
            menu_clientes()
        elif opcion_menu == 2:
            menu_destinos()
        elif opcion_menu == 3:
            menu_pasajes()
        elif opcion_menu == 4:
            menu_busquedas()
        elif opcion_menu == 5:
            menu_estadisticas()
        elif opcion_menu == 6:
            print("\nGracias por utilizar el sistema.")
            print("Cerrando programa...")
            print("Programa finalizado.")

def volver_menu():
    print("\nVolviendo al menú principal...")

def menu_clientes():
    opcion_menu_clientes = 0
    while opcion_menu_clientes != 5:
        print('''
        -------------------------------------
        |    Gestión de clientes            |
        |    1. Agregar cliente             |
        |    2. Eliminar cliente            |
        |    3. Modificar datos cliente     |
        |    4. Ver listado clientes        |
        |    5. Volver al menú principal    |
        -------------------------------------
        ''')
        opcion_menu_clientes= pedir_entero("Seleccione una opción: ", 1, 5)
        if opcion_menu_clientes == 1:
            agregar_cliente()
        elif opcion_menu_clientes == 2:
            eliminar_cliente()
        elif opcion_menu_clientes == 3:
            modificar_cliente()    
        elif opcion_menu_clientes == 4:
            listar_clientes()
        elif opcion_menu_clientes == 5:
            volver_menu()

def menu_destinos():
    opcion_destinos = 0

    while opcion_destinos != 5:
        print('''
        -------------------------------------
        |    Gestión de destinos            |
        |    1. Agregar destino             |
        |    2. Eliminar destino            |
        |    3. Modificar datos destino     |
        |    4. Ver listado destinos        |
        |    5. Volver al menú principal    |
        -------------------------------------
        ''' )

        opcion_destinos = pedir_entero("Seleccione una opción: ", 1, 5)

        if opcion_destinos == 1:
            agregar_destino()
        elif opcion_destinos == 2:
            eliminar_destino()
        elif opcion_destinos == 3:
            modificar_destino()
        elif opcion_destinos == 4:
            listar_destinos()
        elif opcion_destinos == 5:
            volver_menu()

def menu_pasajes():
    opcion_pasajes = 0

    while opcion_pasajes != 5:

        print('''
        ----------------------------------------
        |         Gestión de Pasajes           |
        |    1. Agregar pasaje                 |
        |    2. Eliminar pasaje                |
        |    3. Modificar pasaje               |
        |    4. Listar pasajes                 |
        |    5. Volver al menú principal       |
        ----------------------------------------
        ''')

        opcion_pasajes = pedir_entero("Seleccione una opción: ", 1, 5)

        if opcion_pasajes == 1:
            agregar_pasaje()
        elif opcion_pasajes == 2:
            eliminar_pasaje()
        elif opcion_pasajes == 3:
            modificar_pasaje()
        elif opcion_pasajes == 4:
            listar_pasajes()
        elif opcion_pasajes == 5:
            volver_menu()

def menu_busquedas():
    opcion_busquedas = 0

    while opcion_busquedas != 4:
        print('''
        ----------------------------------------
        |           Búsquedas                  |
        |    1. Buscar cliente                 |
        |    2. Buscar destino                 |
        |    3. Buscar pasaje                  |
        |    4. Volver al menú principal       |
        ----------------------------------------
        ''')
        opcion_busquedas = pedir_entero("Seleccione una opción: ", 1, 4)

        if opcion_busquedas == 1:
            buscar_cliente_menu()
        elif opcion_busquedas == 2:
            buscar_destino_menu()
        elif opcion_busquedas == 3:
            buscar_pasaje_menu()
        elif opcion_busquedas == 4:
            volver_menu()

def menu_estadisticas():
    opcion_estadisticas = 0

    while opcion_estadisticas != 5:

        print('''
        -------------------------------------------
        |           Estadísticas                  |
        | 1. Pasajes por destino y medio de pago  |
        | 2. Pasajes por tipo de cliente          |
        | 3. Total Pasajes por destino            |
        | 4. Distribución ventas por medio de pago|
        | 5. Volver al menú principal             |
        -------------------------------------------
        ''')

        opcion_estadisticas = pedir_entero("Seleccione una opción: ", 1, 5)

        if opcion_estadisticas == 1:
            estadistica_destino_pago()  
        elif opcion_estadisticas == 2: 
            estadistica_tipo_cliente()        
        elif opcion_estadisticas == 3:
            estadistica_pasaje_destino()        
        elif opcion_estadisticas == 4:
            estadistica_ventas_medio_pago()
        elif opcion_estadisticas == 5:
            volver_menu()


## CRUD Clientes
def agregar_cliente():
    print("--------------- Agregar un Cliente Nuevo ---------------")
    nombre_cliente_nuevo = input("Ingrese el nombre del cliente: ")
    # Valida que no ingresen un nombre vacío
    while nombre_cliente_nuevo == "":
        print("ERROR! Nombre vacío.")
        nombre_cliente_nuevo = input("Ingrese otro nombre: ")
    # Valida que ingresen una edad válida (entre 1 y 200)
    edad_cliente_nuevo = pedir_entero("Ingrese la edad del cliente: ",1,200)
    # Valida que ingresen un tipo de cliente válido (1 o 2)
    tipo_cliente_nuevo = pedir_entero("Ingrese tipo (1=Regular/2=Frecuente): ", 1, 2)
    # Genera un código de cliente aleatorio entre 1 y lo definido en cantidad_registros
    codigo_cliente_nuevo = random.randint(1, cantidad_registros)
    # Valida que el código generado no exista y, si está ok, lo agrega a la lista
    while buscar_codigo(codigos_clientes, codigo_cliente_nuevo) == -1:
        codigos_clientes.append(codigo_cliente_nuevo)
    # Se agregan el resto de los campos
    nombres_clientes.append(nombre_cliente_nuevo)
    edades_clientes.append(edad_cliente_nuevo)
    tipos_clientes.append(tipo_cliente_nuevo)

    print("Cliente agregado correctamente.")

def listar_clientes():
    print("----------------------------------------")
    print("\n¿Cómo desea ordenar los clientes?")
    print("1. Por código")
    print("2. Por edad")

    opcion = pedir_entero("Seleccione una opción: ", 1, 2)

    if opcion == 1:
        ordenar_clientes_codigo()
    else:
        ordenar_clientes_edad()

    print("\n--------------- LISTADO DE CLIENTES ---------------")

    for i in range(len(codigos_clientes)):
        print("---------------------")
        print("Código:", codigos_clientes[i])
        print("Nombre:", nombres_clientes[i])
        print("Edad:", edades_clientes[i])
        if tipos_clientes[i] == 1:
            print("Tipo: Regular")
        else:
            print("Tipo: Frecuente")
        print("---------------------")

def modificar_cliente():
    print("------------------- Modificar Cliente ------------------")
    # Valida que se ingrese un entero mayor a 1
    codigo = pedir_entero_minimo("Ingrese el código del cliente a modificar: ", 1)
    # Busca primero que exista (o no) el cliente a modificar
    posicion = buscar_codigo(codigos_clientes, codigo)
    # Si no existe el cliente
    if posicion == -1:
        print("ERROR! No existe un cliente con ese código.")
    else:
        print("\nDatos actuales del cliente")
        print("--------------------------------")
        print("Código:", codigos_clientes[posicion])
        print("Nombre:", nombres_clientes[posicion])
        print("Edad:", edades_clientes[posicion])
        if tipos_clientes[posicion] == 1:
            print("Tipo de cliente: Regular")
        else:
            print("Tipo de cliente: Frecuente")
        print("--------------------------------")

        nuevo_nombre = input("Ingrese el nuevo nombre: ")
        # Valida que no ingresen un nombre vacío
        while nuevo_nombre == "":
            print("ERROR! El nombre no puede estar vacío.")
            nuevo_nombre = input("Ingrese el nuevo nombre: ")
        # Valida que la edad nueva sea un entero entre 1 y 200
        nueva_edad = pedir_entero("Ingrese la nueva edad: ", 1, 200)
        # Valida que el nuevo tipo de cliente sea un entero entre 1 y 2
        nuevo_tipo = pedir_entero("Ingrese el nuevo tipo de cliente (1=Regular/2=Frecuente): ", 1, 2)
        # Guardar modificaciones
        nombres_clientes[posicion] = nuevo_nombre
        edades_clientes[posicion] = nueva_edad
        tipos_clientes[posicion] = nuevo_tipo

        print("Cliente modificado correctamente.")

def eliminar_cliente():
    print("------------------- Eliminar Cliente ------------------")
    # Valida que se ingrese un entero mayor a 1
    codigo = pedir_entero_minimo("Ingrese el código del cliente a eliminar: ", 1)
    # Busca primero que exista (o no) el cliente a eliminar
    posicion_cliente = buscar_codigo(codigos_clientes, codigo)
    # Si existe
    if posicion_cliente != -1:
        # Verifica si tiene pasajes asociados -> si tiene no permite eliminarlo para preservar la integridad de los datos
        tiene_pasajes = False
        # Busca si hay algun pasaje asociado
        for i in range(len(codigos_cliente_pasajes)):
            if codigos_cliente_pasajes[i] == codigo:
                tiene_pasajes = True
        # Si el cliente tiene un pasaje le avisa al usuario
        if tiene_pasajes:
            print("ERROR! No se puede eliminar el cliente porque tiene pasajes asociados.")
        else:
            confirmar = input("¿Está seguro que desea eliminar al cliente? (SI/NO): ")
            # Valida que ingresen SI o NO sin importar las mayúsculas o minúsculas
            while confirmar != "SI" and confirmar != "si" and confirmar != "NO" and confirmar != "no":
                print("ERROR! Debe ingresar SI o NO.")
                confirmar = input("¿Está seguro que desea eliminar al cliente? (SI/NO): ")
            if confirmar == "SI" or confirmar == "si":
                # Eliminamos al cliente de todas las listas paralelas de Clientes
                codigos_clientes.pop(posicion_cliente)
                nombres_clientes.pop(posicion_cliente)
                edades_clientes.pop(posicion_cliente)
                tipos_clientes.pop(posicion_cliente)
                print("Cliente eliminado correctamente.")
            elif confirmar == "NO" or confirmar == "no":
                print("Operación cancelada.")
    else:
        print("ERROR! No existe un cliente con ese código.")

## CRUD Destinos
def agregar_destino():
    print("--------------- Agregar un Destino Nuevo ---------------")
    nombre_destino_nuevo = input("Ingrese nombre del destino: ")
    # Valida que no ingresen un nombre de destino vacío
    while nombre_destino_nuevo == "":
        print("ERROR! Nombre vacío.")
        nombre_destino_nuevo = input("Ingrese otro nombre: ")
    # Valida que ingresen una distancia válida (un flotante positivo)
    distancia_destino_nuevo = pedir_flotante_minimo("Ingrese distancia (km): ", 1.0)
    # Valida que ingresen un precio válido (un flotante positivo)
    precio_destino_nuevo = pedir_flotante_minimo("Ingrese precio base: ", 1.0)
    # Genera un código de destino aleatorio entre 1 y lo definido en cantidad_registros
    codigo_destino_nuevo = random.randint(1,cantidad_registros)
    # Valida que el código generado no exista y, si está ok, lo agrega a la lista
    while buscar_codigo(codigos_destinos, codigo_destino_nuevo) == -1:
        codigos_destinos.append(codigo_destino_nuevo)
    # Se agregan el resto de los campos
    nombres_destinos.append(nombre_destino_nuevo)
    distancias_destinos.append(distancia_destino_nuevo)
    precios_destinos.append(precio_destino_nuevo)

    print("Destino agregado correctamente.")

def listar_destinos():
    print("\n¿Cómo desea ordenar los destinos?")
    print("1. Por código")
    print("2. Por distancia")
    print("3. Por precio base")

    opcion = pedir_entero("Seleccione una opción: ", 1, 3)

    if opcion == 1:
        ordenar_destinos_codigo()
    elif opcion == 2:
        ordenar_destinos_distancia()
    else:
        ordenar_destinos_precio()

    print("\n--------------- LISTADO DE DESTINOS ---------------")
    for i in range(len(codigos_destinos)):
        print("----------------------------------------")
        print("Código:", codigos_destinos[i])
        print("Nombre:", nombres_destinos[i])
        print("Distancia:", distancias_destinos[i], "km")
        print(f"Precio base: ${precios_destinos[i]} ARS")

def modificar_destino():
    print("------------------- Modificar Destino ------------------")
    # Valida que se ingrese un entero mayor a 1
    codigo = pedir_entero_minimo("Ingrese código del destino a modificar: ", 1)
    # Busca primero que exista (o no) el destino a modificar
    posicion = buscar_codigo(codigos_destinos, codigo)
    # Si existe
    if posicion != -1:
        print("\nDatos actuales del destino")
        print("--------------------------------")
        print("Código:", codigos_destinos[posicion])
        print("Nombre:", nombres_destinos[posicion])
        print("Distancia (km):", distancias_destinos[posicion])
        print("Precio base (ARS) $", precios_destinos[posicion])
        print("--------------------------------")
        nuevo_nombre = input("Nuevo nombre: ")
        # Valida que no ingresen un nombre vacío
        while nuevo_nombre == "":
            print("ERROR! Nombre vacío.")
            nuevo_nombre = input("Nuevo nombre: ")
        # Valida que ingresen una distancia decimal positiva
        nueva_distancia = pedir_flotante_minimo("Nueva distancia: ", 1.0)
        # Valida que ingresen un precio decimal positivo
        nuevo_precio = pedir_flotante_minimo("Nuevo precio: ", 1.0)
        # Guardar modificaciones
        nombres_destinos[posicion] = nuevo_nombre
        distancias_destinos[posicion] = nueva_distancia
        precios_destinos[posicion] = nuevo_precio

        print("Destino modificado correctamente.")
    else:
        print("ERROR! No existe ese destino.")

def eliminar_destino():
    print("------------------- Eliminar Destino ------------------")
    # Valida que se ingrese un entero mayor a 1
    codigo = pedir_entero_minimo("Ingrese código del destino a eliminar: ", 1)
    # Busca primero que exista (o no) el destino a eliminar
    posicion_destino = buscar_codigo(codigos_destinos, codigo)
    # Si existe
    if posicion_destino != -1:
        # Verifica si tiene pasajes asociados -> si tiene no permite eliminarlo para preservar la integridad de los datos
        tiene_pasajes = False
        for i in range(len(codigos_destino_pasajes)):
            if codigos_destino_pasajes[i] == codigo:
                tiene_pasajes = True
        # Si existe un pasaje con ese destino le avisa al usuario
        if tiene_pasajes:
            print("ERROR! No se puede eliminar porque tiene pasajes asociados.")
        else:
            confirmacion = input("¿Está seguro que desea eliminar el destino? (SI/NO): ")
            # Valida que ingresen SI o NO sin importar las mayúsculas o minúsculas
            while confirmacion != "SI" and confirmacion != "si" and confirmacion != "NO" and confirmacion != "no":
                print("ERROR! Debe escribir si o no.")
                confirmacion = input("¿Está seguro que desea eliminar el destino? (SI/NO): ")
            if confirmacion == "SI" or confirmacion == "si":
                # Eliminamos al destino de todas las listas paralelas de Destinos
                codigos_destinos.pop(posicion_destino)
                nombres_destinos.pop(posicion_destino)
                distancias_destinos.pop(posicion_destino)
                precios_destinos.pop(posicion_destino)
                print("Destino eliminado correctamente.")
            else:
                print("Operación cancelada")
    else:
        print("ERROR! No existe un destino con ese código.")

## CRUD Pasajes
def agregar_pasaje():
    print("--------------- Agregar un Pasaje Nuevo ---------------")
    # Valida que ingresen un cliente válido (entero positivo)
    codigo_cliente_pasaje_nuevo = pedir_entero_minimo("Ingrese el código del cliente para este pasaje: ", 1)
    # Valida que ese cliente ingresado exista previamente
    while buscar_codigo(codigos_clientes, codigo_cliente_pasaje_nuevo) == -1:
        print ("ERROR! No existe un cliente con ese código.")
        codigo_cliente_pasaje_nuevo = pedir_entero_minimo("Ingrese otro código de cliente: ", 1)
    # Valida que ingresen un código de destino válido (entero positivo)
    codigo_destino_pasaje_nuevo = pedir_entero_minimo("Ingrese el código del destino para este pasaje: ", 1)
    # Valida que ese destino ingresado exista previamente
    while buscar_codigo(codigos_destinos, codigo_destino_pasaje_nuevo) == -1:
        print ("ERROR! No existe un destino con ese código.")        
        codigo_destino_pasaje_nuevo = pedir_entero_minimo("Ingrese otro código de destino: ", 1)
    # Valida que se ingrese un entero positivo
    cantidad_pasaje_nuevo = pedir_entero_minimo("Ingrese la cantidad de pasajes a comprar: ", 1)
    # Valida que se ingrese 1, 2 o 3        
    medio_pago_pasaje_nuevo = pedir_entero("Ingrese el medio de pago (1=Efectivo/2=Tarjeta/3=Transferencia): ", 1, 3)
    # Genera un código de pasaje aleatorio entre 1 y lo definido en cantidad_registros
    codigo_pasaje_nuevo = random.randint(1, cantidad_registros)
    # Valida que el código generado no exista y, si está ok, lo agrega a la lista
    while buscar_codigo(codigos_pasajes, codigo_pasaje_nuevo) == -1:
        codigos_pasajes.append(codigo_pasaje_nuevo)
    # Se agregan el resto de los campos
    codigos_cliente_pasajes.append(codigo_cliente_pasaje_nuevo)
    codigos_destino_pasajes.append(codigo_destino_pasaje_nuevo)
    cantidades_pasajes.append(cantidad_pasaje_nuevo)
    medios_pago_pasajes.append(medio_pago_pasaje_nuevo)
    print("Pasaje agregado correctamente.")

def listar_pasajes():
    print("\n¿Cómo desea ordenar los pasajes?")
    print("1. Por código")
    print("2. Por cantidad")
    print("3. Por medio de pago")

    opcion = pedir_entero("Seleccione una opción: ", 1, 3)

    if opcion == 1:
        ordenar_pasajes_codigo()
    elif opcion == 2:
        ordenar_pasajes_cantidad()
    else:
        ordenar_pasajes_medio_pago()

    print("\n--------------- LISTADO DE PASAJES ---------------")
    for i in range(len(codigos_pasajes)):
        print("----------------------------------------")
        print("Código pasaje:", codigos_pasajes[i])
        print("Código cliente:", codigos_cliente_pasajes[i])
        print("Código destino:", codigos_destino_pasajes[i])
        print("Cantidad pasajes:", cantidades_pasajes[i])
        if medios_pago_pasajes[i] == 1:
            print("Medio de pago: Efectivo")
        elif medios_pago_pasajes[i] == 2:
            print("Medio de pago: Tarjeta")
        elif medios_pago_pasajes[i] == 3:
            print("Medio de pago: Transferencia")
        print("----------------------------------------")

def modificar_pasaje():
    print("------------------- Modificar Pasaje ------------------")
    # Valida que se ingrese un entero mayor a 1
    pasaje_a_modificar = pedir_entero_minimo("Ingrese el código del pasaje a modificar: ",1)
    # Busca primero que exista (o no) el pasaje
    posicion = buscar_codigo(codigos_pasajes, pasaje_a_modificar)
    # Si existe
    if posicion != -1:
        print("\nDatos actuales del pasaje")
        print("--------------------------------")
        print("Código pasaje:", codigos_pasajes[posicion])
        print("Código cliente:", codigos_cliente_pasajes[posicion])
        print("Código destino:", codigos_destino_pasajes[posicion])
        print("Cantidad pasajes:", cantidades_pasajes[posicion])
        if medios_pago_pasajes[posicion] == 1:
            print("Medio de pago: Efectivo")
        elif medios_pago_pasajes[posicion] == 2:
            print("Medio de pago: Tarjeta")
        elif medios_pago_pasajes[posicion] == 3:
            print("Medio de pago: Transferencia")
        print("--------------------------------")

        # Valida que el código de cliente ingresado sea un entero positivo
        nuevo_codigo_cliente = pedir_entero_minimo("Nuevo código cliente: ", 1)
        # Valida que el código de cliente exista
        while buscar_codigo(codigos_clientes, nuevo_codigo_cliente) == -1:
            print("ERROR. Ese cliente no existe.")
            nuevo_codigo_cliente = pedir_entero_minimo("Ingrese otro código cliente: ", 1)
        # Valida que el código de destino ingresado sea un entero positivo
        nuevo_codigo_destino = pedir_entero_minimo("Nuevo código destino: ", 1)
        # Valida que el código de destino exista
        while buscar_codigo(codigos_destinos, nuevo_codigo_destino) == -1:
            print("ERROR. Ese destino no existe.")
            nuevo_codigo_destino = pedir_entero_minimo("Ingrese otro código destino: ", 1)
        # Valida que la cantidad ingresada sea un entero positivo
        nueva_cantidad = pedir_entero_minimo("Nueva cantidad de pasajes: ", 1)
        # Valida que el medio de pago ingresado sea 1, 2 o 3
        nuevo_medio_pago = pedir_entero("Nuevo medio de pago (1=Efectivo, 2=Tarjeta, 3=Transferencia): ", 1, 3)
        # Guardar modificaciones
        codigos_cliente_pasajes[posicion] = nuevo_codigo_cliente
        codigos_destino_pasajes[posicion] = nuevo_codigo_destino
        cantidades_pasajes[posicion] = nueva_cantidad
        medios_pago_pasajes[posicion] = nuevo_medio_pago

        print("Pasaje modificado correctamente.")
    else:
        print("No existe el pasaje ingresado.")

def eliminar_pasaje():
    print("------------------- Eliminar Pasaje ------------------")
    # Valida que se ingrese un entero positivo
    codigo = pedir_entero_minimo("Ingrese el código del pasaje a eliminar: ", 1)
    # Busca si existe ese pasaje
    posicion_pasaje = buscar_codigo(codigos_pasajes, codigo)
    # Si existe
    if posicion_pasaje != -1:
        confirmacion = input("¿Está seguro que desea eliminar el pasaje? (SI/NO): ")
        # Valida que ingresen SI o NO sin importar las mayúsculas o minúsculas
        while confirmacion != "SI" and confirmacion != "si" and confirmacion != "NO" and confirmacion != "no":
            print("ERROR! Debe ingresar SI o NO.")
            confirmacion = input("¿Está seguro que desea eliminar el pasaje? (SI/NO): ")
        if confirmacion == "SI" or confirmacion == "si":
            # Eliminamos el pasaje de todas las listas de Pasajes
            codigos_pasajes.pop(posicion_pasaje)
            codigos_cliente_pasajes.pop(posicion_pasaje)
            codigos_destino_pasajes.pop(posicion_pasaje)
            cantidades_pasajes.pop(posicion_pasaje)
            medios_pago_pasajes.pop(posicion_pasaje)
            print("Pasaje eliminado correctamente.")
        elif confirmacion == "NO" or confirmacion == "no":
            print("Operación cancelada")
    else:
        print("ERROR! No existe un pasaje con ese código.")


# Ordenamientos

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

def ordenar_clientes_edad():
    for i in range(len(edades_clientes) - 1):
        pos_menor = i
        for j in range(i + 1, len(edades_clientes)):
            if edades_clientes[j] < edades_clientes[pos_menor]:
                pos_menor = j
        if pos_menor != i:
            edades_clientes[i], edades_clientes[pos_menor] = edades_clientes[pos_menor], edades_clientes[i]
            codigos_clientes[i], codigos_clientes[pos_menor] = codigos_clientes[pos_menor], codigos_clientes[i]
            nombres_clientes[i], nombres_clientes[pos_menor] = nombres_clientes[pos_menor], nombres_clientes[i]
            tipos_clientes[i], tipos_clientes[pos_menor] = tipos_clientes[pos_menor], tipos_clientes[i]

#DESTINOS--> Burbujeo
def ordenar_destinos_distancia():
    for i in range(len(distancias_destinos)-1):
        for j in range(len(distancias_destinos)-1-i):
            if distancias_destinos[j] > distancias_destinos[j+1]:
                distancias_destinos[j], distancias_destinos[j+1] = distancias_destinos[j+1], distancias_destinos[j]
                codigos_destinos[j], codigos_destinos[j+1] = codigos_destinos[j+1], codigos_destinos[j]
                nombres_destinos[j], nombres_destinos[j+1] = nombres_destinos[j+1], nombres_destinos[j]
                precios_destinos[j], precios_destinos[j+1] = precios_destinos[j+1], precios_destinos[j]

def ordenar_destinos_codigo():
    for i in range(len(codigos_destinos) - 1):
        for j in range(len(codigos_destinos) - 1 - i):
            if codigos_destinos[j] > codigos_destinos[j + 1]:
                codigos_destinos[j], codigos_destinos[j + 1] = codigos_destinos[j + 1], codigos_destinos[j]
                nombres_destinos[j], nombres_destinos[j + 1] = nombres_destinos[j + 1], nombres_destinos[j]
                distancias_destinos[j], distancias_destinos[j + 1] = distancias_destinos[j + 1], distancias_destinos[j]
                precios_destinos[j], precios_destinos[j + 1] = precios_destinos[j + 1], precios_destinos[j]

def ordenar_destinos_precio():
    for i in range(len(precios_destinos) - 1):
        for j in range(len(precios_destinos) - 1 - i):
            if precios_destinos[j] > precios_destinos[j + 1]:
                precios_destinos[j], precios_destinos[j + 1] = precios_destinos[j + 1], precios_destinos[j]
                codigos_destinos[j], codigos_destinos[j + 1] = codigos_destinos[j + 1], codigos_destinos[j]
                nombres_destinos[j], nombres_destinos[j + 1] = nombres_destinos[j + 1], nombres_destinos[j]
                distancias_destinos[j], distancias_destinos[j + 1] = distancias_destinos[j + 1], distancias_destinos[j]

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

def ordenar_pasajes_codigo():
    for i in range(1, len(codigos_pasajes)):
        codigo_aux = codigos_pasajes[i]
        cliente_aux = codigos_cliente_pasajes[i]
        destino_aux = codigos_destino_pasajes[i]
        cantidad_aux = cantidades_pasajes[i]
        medio_aux = medios_pago_pasajes[i]
        j = i - 1

        while j >= 0 and codigos_pasajes[j] > codigo_aux:
            codigos_pasajes[j + 1] = codigos_pasajes[j]
            codigos_cliente_pasajes[j + 1] = codigos_cliente_pasajes[j]
            codigos_destino_pasajes[j + 1] = codigos_destino_pasajes[j]
            cantidades_pasajes[j + 1] = cantidades_pasajes[j]
            medios_pago_pasajes[j + 1] = medios_pago_pasajes[j]
            j -= 1
        codigos_pasajes[j + 1] = codigo_aux
        codigos_cliente_pasajes[j + 1] = cliente_aux
        codigos_destino_pasajes[j + 1] = destino_aux
        cantidades_pasajes[j + 1] = cantidad_aux
        medios_pago_pasajes[j + 1] = medio_aux

def ordenar_pasajes_medio_pago():
    for i in range(1, len(medios_pago_pasajes)):
        medio_aux = medios_pago_pasajes[i]
        codigo_aux = codigos_pasajes[i]
        cliente_aux = codigos_cliente_pasajes[i]
        destino_aux = codigos_destino_pasajes[i]
        cantidad_aux = cantidades_pasajes[i]
        j = i - 1

        while j >= 0 and medios_pago_pasajes[j] > medio_aux:
            medios_pago_pasajes[j + 1] = medios_pago_pasajes[j]
            codigos_pasajes[j + 1] = codigos_pasajes[j]
            codigos_cliente_pasajes[j + 1] = codigos_cliente_pasajes[j]
            codigos_destino_pasajes[j + 1] = codigos_destino_pasajes[j]
            cantidades_pasajes[j + 1] = cantidades_pasajes[j]
            j -= 1
        medios_pago_pasajes[j + 1] = medio_aux
        codigos_pasajes[j + 1] = codigo_aux
        codigos_cliente_pasajes[j + 1] = cliente_aux
        codigos_destino_pasajes[j + 1] = destino_aux
        cantidades_pasajes[j + 1] = cantidad_aux

# Búsquedas
def buscar_cliente_menu():
    print("------------------- Buscar Cliente ------------------")
    ordenar_clientes_codigo() #Para el funcionamiento del calculo binario
    codigo_a_buscar = pedir_entero_minimo("Ingrese el código del cliente a buscar: ", 1)
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
    print("-----------------------------------")
    
    opcion_busqueda = pedir_entero("Seleccione una opción de búsqueda: ", 1, 3)

    if opcion_busqueda == 1:
        codigo_a_buscar = pedir_entero_minimo("Ingrese el código del destino a buscar: ", 1)
        posicion_destino = buscar_codigo(codigos_destinos, codigo_a_buscar)

        if posicion_destino != -1:
            mostrar_datos_destino(posicion_destino)
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
    codigo_a_buscar = pedir_entero_minimo("Ingrese el código del pasaje a buscar: ", 1)
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

# Estadísticas
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

    matriz = [[0], [0]]

    for i in range(len(codigos_pasajes)):

        codigo_cliente = codigos_cliente_pasajes[i]
        cantidad = cantidades_pasajes[i]

        posicion_cliente = buscar_codigo(
            codigos_clientes,
            codigo_cliente
        )

        if posicion_cliente != -1:

            tipo_cliente = tipos_clientes[posicion_cliente]

            if tipo_cliente == 1:
                matriz[0][0] += cantidad

            elif tipo_cliente == 2:
                matriz[1][0] += cantidad

    print("\nCantidad de pasajes por tipo de cliente")
    print("----------------------------------------")
    print("Tipo Cliente\tCantidad")

    print("Regular\t\t", matriz[0][0])
    print("Frecuente\t", matriz[1][0])


def estadistica_pasaje_destino():

    matriz = []

    for i in range(len(codigos_destinos)):
        matriz.append([0])

    for i in range(len(codigos_pasajes)):

        codigo_destino = codigos_destino_pasajes[i]
        cantidad = cantidades_pasajes[i]

        posicion_destino = buscar_codigo(
            codigos_destinos,
            codigo_destino
        )

        if posicion_destino != -1:
            matriz[posicion_destino][0] += cantidad

    print("\nCantidad de pasajes vendidos por destino")
    print("-----------------------------------------")
    print("Destino\t\tCantidad")

    for i in range(len(matriz)):
        print(
            nombres_destinos[i], "\t\t",
            matriz[i][0]
        )

def estadistica_ventas_medio_pago():

    matriz = [[0], [0], [0]]

    for i in range(len(codigos_pasajes)):

        codigo_destino = codigos_destino_pasajes[i]
        cantidad = cantidades_pasajes[i]
        medio_pago = medios_pago_pasajes[i]

        posicion_destino = buscar_codigo(
            codigos_destinos,
            codigo_destino
        )

        if posicion_destino != -1:

            precio = precios_destinos[posicion_destino]
            importe = cantidad * precio

            matriz[medio_pago - 1][0] += importe

    print("\nRecaudación según medio de pago")
    print("--------------------------------")
    print("Medio de Pago\tRecaudación")

    print("Efectivo\t$", matriz[0][0])
    print("Tarjeta\t\t$", matriz[1][0])
    print("Transferencia\t$", matriz[2][0])

### 

print("--------------- Sistema de Venta de Pasajes ---------------")
print("--------------------- Inicio de sesión --------------------")

user = input("Ingrese su usuario: ")
password = input("Ingrese su contraseña: ")

if login(user, password):
    print("--------------- Sistema de Venta de Pasajes ---------------")
    print("Bienvenido,", user)

    menu_principal()
