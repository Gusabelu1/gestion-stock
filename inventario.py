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
import funciones, archivos

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------s

# verProductos
def verProductos(categoria = None, id = None): 
    """
    Función para visualizar un listado de productos.
    
    Parámetros:
    categoria   : String (default None): Categoría para filtrar o None para no filtrar.
    id          : String (default None): ID para filtrar o None para no filtrar.
    
    Retorna:
    None.
    """
    diccionario = archivos.leer_todo(archivos.archivo_productos)

    if categoria:
        dic = {clave: diccionario[clave] for clave in diccionario if diccionario[clave]["categoria"] == categoria}
    elif id:
        dic = {clave: diccionario[clave] for clave in diccionario if clave == id}
    else:
        dic = diccionario

    for codigo, detalles in dic.items():
        print(f"Codigo: {codigo} | Nombre: {detalles["nombre"]} | Stock: {detalles["stock"]} | Precio: {detalles["precio"]} | Categoría: {detalles["categoria"]}")
    return

# agregarProductos
def agregarProductos(): 
    """
    Función para agregar un nuevo producto al listado.

    Parámetros:
    None

    Retorna:
    Int : 0 Si la operacion fué exitosa, 1 si hubo algun error.
    """
    codigo = input("Ingrese el codigo del producto o [0] para volver al menu: ").upper()

    if codigo == "0":
        return 1
            
    nombre = input("Ingrese el nombre del producto: ")
    
    stock = input("Ingrese el stock del producto: ")
    while funciones.validarNumero(stock,"El stock ingresado no es válido.") == False:
        stock = input("Ingrese el stock del producto nuevamente: ")
        
    precio = input("Ingrese el precio por unidad del producto: ")
    while funciones.validarNumero(precio,"El precio ingresado no es válido.") == False:
        precio = input("Ingrese el precio por unidad del producto nuevamente: ")
        
    categoria = input("Ingrese la categoria del producto: ").lower()
    agregar = input("Esta seguro que desea agregar el nuevo producto? \n[x] Confirmar | [0] Cancelar: ").lower()

    while agregar != "x" and agregar != "0":
        print("Opcion no valida.")
        agregar = input("Esta seguro que desea agregar el nuevo producto? \n[x] Confirmar | [0] Cancelar: ").lower()

    if agregar == "x":
        producto = {
            codigo: {
                "nombre": nombre,
                "stock": int(stock),
                "precio": int(precio),
                "categoria": categoria
            }
        }

        return archivos.crear(archivos.archivo_productos, producto)
    else:
        return 1

# modificarProducto
def modificarProducto(): 
    """
    Función para modificar valores de un producto del listado.
    
    Parámetros:
    None
    
    Retorna:
    Int : 0 Si la operacion fué exitosa, 1 si hubo algun error.
    """
    diccionario = archivos.leer_todo(archivos.archivo_productos)
    codigo = input("Ingrese el codigo del producto que desea modificar o [0] para cancelar: ").upper()  
    
    while codigo not in diccionario and codigo != "0":
        print(f"El producto con código {codigo} no existe.")
        codigo = input("Ingrese el nuevamente el codigo del producto que desea modificar o [0] para cancelar: ").upper()     
    
    if codigo == "0":
        return 1
    
    producto = diccionario[codigo]

    print("Nombre actual del producto: ", diccionario[codigo]["nombre"])
    nombre = input("Ingrese el nuevo nombre del producto | [Enter] para no modificar: ")
    if nombre != "":
        producto['nombre'] = nombre
    
    print("Stock actual del producto: ", diccionario[codigo]["stock"])
    stock = input("Ingrese el nuevo stock del producto | [Enter] para no modificar: ")
    while stock != "":
        if funciones.validarNumero(stock,"El stock ingresado no es válido."):
            producto['stock'] = int(stock)
            break
        stock = input("Ingrese nuevamente el stock del producto | [Enter] para no modificar: ")

        
    print("Precio actual del producto: ", diccionario[codigo]["precio"])
    precio = input("Ingrese el nuevo precio del producto | [Enter] para no modificar: ")
    while precio != "":
        if funciones.validarNumero(precio,"El precio ingresado no es válido."):
            producto['precio'] = int(precio)
            break
        precio = input("Ingrese nuevamente el precio del producto | [Enter] para no modificar: ")
        
    print("Categoría actual del producto: ", diccionario[codigo]["categoria"])
    categoria = input("Ingrese la nueva categoria del producto | [Enter] para no modificar: : ").lower()
    if categoria != "":
        producto['categoria'] = categoria

    actualizar = input(f"Esta seguro que desea actualizar el producto {codigo}? \n[x] Confirmar | [0] Cancelar: ").lower()

    while actualizar != "x" and actualizar != "0":
        print("Opcion no valida.")
        actualizar = input(f"Esta seguro que desea actualizar el producto {codigo}? \n[x] Confirmar | [0] Cancelar: ").lower()

    if actualizar == "x":
        return archivos.actualizar(archivos.archivo_productos, codigo, producto)
    else:
        return 1

# eliminarProductos
def eliminarProductos():
    """
    Función para eliminar un producto del listado.
    
    Parámetros:
    None

    Retorna:
    bool: True si el producto se eliminó exitosamente, False si no.
    """
    diccionario = archivos.leer_todo(archivos.archivo_productos)
    codigo = input("Ingrese el codigo del producto que desea eliminar o [0] para cancelar: ").upper()
    
    while codigo not in diccionario and codigo != "0":
        print(f"El codigo {codigo} no existe.")
        codigo = input("Ingrese el codigo del producto que desea eliminar o [0] para cancelar: ").upper()

    if codigo == "0":
        return 1
    
    verProductos(id = codigo)

    eliminar = input("Esta seguro que desea eliminar el producto? \n[x] Confirmar | [0] Cancelar: ").lower()

    while eliminar != "x" and eliminar != "0":
        print("Opcion no valida")
        eliminar = input("Esta seguro que desea eliminar el producto? \n[x] Confirmar | [0] Cancelar: ").lower()

    if eliminar == "x":
        return archivos.borrar(archivos.archivo_productos, codigo)
    else:
        return 1

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

            if opcion == "0": # Opción salir del inventario
                break

            elif opcion == "1": # Ver Invetnario
                verProductos()
            elif opcion == "2": # Agregar Productos
                if agregarProductos():
                    print("No se pudo agregar el producto.")
                else:
                    print("Producto agregado con exito.")
            elif opcion == "3": # Modificar Productos
                modificarProducto()
            elif opcion == "4": # Eliminar Productos
                if eliminarProductos():
                    print("No se pudo eliminar el producto.")
                else:
                    print("Producto eliminado con exito.")
    return