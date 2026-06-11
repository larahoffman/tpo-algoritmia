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
medios_pago_pasajes = [2, 1, 3, 2, 1, 3, 2, 1, 3, 2]  # 1 efectivo, 2 tarjeta, 3 transferencia

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
    if intentos > 3:
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
        # Validar que no ingresen un texto vacío
        print("Nombre actual:", nombres_clientes[posicion])
        nombres_clientes[posicion] = input("Nuevo nombre: ")
        print("Edad actual:", edades_clientes[posicion])
        edades_clientes[posicion] = es_entero(input("Nueva edad: "))
        print("Tipo de cliente:", tipos_clientes[posicion])
        tipos_clientes[posicion] = es_entero(input("Nuevo tipo de cliente: "))
    else:
        print("No existe el cliente ingresado")


def eliminar_cliente():
    print("------------------- Eliminar Cliente ------------------")
    cliente_a_eliminar = int(input("Ingrese el código del cliente a eliminar: "))
    codigo = pedir_entero_minimo("Código de cliente a eliminar: ", 1)
    posicion_cliente = buscar_codigo(cliente_a_eliminar, codigo)
    
    if posicion_cliente != -1:
        # Eliminar cliente de las listas
        codigos_clientes.pop(posicion_cliente)
        nombres_clientes.pop(posicion_cliente)
        edades_clientes.pop(posicion_cliente)
        tipos_clientes.pop(posicion_cliente)
        print("Cliente eliminado exitosamente.")
    elif posicion_cliente == -1: 
        print("Error. No existe un cliente con ese código.")
    else:
        print("Error. Ingrese un número válido.")

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
    cantidad_destino_efectivo = 0
    cantidad_destino_tarjeta = 0
    cantidad_destino_transferencia = 0
   
    for i in range(len(codigos_pasajes)):
        codigo_destino = codigos_destino_pasajes[i]
        medio_pago = medios_pago_pasajes[i]

        if medio_pago == 1:
            cantidad_destino_efectivo += 1
        elif medio_pago == 2:
            cantidad_destino_tarjeta += 1
        elif medio_pago == 3:
            cantidad_destino_transferencia += 1
    print("\nCantidad de pasajes por medio de pago para cada destino")
    print("--------------------------------------------------")
                    
    for i in range(len(codigos_destinos)):
        codigo_destino = codigos_destinos[i]
        nombre_destino = nombres_destinos[i]
    print("Destino:", nombre_destino)
    print("Efectivo:", cantidad_destino_efectivo)
    print("Tarjeta:", cantidad_destino_tarjeta)
    print("Transferencia:", cantidad_destino_transferencia)
    print("----------------------------------")

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
    cantidad_pasajes_destino = {}
    for i in range(len(codigos_pasajes)): 
        codigo_destino = codigos_destino_pasajes[i] 
        cantidad = cantidades_pasajes[i]
        
        if codigo_destino in cantidad_pasajes_destino: 
            cantidad_pasajes_destino[codigo_destino] += cantidad 
        else: 
            cantidad_pasajes_destino[codigo_destino] = cantidad
    print("\nCantidad de pasajes vendidos por destino")
    print("-----------------------------------------")
    
    for codigo_destino, cantidad in cantidad_pasajes_destino.items():
        posicion_destino = buscar_codigo(codigos_destinos, codigo_destino)
        if posicion_destino != -1:
            nombre_destino = nombres_destinos[posicion_destino]
    print("Destino:", nombre_destino)
    print("Cantidad de pasajes vendidos:", cantidad)
    print("----------------------------------")

def estadistica_medio_pago(): 
    cantidad_pago = {1: 0, 2: 0, 3: 0} 
    for i in range(len(codigos_pasajes)): 
        medio_pago = medios_pago_pasajes[i] 
        cantidad_pago[medio_pago] += 1
    print("\nCantidad de pasajes vendidos por medio de pago")
    print("---------------------------------------------")
    print("Efectivo:", cantidad_pago[1])
    print("Tarjeta:", cantidad_pago[2])
    print("Transferencia:", cantidad_pago[3])
    print("----------------------------------")

