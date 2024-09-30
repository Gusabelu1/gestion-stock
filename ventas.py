def menuProductos(productos):
    opciones = len(productos)
    listaProductos = []

    while True:
        print()
        print("---------------------------")
        print("SELECCIONE LOS PRODUCTOS")
        print("---------------------------")
        for i in range(opciones):
            print(f"[{i+1}] {productos[i]}")
        print("---------------------------")
        print("[0] Volver a las categorías")
        print()
        
        opcion = input("Seleccione una opción: ")
        if opcion in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
            if opcion == "0":
                break
            else:
                for i in range(opciones):
                    if i+1 == int(opcion):
                        listaProductos.append(productos[i])
        else:
            input("Opción inválida. Presione ENTER para volver a seleccionar.")
    print()

    return listaProductos

def generarVenta():
    productos = {
        "M-001": {"nombre": "Monitor", "stock": 10, "precio": 500, "categoria": "monitor"},
        "T-001": {"nombre": "Teclado", "stock": 5, "precio": 100, "categoria": "teclado"},
    }

    print("---------------------------")
    print("GENERAR VENTA")
    print("---------------------------")

    cliente = input("Ingrese el nombre del cliente: ")
    listaProductos = []
    print("")

    opciones = 2
    while True:
        print("---------------------------")
        print("CATEGORIAS DE PRODUCTOS")
        print("---------------------------")
        print("[1] Monitores")
        print("---------------------------")
        print("[0] Cancelar")
        print("[X] Generar Venta")
        print()

        opcion = input("Seleccione una opción: ")
        if opcion == "X" or opcion == "x":
            print(listaProductos)
            break
        
        if opcion in [str(i) for i in range(0, opciones)]: # Sólo continua si se elije una opcion de menú válida
            if opcion == "0": # Opción salir del programa
                break
            elif opcion == "1":   # Generar Venta
                print("Menu de Monitores")
                listaProductos.append(menuProductos([producto for producto in productos if producto['categoria'] == 'monitor']))
        else:
            input("Opción inválida. Presione ENTER para volver a seleccionar.")
    print()