"""
-----------------------------------------------------------------------------------------------
Título: Inventario
Fecha: 08/10/2024
Autor: Grupo 02

Descripción: Sistema de gestion de inventario

Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
import funciones

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------s

# verProductos
def verProductos(dic): 
    """
    Función para visualizar un listado de productos.
    
    Parámetros:
    dic (dict): Diccionario que contiene los productos, donde la clave es el código del producto 
                y el valor es un diccionario con los detalles del producto (nombre, stock, precio, categoría).
    
    Retorna:
    None.
    """
    for codigo, detalles in dic.items():
        print(f"Codigo: {codigo} | Nombre: {detalles["nombre"]} | Stock: {detalles["stock"]} | Precio: {detalles["precio"]} | Categoría: {detalles["categoria"]}")
    return

# agregarProductos
def agregarProductos(dic): 
    """
    Función para agregar un nuevo producto al listado.

    Parámetros:
    dic (dict): Diccionario que contiene los productos, donde la clave es el código del producto 
                y el valor es un diccionario con los detalles del producto (nombre, stock, precio, categoría).

    Retorna:
    bool: True si el producto se agregó exitosamente, False si no.
    """
    exito = True
    codigo = input("Ingrese el codigo del producto o [0] para volver al menu: ").upper()

    if codigo == "0":
        return

    while codigo in dic:
        print(f"El codigo {codigo} ya existe.")
        codigo = input("Ingrese el codigo del producto: ").upper()
            
    nombre = input("Ingrese el nombre del producto: ")
    
    while True:
        stock = input("Ingrese el stock del producto: ")
        if funciones.validarNumero(stock,"El stock ingresado es incorrecto."):  
            break
        
    while True:
        precio = input("Ingrese el precio por unidad del producto: ")
        if funciones.validarNumero(precio,"El precio ingresado es incorrecto. Inténtalo de nuevo."):  
            break
        
    categoria = input("Ingrese la categoria del producto: ").lower()
    agregar = input("Esta seguro que desea agregar el nuevo producto? Si/No: ").lower()

    while agregar != "si" and agregar != "no":
        print("Opcion no valida.")
        agregar = input("Esta seguro que desea agregar el nuevo producto? Si/No: ").lower()

    if agregar == "si":
        dic[codigo] = {
            "nombre": nombre,
            "stock": stock,
            "precio": precio,
            "categoria": categoria
        }
    else:
        exito = False
    return exito

# modificarProducto
def modificarProducto(dic): 
    """
    Función para modificar valores de un producto del listado.
    
    Parámetros:
    dic (dict): Diccionario que contiene los productos, donde la clave es el código del producto 
                y el valor es un diccionario con los detalles del producto (nombre, stock, precio, categoría).
    
    Retorna:
    None.
    """
    codigo = input("Ingrese el codigo del producto que desea modificar o [0] para volver: ").upper()  
    if codigo == "0":
        return      
    while codigo not in dic:
        print(f"El codigo {codigo} ya existe")
        codigo = input("Ingrese el codigo del producto que desea modificar: ").upper()            
    while True:
        opciones = 5
        while True:
            print()
            print("-----------------------------")
            print(f" MENÚ PARA MODIFICAR \n")
            print(f"Codigo: {codigo} | Nombre: {dic[codigo]["nombre"]} | Stock: {dic[codigo]["stock"]} | Precio: {dic[codigo]["precio"]} | Categoría: {dic[codigo]["categoria"]}")
            print("-----------------------------")
            print("[1] Modificar nombre")
            print("[2] Modificar stock")
            print("[3] Modificar precio")
            print("[4] Modificar categoria")
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
            nombre = input("Ingrese un nuevo nombre (o [X] para cancelar): ").lower()
            if nombre == "x": # 
                continue
            dic[codigo]['nombre'] = nombre
            print(f"\nEl nombre de {codigo} se modifico con exito")

        elif opcion == "2":   # Modificar stock
            while True:
                stock = input("Ingrese un nuevo stock (o [X] para cancelar): ").lower()
                if funciones.validarNumero(stock,"El stock ingresado es incorrecto."):
                    dic[codigo]['stock'] = stock  
                    print(f"\nEl stock de {codigo} se modifico con exito")

                    break
                elif stock == "x": # 
                    break          
            
        elif opcion == "3":   # Modificar precio           
            while True:
                precio = input("Ingrese un nuevo precio (o [X] para cancelar): ").lower()
                if funciones.validarNumero(precio,"El precio ingresado es incorrecto."):  
                    dic[codigo]['precio'] = precio
                    print(f"\nEl precio de {codigo} se modifico con exito")

                    break
                elif precio == "x": # 
                    break 
            
        elif opcion == "4":   # Modificar categoria
            categoria = input("Ingrese un nuevo nombre (o [X] para cancelar): ").lower()
            if categoria == "x": # 
                continue
            dic[codigo]['categoria'] = categoria 
            print(f"\nLa categoria de {codigo} se modifico con exito")
            
    return 

# eliminarProductos
def eliminarProductos(dic):
    """
    Función para eliminar un producto del listado.
    
    Parámetros:
    dic (dict): Diccionario que contiene los productos, donde la clave es el código del producto 
                y el valor es un diccionario con los detalles del producto (nombre, stock, precio, categoría).
    
    Retorna:
    bool: True si el producto se eliminó exitosamente, False si no.
    """
    exito = True
    codigo = input("Ingrese el codigo del producto que desea eliminar o 0 para volver: ").upper()
    if codigo == "0":
        return
    
    while codigo not in dic:
        print(f"El codigo {codigo} no existe")
        codigo = input("Ingrese el codigo del producto que desea eliminar: ").upper()

    
    print(f"Codigo: {codigo} | Nombre: {dic[codigo]["nombre"]} | Stock: {dic[codigo]["stock"]} | Precio: {dic[codigo]["precio"]} | Categoría: {dic[codigo]["categoria"]}")

    eliminar = input("Esta seguro que desea eliminar el producto? Si/No: ").lower()

    while eliminar != "si" and eliminar != "no":
        print("Opcion no valida")
        eliminar = input("Esta seguro que desea eliminar el producto? Si/No: ").lower()

    if eliminar == "si":
        dic.pop(codigo)
    else:
        exito = False
    return exito

productos = {
    "M-001": {"nombre": "Monitor", "stock": 10, "precio": 500, "categoria": "monitor"},
    "T-001": {"nombre": "Teclado", "stock": 5, "precio": 100, "categoria": "teclado"},
    "R-001": {"nombre": "Ratón", "stock": 15, "precio": 50, "categoria": "ratón"},
    "P-001": {"nombre": "Portátil", "stock": 8, "precio": 1200, "categoria": "ordenador"},
    "A-001": {"nombre": "Auriculares", "stock": 25, "precio": 80, "categoria": "audio"},
    "C-001": {"nombre": "Cámara Web", "stock": 12, "precio": 150, "categoria": "cámara"},
    "H-001": {"nombre": "Hub USB", "stock": 30, "precio": 40, "categoria": "accesorios"},
    "F-001": {"nombre": "Fuente de Poder", "stock": 10, "precio": 75, "categoria": "hardware"},
    "E-001": {"nombre": "Escritorio", "stock": 5, "precio": 200, "categoria": "mobiliario"},
    "S-001": {"nombre": "Silla Gamer", "stock": 7, "precio": 300, "categoria": "mobiliario"},
    "M-002": {"nombre": "Monitor UltraWide", "stock": 6, "precio": 700, "categoria": "monitor"},
    "T-002": {"nombre": "Teclado Mecánico", "stock": 4, "precio": 150, "categoria": "teclado"},
    "R-002": {"nombre": "Ratón Inalámbrico", "stock": 20, "precio": 60, "categoria": "ratón"},
    "P-002": {"nombre": "PC Gaming", "stock": 3, "precio": 2000, "categoria": "ordenador"},
    "A-002": {"nombre": "Altavoces", "stock": 18, "precio": 120, "categoria": "audio"},
    "C-002": {"nombre": "Cámara de Seguridad", "stock": 9, "precio": 300, "categoria": "cámara"},
    "H-002": {"nombre": "Hub USB-C", "stock": 14, "precio": 60, "categoria": "accesorios"},
    "F-002": {"nombre": "Fuente de Poder Modular", "stock": 5, "precio": 100, "categoria": "hardware"},
    "E-002": {"nombre": "Escritorio Ajustable", "stock": 2, "precio": 400, "categoria": "mobiliario"},
    "S-002": {"nombre": "Silla Ejecutiva", "stock": 6, "precio": 250, "categoria": "mobiliario"},
    "M-003": {"nombre": "Monitor 4K", "stock": 9, "precio": 850, "categoria": "monitor"},
    "T-003": {"nombre": "Teclado Ergonómico", "stock": 8, "precio": 130, "categoria": "teclado"},
    "R-003": {"nombre": "Ratón Gaming", "stock": 17, "precio": 70, "categoria": "ratón"},
    "P-003": {"nombre": "Laptop Ultraligera", "stock": 4, "precio": 1800, "categoria": "ordenador"},
    "A-003": {"nombre": "Auriculares Inalámbricos", "stock": 22, "precio": 90, "categoria": "audio"},
    "C-003": {"nombre": "Cámara Reflex", "stock": 3, "precio": 1200, "categoria": "cámara"},
    "H-003": {"nombre": "Hub Thunderbolt", "stock": 10, "precio": 150, "categoria": "accesorios"},
    "F-003": {"nombre": "Fuente de Poder ATX", "stock": 7, "precio": 110, "categoria": "hardware"},
    "E-003": {"nombre": "Escritorio Gaming", "stock": 5, "precio": 450, "categoria": "mobiliario"},
    "S-003": {"nombre": "Silla de Oficina", "stock": 11, "precio": 350, "categoria": "mobiliario"}
}

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def gestionInventario():
    """
        Función que representa el menú principal del inventario.
        
        Recibe: Nada.
        
        Retorna: None.
    """
    while True:
            opciones = 5
            while True:
                print()
                print("---------------------------")
                print("    MENÚ DEL INVENTARIO    ")
                print("---------------------------")
                print("[1] Ver Inventario")
                print("[2] Agregar productos")
                print("[3] Modificar productos")
                print("[4] Eliminar productos")
                print("---------------------------")
                print("[0] Volver al menú")
                print()
                
                opcion = input("Seleccione una opción: ")
                if opcion in [str(i) for i in range(0, opciones)]: # Sólo continua si se elije una opcion de menú válida
                    break
                else:
                    input("Opción inválida. Presione ENTER para volver a seleccionar.")
            print()

            if opcion == "0": # Opción salir del programa
                break

            elif opcion == "1":   # Generar Venta
                verProductos(productos)
            elif opcion == "2":   # Administrar Inventario
                if agregarProductos(productos):
                    print("Producto agregado con exito")
                else:
                    print("El producto no fue agregado")
            elif opcion == "3":   # Administrar Clientes
                modificarProducto(productos)
            elif opcion == "4":   # Historial de Ventas
                if eliminarProductos(productos):
                    print("Producto eliminado con exito")
                else:
                    print("El producto no fue eliminado")
    return