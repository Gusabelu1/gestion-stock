import json

def leer_archivo(archivo):
    """Lee el contenido de un archivo .json y devuelve los datos como un diccionario."""
    try:
        with open(archivo, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}  # Si no existe el archivo o está vacío, devuelve un diccionario vacío

def escribir_archivo(archivo, datos):
    """Escribe los datos en un archivo .json."""
    with open(archivo, 'w') as f:
        json.dump(datos, f, indent=4)

def crear(archivo, nuevo_dato):
    """Crea una nueva entrada en el archivo .json, usando un diccionario de diccionarios."""
    datos = leer_archivo(archivo)
    
    # nuevo_dato es un diccionario con el formato {"CL-001": {...}}
    id_cliente = list(nuevo_dato.keys())[0]  # Obtenemos la clave del diccionario
    
    if id_cliente in datos:
        print(f"El ID {id_cliente} ya existe en {archivo}")
        return
    
    # Agregamos el nuevo dato al diccionario de datos
    datos[id_cliente] = nuevo_dato[id_cliente]
    escribir_archivo(archivo, datos)
    print(f"Entrada agregada con ID {id_cliente} en {archivo}")

def leer_todo(archivo):
    """Lee todas las entradas de un archivo .json."""
    return leer_archivo(archivo)

def actualizar(archivo, datos_actualizados):
    """Actualiza una entrada en el archivo .json usando un diccionario de diccionarios."""
    datos = leer_archivo(archivo)
    id_cliente = list(datos_actualizados.keys())[0]  # Obtenemos la clave del diccionario
    
    if id_cliente in datos:
        datos[id_cliente] = datos_actualizados[id_cliente]  # Actualizamos los datos
        escribir_archivo(archivo, datos)
        print(f"Entrada con ID {id_cliente} actualizada en {archivo}")
    else:
        print(f"Entrada con ID {id_cliente} no encontrada en {archivo}")

def borrar(archivo, id_cliente):
    """Borra una entrada en el archivo .json según el ID del cliente."""
    datos = leer_archivo(archivo)
    
    if id_cliente in datos:
        del datos[id_cliente]
        escribir_archivo(archivo, datos)
        print(f"Entrada con ID {id_cliente} borrada de {archivo}")
    else:
        print(f"Entrada con ID {id_cliente} no encontrada en {archivo}")

# Definir archivos
archivo_clientes = 'clientes.json'
archivo_compras = 'compras.json'
archivo_productos = 'productos.json'
archivo_ventas = 'ventas.json'