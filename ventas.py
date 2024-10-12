"""
-----------------------------------------------------------------------------------------------
Título: Ventas
Fecha: 08/10/2024
Autor: Grupo 02

Descripción: Sistema de gestion de ventas

Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
import inventario
import archivos

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def menuProductos(productos):
    listaProductos = []

    while True:
        print()
        print("---------------------------")
        print("SELECCIONE LOS PRODUCTOS")
        print("---------------------------")
        inventario.verProductos(productos)
        print("---------------------------")
        print("[0] Volver a las categorías")
        print()
        
        opcion = input("Seleccione una opción: ")
        if opcion == "0" or opcion in [codigo for codigo in productos]: # Sólo continua si se elije una opcion de menú válida
            if opcion == "0":
                break
            else:
                print(productos[opcion])
                while True:
                    print()
                    cantidad = input("Ingrese la cantidad | [0] Cancelar: ")

                    if cantidad == "0":
                        break
                    elif int(cantidad) > 0 and int(cantidad) <= int(productos[opcion]["stock"]):
                        if opcion not in listaProductos:
                            listaProductos.append((opcion, int(cantidad)))

                        productos[opcion]["stock"] -= int(cantidad)
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
        else:
            input("Opción inválida. Presione ENTER para volver a seleccionar.")
    print()

    return listaProductos

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def generarVenta():
    print("---------------------------")
    print("GENERAR VENTA")
    print("---------------------------")

    cliente = input("Ingrese el nombre del cliente: ")
    listaProductos = []
    print("")

    categorias = set()
    for producto in inventario.productos.values():
        categorias.add(producto["categoria"])
    
    opciones = len(categorias)
    while True:
        print("---------------------------")
        print("CATEGORIAS DE PRODUCTOS")
        print("---------------------------")

        for i, categoria in enumerate(sorted(categorias), start=1):
            print(f"[{i}] {categoria.capitalize()}")
        
        print("---------------------------")
        print("[0] Cancelar")
        print("[X] Generar Venta")
        print()

        opcion = input("Seleccione una opción: ")
        if opcion == "X" or opcion == "x":
            print(listaProductos)
            break
        
        if opcion in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
            if opcion == "0": # Opción salir del programa
                break
            else:
                for i, categoria in enumerate(sorted(categorias), start=1):
                    if int(opcion) == i:
                        print(f"Menu de {categoria}")
                        productos_filtrados = {producto_id: detalles for producto_id, detalles in inventario.productos.items() if detalles["categoria"] == categoria}

                        listaProductos.append(menuProductos(productos_filtrados))
                        break
        else:
            input("Opción inválida. Presione ENTER para volver a seleccionar.")
    print()