def agregar_destino():
    print("--------------- Agregar un Destino Nuevo ---------------")
                        
    codigo_destino_nuevo=int(input("Ingrese el código del destino que desea agregar: "))
    
    while buscar_codigo(codigos_destinos, codigo_destino_nuevo) !=-1:
        print ("ERROR! Ese código ya se encuentra registrado.")
    
    codigo_destino_nuevo=int(input("Ingrese otro código: "))

    nombre_destino_nuevo=str(input("Ingrese el nombre del destino: "))
    
    while nombre_destino_nuevo=="":
        print("ERROR! Nombre vacío.")
    
    nombre_destino_nuevo=str(input("Ingrese otro nombre: "))
    distancia_destino_nuevo=int(input("Ingrese la distancia del destino: "))
    
    while distancia_destino_nuevo <=0:
        print("ERROR! Distancia inválida.")
    
    distancia_destino_nuevo=int(input("Ingrese la distancia del destino: "))
    precio_destino_nuevo=int(input("Ingrese el precio del destino: "))
    
    while precio_destino_nuevo <=0:
        print("ERROR! Precio inválido.")
                            
    precio_destino_nuevo=int(input("Ingrese el precio del destino: "))

    codigos_destinos.append(codigo_destino_nuevo)
    nombres_destinos.append(nombre_destino_nuevo)
    distancias_destinos.append(distancia_destino_nuevo)
    precios_destinos.append(precio_destino_nuevo)

    print("Destino agregado correctamente.")

def eliminar_destino():
    print("------------------- Eliminar Destino ------------------")
    destino_a_eliminar = int(input("Ingrese el código del destino a eliminar: "))
    codigo = pedir_entero_minimo("Código de destino a eliminar: ", 1)
    posicion_destino = buscar_codigo(destino_a_eliminar, codigo)
                        
    if posicion_destino != -1:
        # Eliminar destino de las listas
        codigos_destinos.pop(posicion_destino)
        nombres_destinos.pop(posicion_destino)
        distancias_destinos.pop(posicion_destino)
        precios_destinos.pop(posicion_destino)
        print("Destino eliminado exitosamente.")
    
    elif posicion_destino == -1: 
        print("Error. No existe un destino con ese código.")
    else:
        print("Error. Ingrese un número válido.")

def estadistica_pasaje_destino():
    cantidad_pasajes_destino = {}
    for i in range(len(codigos_pasajes)):
        codigo_destino = codigos_destino_pasajes[i]
        cantidad = cantidades_pasajes[i]
                            
    if codigo_destino in cantidad_pasajes_destino:
        cantidad_pasajes_destino[codigo_destino] += cantidad
    else:
        cantidad_pasajes_destino[codigo_destino] = cantidad
        print("\nCantidad de pasajes vendidos por destino")
        print("-----------------------------------------")
                        
    for codigo_destino, cantidad in cantidad_pasajes_destino.items():
        posicion_destino = buscar_codigo(codigos_destinos, codigo_destino)
        if posicion_destino != -1:
            nombre_destino = nombres_destinos[posicion_destino]
            print("Destino:", nombre_destino)
            print("Cantidad de pasajes vendidos:", cantidad)
            print("----------------------------------")




#LOGIN    

print("--------------- Sistema de Venta de Pasajes ---------------")
print("--------------------- Inicio de sesión --------------------")

user = input("Ingrese su usuario: ")
password = input("Ingrese su contraseña: ")

#MENÚ
if login(user, password):
    print("--------------- Sistema de Venta de Pasajes ---------------")
    print("Bienvenido,", usuario_admin)
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
            '''
        )
        opcion_menu = int(input("Seleccione una opción: "))
        if opcion_menu == 1:
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
                '''
                )

                opcion_menu_clientes= es_entero(input("Seleccione una opción: "))
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

                elif opcion_destinos == 3: #Falta definir función 
                    modificar_destino()

                elif opcion_destinos == 4: #Falta definir función
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

            while opcion_busquedas != 5:

                print('''
                -------------------------------------
                |           Búsquedas               |
                | 1. Buscar cliente                 |
                | 2. Buscar destino                 |
                | 3. Buscar pasaje                  |
                | 4. Búsqueda binaria cliente       |
                | 5. Volver al menú principal       |
                -------------------------------------
                ''')

                opcion_busquedas = int(input("Seleccione una opción: "))

                if opcion_busquedas == 1:
                    buscar_cliente_menu()

                elif opcion_busquedas == 2:
                    buscar_destino_menu()

                elif opcion_busquedas == 3:
                    buscar_pasaje_menu()

                elif opcion_busquedas == 4:
                    busqueda_binaria_cliente()
                    
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

            #SALIDA
        elif opcion_menu == 6:

            print("\nGracias por utilizar el sistema.")
            print("Cerrando programa...")
            print("Programa finalizado.")



#BASE DE DATOS (JASON)
#meter todas las funciones en un archivo e importarlas, entonces te queda todo en una linea.
#Nosotros vamos a hacer un CRUD sobre :
#1.Import Json
#2.Crear dos funciones: def crear_json(...)--> va a tomar los datos de las listas y crea el json. si ya tenia algo lo reescribe y def cargar_jason(...)--> la info q esta en json la carga en nuestras listas
#3.Codigo, nombre, edad=cargar_json(...)

#CRUD



 
