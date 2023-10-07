# Parámetro con valores predeterminados

"""def saludar(nombre="amigo"):
    print("Hola,", nombre, "Bienvenido a la clase")

saludar("Carlos")
"""
# USo de *args y **kwargs

def mostrar_argumentos(*args, **kwargs):
    print("Argumentos posicionales:", args)
    print("Argumentos con nombre:", kwargs)

# Llamado a la función con argumentos posicionales

mostrar_argumentos(1,2,3,4,5)

# Llamada con argumentos con nombre
mostrar_argumentos(nombre="Juan", edad=25, ciudad="Madrid")

# Llamada con argumentos posicionales y con nombre
mostrar_argumentos(10, 20, nombre="Ana", apellido="Garcia")

# LLamada con argumentos posicionales y con nombre usando *args y **kwargs

argumentos_posicionales = (5,10,15)
argumentos_con_nombre = {"nombre": "Luis", "profesión": "Ingeniero"}

mostrar_argumentos(*argumentos_posicionales, **argumentos_con_nombre)