usuario = "admin"
contrasenia = "Admin2026!"

print("--------------- Sistema de Venta de Pasajes ---------------")
print("--------------------- Inicio de sesión --------------------")

user = input("Ingrese su usuario: ")
password = input("Ingrese su contraseña: ")

while user != usuario or password != contrasenia:
    print("Error! Usuario o contraseña incorrectos. Intente nuevamente.")
    user = input("Ingrese su usuario: ")
    password = input("Ingrese su contraseña: ")

print("--------------- Sistema de Venta de Pasajes ---------------")
print("Bienvenido,", user)
print('''
----------------------
|    Menú principal  |
|    1. Clientes     |
|    2. Destinos     |
|    3. Pasajes      |
----------------------
    '''
)


