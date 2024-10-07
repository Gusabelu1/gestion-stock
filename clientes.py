import re

clientes = {}

def validar_email(email):
    """
    Funcion que valida mediante expresion regualar el ingreso de un email
    Recibe: String
    Devuelve: Booleano
    """
    patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    if re.match(patron, email):
        return True
    else:
        return False

def verClientes(dic):
    """
    Funcion que permite ver un listado de los clientes
    Recibe: Diccionario
    Devuelve: Nada
    """
    for dni, descripcion in dic.items():
        print(f"Dni: {dni} | Nombre: {descripcion["nombre"]} | Apellido: {descripcion["apellido"]} | Correo: {descripcion["correo"]} | Direccion: {descripcion["direccion"]} | Telefono: {descripcion["telefono"]}")
    return
def crearCliente(dic):
    """
    Funcion que permite crear un cliente para el sistema y guardarlo en un diccionario
    Recibe: Diccionario
    Devuelve: Booleano
    """
    exito = True
    dni = int(input("Ingrese el dni del cliente o 0 para volver al menu: "))

    if dni == 0:
        return

    while dni in dic:
        print(f"El dni {dni} ya existe")
        dni = int(input("Ingrese el dni del cliente: "))
    nombre = input("Ingrese el nombre del cliente: ").lower()
    apellido = input("Ingrese el apellido del cliente: ").lower()
    correo = input("Ingrese el correo del cliente: ")
    while validar_email(correo) == False:
        print("Correo invalido")
        correo = input("Ingrese el correo del cliente: ")
    direccion = input("Ingrese la direccion del cliente: ").lower()
    telefono = input("Ingrese el telefono del cliente: ")
    agregar = input("Esta seguro que desea agregar el nuevo cliente? Si/No: ").lower()

    while agregar != "si" and agregar != "no":
        print("Opcion no valida")
        agregar = input("Esta seguro que desea agregar el nuevo producto? Si/No: ").lower()

    if agregar == "si":
        dic[dni] = {
            "nombre": nombre,
            "apellido": apellido,
            "correo": correo,
            "direccion": direccion,
            "telefono": telefono
        }
    else:
        exito = False
    return exito

def actualizarCliente(dic):
    """
    Funcion que permite actualizar la informacion de algun cliente ya creado
    Recibe: Diccionario
    Devuelve: Booleano
    """
    dni = int(input("Ingrese el dni del cliente que desea modificar o 0 para volver: "))  
    if dni == "0":
        return      
    while dni not in dic:
        print(f"El dni {dni} ya existe")
        dni = int(input("Ingrese el dni del cliente que desea modificar: "))          
    while True:
        opciones = 5
        while True:
            print()
            print("-----------------------------")
            print(f" MENÚ PARA MODIFICAR ({dni})")
            print("-----------------------------")
            print("[1] Modificar nombre")
            print("[2] Modificar apellido")
            print("[3] Modificar correo")
            print("[4] Modificar direccion")
            print("[5] Modificar telefono")
            print("---------------------------")
            print("[0] Volver")
            print()
                
            opcion = input("Seleccione una opción: ")
            if opcion in [str(i) for i in range(0, opciones)]: # Sólo continua si se elije una opcion de menú válida
                break
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
        print()

        if opcion == "0": # Opción salir del programa
            break

        elif opcion == "1":   # Modificar nombre
            nombre = input("Ingrese un nuevo nombre: ")
            dic[dni]['nombre'] = nombre
        elif opcion == "2":   # Modificar apellido
            apellido = input("Ingrese un nuevo apellido: ")
            dic[dni]['apellido'] = apellido
        elif opcion == "3":   # Modificar correo
            correo = input("Ingrese un nuevo correo: ")
            while validar_email(correo) == False:
                print("Correo invalido")
                correo = input("Ingrese un nuevo correo: ")
            dic[dni]['correo'] = correo
        elif opcion == "4":   # Modificar direccion
            direccion = input("Ingrese una nueva direccion: ")
            dic[dni]['direccion'] = direccion
        elif opcion == "5":   # Modificar telefono
            telefono = input("Ingrese un nuevo telefono: ")
            dic[dni]['telefono'] = telefono                    
    return

def eliminarCliente(dic):
    """
    Funcion que permite eliminar un cliente creado anteriormente que este dentro del diccionario
    Recibe: Diccionario
    Devuelve: 
    """
    exito = True
    dni = int(input("Ingrese el dni del cliente que desea eliminar o 0 para volver: "))
    if dni == "0":
        return
    
    while dni not in dic:
        print(f"El cliente con dni {dni} no existe")
        dni = int(input("Ingrese el dni del cliente que desea eliminar: "))

    eliminar = input(f"Esta seguro que desea eliminar el cliente {dic[dni]["nombre"]} {dic[dni]["apellido"]}? Si/No: ").lower()

    while eliminar != "si" and eliminar != "no":
        print("Opcion no valida")
        eliminar = input(f"Esta seguro que desea eliminar el cliente {dic[dni]["nombre"]} {dic[dni]["apellido"]}? Si/No: ").lower()

    if eliminar == "si":
        dic.pop(dni)
    else:
        exito = False
    return exito

clientes = {
    12345678: {"nombre": "Juan", "apellido": "Pérez", "correo": "juan.perez@gmail.com", "direccion": "Calle Falsa 123", "telefono": "555-1234"},
    87654321: {"nombre": "María", "apellido": "Gómez", "correo": "maria.gomez@yahoo.com", "direccion": "Av. Siempre Viva 456", "telefono": "555-5678"},
    11223344: {"nombre": "Carlos", "apellido": "Rodríguez", "correo": "carlos.rodriguez@hotmail.com", "direccion": "Calle Luna 789", "telefono": "555-9012"},
    44332211: {"nombre": "Ana", "apellido": "Martínez", "correo": "ana.martinez@gmail.com", "direccion": "Calle Sol 321", "telefono": "555-3456"},
    99887766: {"nombre": "Luis", "apellido": "López", "correo": "luis.lopez@yahoo.com", "direccion": "Calle Estrella 654", "telefono": "555-7890"},
}
def gestionClientes():
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
            print("[4] Inactivar Cliente")
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
            break

        elif opcion == "1":     # Ver Clientes
            verClientes(clientes)
        elif opcion == "2":     # Crear Cliente
            crearCliente(clientes)
        elif opcion == "3":     # Actualizar Cliente
            actualizarCliente(clientes)
        elif opcion == "4":     # Eliminar Cliente
            eliminarCliente(clientes)
    return