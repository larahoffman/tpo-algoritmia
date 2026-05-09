def login(usuario, contrasenia):
    acceso = False
    while usuario != usuario_admin or contrasenia != contrasenia_admin:
        print("Error! Usuario o contraseña incorrectos. Intente nuevamente.")
        usuario = input("Ingrese su usuario: ")
        contrasenia = input("Ingrese su contraseña: ")
    acceso = True
    return acceso

usuario_admin = "admin"
contrasenia_admin = "Admin2026!"

print("--------------- Sistema de Venta de Pasajes ---------------")
print("--------------------- Inicio de sesión --------------------")

user = input("Ingrese su usuario: ")
password = input("Ingrese su contraseña: ")

if login(user, password):
    print("--------------- Sistema de Venta de Pasajes ---------------")
    print("Bienvenido,", usuario_admin)
    print('''
    ----------------------
    |    Menú principal  |
    |    1. Clientes     |
    |    2. Destinos     |
    |    3. Pasajes      |
    ----------------------
        '''
    )


