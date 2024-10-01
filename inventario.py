def VerProductos(dic):
    for codigo, detalles in dic.items():
        print(f"Codigo: {codigo} | Nombre: {detalles["nombre"]} | Stock: {detalles["stock"]} | Precio: {detalles["precio"]} | Categoría: {detalles["categoria"]}")
    return

def AgregarProductos(dic):
    codigo = input("Ingrese el codigo del producto: ").upper()
    
    while codigo in dic:
        print(f"El codigo {codigo} ya existe")
        codigo = input("Ingrese el codigo del producto: ").upper()
            
    nombre = input("Ingrese el nombre del producto: ")
    stock = input("Ingrese el stock del producto: ")
    precio = input("Ingrese el precio por unidad del producto: ")
    categoria = input("Ingrese el categoria del producto: ").lower()
    dic[codigo] = {
        "nombre": nombre,
        "stock": stock,
        "precio": precio,
        "categoria": categoria
    }
    return

def ModificarProducto(dic):
    codigo = input("Ingrese el codigo del producto que desea modificar: ").upper()        
    while codigo not in dic:
        print(f"El codigo {codigo} ya existe")
        codigo = input("Ingrese el codigo del producto que desea modificar: ").upper()            
    while True:
        opciones = 5
        while True:
            print()
            print("-----------------------------")
            print(f" MENÚ PARA MODIFICAR ({codigo})")
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
            return   # También puede ser sys.exit() para lo cual hay que importar el módulo sys

        elif opcion == "1":   # Modificar nombre
            nombre = input("Ingrese un nuevo nombre: ")
            dic[codigo]['nombre'] = nombre
        elif opcion == "2":   # Modificar stock
            stock = input("Ingrese un nuevo stock: ")
            dic[codigo]['stock'] = stock
        elif opcion == "3":   # Modificar precio
            precio = input("Ingrese un nuevo precio: ")
            dic[codigo]['nombre'] = precio
        elif opcion == "4":   # Modificar categoria
            categoria = input("Ingrese un nuevo nombre")
            dic[codigo]['categoria'] = categoria               
    return 

def EliminarProductos(dic):
    codigo = input("Ingrese el codigo del producto que desea eliminar: ").upper()
    
    while codigo not in dic:
        print(f"El codigo {codigo} no existe")
        codigo = input("Ingrese el codigo del producto que desea eliminar: ").upper()
    dic.pop(codigo)
    print(f"El producto {codigo} ha sido eliminado con exito")
    return

productos = {
    "M-001": {"nombre": "Monitor", "stock": 10, "precio": 500, "categoria": "monitor"},
    #"T-001": {"nombre": "Teclado", "stock": 5, "precio": 100, "categoria": "teclado"},
    #"R-001": {"nombre": "Ratón", "stock": 15, "precio": 50, "categoria": "ratón"},
    #"P-001": {"nombre": "Portátil", "stock": 8, "precio": 1200, "categoria": "ordenador"},
    #"A-001": {"nombre": "Auriculares", "stock": 25, "precio": 80, "categoria": "audio"},
    #"C-001": {"nombre": "Cámara Web", "stock": 12, "precio": 150, "categoria": "cámara"},
    #"H-001": {"nombre": "Hub USB", "stock": 30, "precio": 40, "categoria": "accesorios"},
    #"F-001": {"nombre": "Fuente de Poder", "stock": 10, "precio": 75, "categoria": "hardware"},
    #"E-001": {"nombre": "Escritorio", "stock": 5, "precio": 200, "categoria": "mobiliario"},
    #"S-001": {"nombre": "Silla Gamer", "stock": 7, "precio": 300, "categoria": "mobiliario"},
    #"M-002": {"nombre": "Monitor UltraWide", "stock": 6, "precio": 700, "categoria": "monitor"},
    #"T-002": {"nombre": "Teclado Mecánico", "stock": 4, "precio": 150, "categoria": "teclado"},
    #"R-002": {"nombre": "Ratón Inalámbrico", "stock": 20, "precio": 60, "categoria": "ratón"},
    #"P-002": {"nombre": "PC Gaming", "stock": 3, "precio": 2000, "categoria": "ordenador"},
    #"A-002": {"nombre": "Altavoces", "stock": 18, "precio": 120, "categoria": "audio"},
    #"C-002": {"nombre": "Cámara de Seguridad", "stock": 9, "precio": 300, "categoria": "cámara"},
    #"H-002": {"nombre": "Hub USB-C", "stock": 14, "precio": 60, "categoria": "accesorios"},
    #"F-002": {"nombre": "Fuente de Poder Modular", "stock": 5, "precio": 100, "categoria": "hardware"},
    #"E-002": {"nombre": "Escritorio Ajustable", "stock": 2, "precio": 400, "categoria": "mobiliario"},
    #"S-002": {"nombre": "Silla Ejecutiva", "stock": 6, "precio": 250, "categoria": "mobiliario"}
}

while True:
        opciones = 5
        while True:
            print()
            print("---------------------------")
            print("     MENÚ DEL SISTEMA      ")
            print("---------------------------")
            print("[1] Ver Inventario")
            print("[2] Agregar productos")
            print("[3] Modificar productos")
            print("[4] Eliminar productos")
            print("---------------------------")
            print("[0] Salir del programa")
            print()
            
            opcion = input("Seleccione una opción: ")
            if opcion in [str(i) for i in range(0, opciones)]: # Sólo continua si se elije una opcion de menú válida
                break
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
        print()

        if opcion == "0": # Opción salir del programa
            exit() # También puede ser sys.exit() para lo cual hay que importar el módulo sys

        elif opcion == "1":   # Generar Venta
            VerProductos(productos)
        elif opcion == "2":   # Administrar Inventario
            AgregarProductos(productos)
        elif opcion == "3":   # Administrar Clientes
            ModificarProducto(productos)
        elif opcion == "4":   # Historial de Ventas
            EliminarProductos(productos)


# Punto de entrada al programa
main()
