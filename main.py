"""
-----------------------------------------------------------------------------------------------
Título: Equipo 02 - TP
Fecha: 23/09/2024
Autor:
Santino Castro

Descripción:
Sistema de gestión de productos, proveedores y clientes de un comercio electrónico dedicado 
a la venta de componentes de computadoras.

Pendientes:
Marcar realizados con "X"

1) Agregar CRUD con módulos:
    - Productos
    - Clientes
    - Ventas

2) Búsqueda por filtros

3) Generar ventas modificando clientes y stock de productos a la par

4) Descarga y monitoreo de stock mediante archivos (CSV)

-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
import ventas, inventario


#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    #-------------------------------------------------
    # Inicialización de variables
    #----------------------------------------------------------------------------------------------

    #-------------------------------------------------
    # Bloque de menú
    #----------------------------------------------------------------------------------------------
    while True:
        opciones = 5
        while True:
            print()
            print("---------------------------")
            print("     MENÚ DEL SISTEMA      ")
            print("---------------------------")
            print("[1] Generar venta")
            print("[2] Administrar inventario")
            print("[3] Administar clientes")
            print("[4] Historial de ventas")
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
            print("Llamar a generar venta")
            ventas.generarVenta()
        elif opcion == "2":   # Administrar Inventario
            print("Llamar a administrar inventario")
            inventario.gestionInventario()
        elif opcion == "3":   # Administrar Clientes
            print("Llamar a administrar clientes")
        elif opcion == "4":   # Historial de Ventas
            print("Llamar a historial de ventas")


# Punto de entrada al programa
main()