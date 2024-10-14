def validarNumero(nro,mensaje):
    """
    Función para validar si un string puede ser convertido a un número entero positivo.
    
    Parámetros:
    nro (str): El string que se va a validar y convertir a número.
    mensaje (str): Mensaje que se imprimirá si la validación falla.
    
    Retorna:
    bool: True si el string puede ser convertido a un número entero positivo, False en caso contrario.
    """
    numeroValido= True
    try:
        nro = int(nro)
        if nro < 0:
            numeroValido = False      
    except ValueError:
        numeroValido = False
        print(mensaje)
    return numeroValido

