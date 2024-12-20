import json

usuario = "admin"

def leerArchivo(archivo):
    """
        Lee el .json especificado y devuelve los datos como un diccionario.
        Recibe: String
        Devuelve: Diccionario o Int
    """
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        if usuario == "admin":
            print("Ocurrio un error al leer el archivo.")
        return 1

def escribirArchivo(archivo, datos):
    """
        Escribe los datos en un .json especificado.
        Recibe: String y Diccionario
        Devuelve: Int
    """
    try:
        with open(archivo, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=4)
        return 0
    except:
        if usuario == "admin":
            print("Ocurrió un error al escribir en el archivo.")
        return 1

def crear(archivo, data):
    """
        Crea un nuevo registro en el .json.
        Recibe: String y Diccionario
        Devuelve: Int
    """
    try:
        datos = leerArchivo(archivo)
        
        id = list(data.keys())[0]
        
        if id in datos:
            print(f"Ya existe un registro con el ID {id} en {archivo}.")
            return 1
        
        datos[id] = data[id]
        # print(f"Se agregó el registro con el ID {id} en {archivo}")
        return escribirArchivo(archivo, datos)
    except:
        return 1

def leer_todo(archivo):
    """
        Lee todos los registros del .json.
        Recibe: String
        Devuelve: Diccionario o Int
    """
    
    return leerArchivo(archivo)

def actualizar(archivo, id, data):
    """
        Actualiza un registro en el .json.
        Recibe: String y Diccionario
        Devuelve: Int
    """
    datos = leerArchivo(archivo)
    
    if id in datos:
        datos[id] = data  # Actualizamos los datos
        # print(f"Se modificó el registro con el ID {id} en {archivo}")
        return escribirArchivo(archivo, datos)
    else:
        print(f"No se encontró el registro con el ID {id} en {archivo}")
        return 1

def borrar(archivo, id):
    """
        Borra un registro en el .json según el ID recibido por parámetro.
        Recibe: String y Int
        Devuelve: Int
    """
    datos = leerArchivo(archivo)
    
    if id in datos:
        del datos[id]
        # print(f"Se borró el registro con el ID {id} de {archivo}")
        return escribirArchivo(archivo, datos)
    else:
        print(f"No se encontró el registro con el ID {id} en {archivo}")
        return 1

# Definir archivos
archivo_clientes = 'clientes.json'
archivo_compras = 'compras.json'
archivo_productos = 'productos.json'
archivo_ventas = 'ventas.json'