clientes = {}

def verClientes(dic):
    for dni, datos in clientes.items():
        print(f"DNI: {dni}, Datos: {datos}")

def crearCliente(dni, nombre, apellido, correo, direccion, telefono):
    clientes[dni] = {
        'nombre': nombre,
        'apellido': apellido,
        'correo': correo,
        'direccion': direccion,
        'telefono': telefono
    }
    print(f"Cliente {nombre} creado.")

def actualizarCliente(dic): #VER QUE DEJE LO ANTEIOR AL DEJAR VACIO
    dni = input("Ingrese el DNI del cliente a modificar: ")
    if dni in clientes:
        
        nombre = input("Ingrese el nuevo nombre (dejar vacío para no modificar): ")
        apellido = input("Ingrese el nuevo apellido (dejar vacío para no modificar): ")
        correo = input("Ingrese el nuevo correo (dejar vacío para no modificar): ")
        direccion = input("Ingrese la nueva dirección (dejar vacío para no modificar): ")
        telefono = input("Ingrese el nuevo teléfono (dejar vacío para no modificar): ")
        
        clientes[dni]['nombre'] = nombre
        
        clientes[dni]['apellido'] = apellido
        
        clientes[dni]['correo'] = correo
        
        clientes[dni]['direccion'] = direccion
        
        clientes[dni]['telefono'] = telefono
        print(f"Cliente con DNI {dni} actualizado.")
    else:
        print("Cliente no encontrado.")

def eliminarCliente(dni):
    if dni in clientes:
        del clientes[dni]
        print(f"Cliente con DNI {dni} eliminado.")
    else:
        print("Cliente no encontrado.")

clientes = {
    "12345678": {"nombre": "Juan", "apellido": "Pérez", "correo": "juan.perez@gmail.com", "direccion": "Calle Falsa 123", "telefono": "555-1234"},
    #"87654321": {"nombre": "María", "apellido": "Gómez", "correo": "maria.gomez@yahoo.com", "direccion": "Av. Siempre Viva 456", "telefono": "555-5678"},
    #"11223344": {"nombre": "Carlos", "apellido": "Rodríguez", "correo": "carlos.rodriguez@hotmail.com", "direccion": "Calle Luna 789", "telefono": "555-9012"},
    #"44332211": {"nombre": "Ana", "apellido": "Martínez", "correo": "ana.martinez@gmail.com", "direccion": "Calle Sol 321", "telefono": "555-3456"},
    #"99887766": {"nombre": "Luis", "apellido": "López", "correo": "luis.lopez@yahoo.com", "direccion": "Calle Estrella 654", "telefono": "555-7890"},
}

while True:
    opciones = 4
    while True:
        print()
        print("---------------------------")
        print("     MENÚ DE CLIENTES      ")
        print("---------------------------")
        print("[1] Ver Clientes")
        print("[2] Crear Cliente")
        print("[3] Modificar Cliente")
        print("[4] Eliminar Cliente")
        print("---------------------------")
        print("[0] Salir del programa")
        print()
        
        opcion = input("Seleccione una opción: ")
        if opcion in [str(i) for i in range(0, opciones + 1)]:  # Solo continúa si se elige una opción de menú válida
            break
        else:
            input("Opción inválida. Presione ENTER para volver a seleccionar.")
        print()

    if opcion == "0":  # Opción salir del programa
        exit()  # También puede ser sys.exit() para lo cual hay que importar el módulo sys

    elif opcion == "1":   
        verClientes()
    elif opcion == "2":   
        dni = input("Ingrese el DNI: ")
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        correo = input("Ingrese el correo: ")
        direccion = input("Ingrese la dirección: ")
        telefono = input("Ingrese el teléfono: ")
        crearCliente(dni, nombre, apellido, correo, direccion, telefono)
    elif opcion == "3":
        actualizarCliente(clientes)
    elif opcion == "4":   # Eliminar Cliente
        dni = input("Ingrese el DNI del cliente a eliminar: ")
        eliminarCliente(dni)
