# Creación de tuplas
coordenadas = (3,4, 5, 6, 7, 8, 9, 0, 1,2)
nombres = ("Alice", "Bob", "Charlie")
mezclados = (10, "Hola", 3.14)
"""
print(coordenadas)
print(nombres)
print(mezclados)

print(type(coordenadas))
print(type(nombres))
print(type(mezclados))
"""

# Ejemplo de acceso
x = coordenadas[6]
y = coordenadas[7]
print(x)
print(y)

# coordenadas[0] = 5 generará un error

# Desempaquetado
nombre, edad = ("Alice", 25)
print(nombre)
print(edad)

# Tuplas en una Función de Retorno Múltiple
def obtener_coordenadas():
    x = 3
    y = 5
    return x, y 

coordenada_x, coordenada_y = obtener_coordenadas()
print("Coordenada X: ", coordenada_x)
print("Coordenada Y: ", coordenada_y)

# Creando una lista de tuplas

personas = [("Alice", 25), ("Bob", 30), ("Charlie", 28)]

for nombre, edad in personas:
    print(nombre, "Tiene", edad, "años.")