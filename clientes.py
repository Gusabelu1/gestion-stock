"""
-----------------------------------------------------------------------------------------------
Título: Clientes
Fecha: 08/10/2024
Autor: Grupo 02

Descripción: Sistema de gestion de clientes

Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
import re

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
clientes = {}

def validar_email(email):
    """
    Funcion que valida mediante expresion regular el ingreso de un email
    Recibe: String
    Devuelve: Booleano
    """
    patron = r'^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.]+$'
    
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
        agregar = input("Esta seguro que desea agregar el nuevo cliente? Si/No: ").lower()

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
                
            opcion = int(input("Seleccione una opción: "))
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
    55667788: {"nombre": "Sofía", "apellido": "Hernández", "correo": "sofia.hernandez@gmail.com", "direccion": "Calle Palma 100", "telefono": "555-1010"},
    33445566: {"nombre": "Pedro", "apellido": "Ramírez", "correo": "pedro.ramirez@yahoo.com", "direccion": "Av. Los Andes 234", "telefono": "555-1212"},
    22113344: {"nombre": "Lucía", "apellido": "Vega", "correo": "lucia.vega@hotmail.com", "direccion": "Calle Libertad 789", "telefono": "555-2323"},
    77889900: {"nombre": "Raúl", "apellido": "Mendoza", "correo": "raul.mendoza@gmail.com", "direccion": "Av. San Juan 100", "telefono": "555-3434"},
    66778899: {"nombre": "Clara", "apellido": "Ferrer", "correo": "clara.ferrer@yahoo.com", "direccion": "Calle Roca 432", "telefono": "555-4545"},
    99880077: {"nombre": "Manuel", "apellido": "Guzmán", "correo": "manuel.guzman@hotmail.com", "direccion": "Calle Sarmiento 567", "telefono": "555-5656"},
    55667799: {"nombre": "Fernanda", "apellido": "Rojas", "correo": "fernanda.rojas@gmail.com", "direccion": "Av. Las Flores 987", "telefono": "555-6767"},
    11220099: {"nombre": "Julio", "apellido": "Silva", "correo": "julio.silva@yahoo.com", "direccion": "Calle Mitre 111", "telefono": "555-7878"},
    88990077: {"nombre": "Valeria", "apellido": "Ortega", "correo": "valeria.ortega@gmail.com", "direccion": "Calle Saavedra 222", "telefono": "555-8989"},
    66554433: {"nombre": "Tomás", "apellido": "Suárez", "correo": "tomas.suarez@hotmail.com", "direccion": "Av. Libertador 333", "telefono": "555-9090"},
    77665544: {"nombre": "Gabriela", "apellido": "Domínguez", "correo": "gabriela.dominguez@yahoo.com", "direccion": "Calle Belgrano 444", "telefono": "555-1122"},
    33446688: {"nombre": "Martín", "apellido": "Escobar", "correo": "martin.escobar@gmail.com", "direccion": "Av. Los Incas 555", "telefono": "555-2233"},
    55447766: {"nombre": "Elena", "apellido": "Pineda", "correo": "elena.pineda@hotmail.com", "direccion": "Calle Lavalle 666", "telefono": "555-3344"},
    11334455: {"nombre": "Nicolás", "apellido": "Arce", "correo": "nicolas.arce@yahoo.com", "direccion": "Av. Córdoba 777", "telefono": "555-4455"},
    99007711: {"nombre": "Mónica", "apellido": "Zamora", "correo": "monica.zamora@gmail.com", "direccion": "Calle San Martín 888", "telefono": "555-5566"},
    44330022: {"nombre": "Esteban", "apellido": "Flores", "correo": "esteban.flores@hotmail.com", "direccion": "Av. Mayo 999", "telefono": "555-6677"},
    66559988: {"nombre": "Isabel", "apellido": "Cabrera", "correo": "isabel.cabrera@yahoo.com", "direccion": "Calle Mendoza 101", "telefono": "555-7788"},
    99887700: {"nombre": "Sebastián", "apellido": "Herrera", "correo": "sebastian.herrera@gmail.com", "direccion": "Av. Pueyrredón 202", "telefono": "555-8899"},
    55448899: {"nombre": "Laura", "apellido": "Rivera", "correo": "laura.rivera@hotmail.com", "direccion": "Calle Rivadavia 303", "telefono": "555-9900"},
    33442211: {"nombre": "Diego", "apellido": "Luna", "correo": "diego.luna@yahoo.com", "direccion": "Calle Viamonte 404", "telefono": "555-1011"},
    11229988: {"nombre": "Rocío", "apellido": "Díaz", "correo": "rocio.diaz@gmail.com", "direccion": "Av. Sarmiento 505", "telefono": "555-2121"},
    77886655: {"nombre": "Alejandro", "apellido": "Molina", "correo": "alejandro.molina@hotmail.com", "direccion": "Calle Brown 606", "telefono": "555-3232"},
    99881122: {"nombre": "Cecilia", "apellido": "Villalba", "correo": "cecilia.villalba@gmail.com", "direccion": "Calle Moreno 707", "telefono": "555-4343"},
    66558833: {"nombre": "Mauricio", "apellido": "Paz", "correo": "mauricio.paz@yahoo.com", "direccion": "Av. San Martín 808", "telefono": "555-5454"},
    55443322: {"nombre": "Alicia", "apellido": "Sosa", "correo": "alicia.sosa@hotmail.com", "direccion": "Calle Colon 909", "telefono": "555-6565"},
    11220077: {"nombre": "Javier", "apellido": "García", "correo": "javier.garcia@yahoo.com", "direccion": "Av. Alem 1010", "telefono": "555-7676"},
}

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
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