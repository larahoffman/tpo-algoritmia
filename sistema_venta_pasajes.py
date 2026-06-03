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

#def buscar_codigo(lista, )

def agregar_cliente():
    print("--------------- Agregar un Cliente Nuevo ---------------")
     
    
def modificar_cliente():
    print("------------------- Modificar Cliente ------------------")
    cliente_a_modificar = int(input("Ingrese el codigo del cliente a modificar: "))
    pass


# def eliminar_cliente():
#     print("------------------- Eliminar Cliente ------------------")
#     cliente_a_eliminar = int(input("Ingrese el código del cliente a eliminar: "))
#     pos = buscar_cliente(cliente_a_eliminar, codigo)

#LOGIN    

print("--------------- Sistema de Venta de Pasajes ---------------")
print("--------------------- Inicio de sesión --------------------")

user = input("Ingrese su usuario: ")
password = input("Ingrese su contraseña: ")

#MENÚ
if login(user, password):
    print("--------------- Sistema de Venta de Pasajes ---------------")
    print("Bienvenido,", usuario_admin)
    print('''
    ---------------------------------
    |    Menú principal             |
    |    1. Gestión de clientes     |
    |    2. Gestión de destinos     |
    |    3. Gestión de pasajes      |
    |    4. Salir                   |
    ---------------------------------
        '''
    )
    opcion_menu = int(input("Seleccione una opción: "))
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
        opcion_menu_clientes= int(input("Seleccione una opción: "))

        if opcion_menu_clientes == 1:
            # funcion alta
            agregar_cliente()
            pass
        elif opcion_menu_clientes == 2:
            # funcion baja
            pass
        elif opcion_menu_clientes == 3:
            # funcion update
            modificar_cliente()
            pass
        elif opcion_menu_clientes == 4:
            # Funcion listado
            pass
        else:
            pass
        




        
    


 