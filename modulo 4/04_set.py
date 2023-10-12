# Son una estructura de datos que nos permitirá trabajar con colecciones únicas de elementos.

# Los conjuntos se crean utiliando llaves "{}" o la función "set()" y contienen elementos únicos sin un orden especifico
colores = {"rojo", "verde", "azul"}
numeros = set([1, 2, 3, 4, 5])

# print(type(colores))
# print(type(numeros))

# Los conjuntos en Python permiten realizar operaciones como unión, intersección y diferencia

conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}

union = conjunto_a | conjunto_b
interseccion = conjunto_a & conjunto_b 
diferencia = conjunto_a - conjunto_b

# print(union)
# print(interseccion)
# print(diferencia)

# Podemos verificar si un elemento está presente en un conjunto utilizando la palabra clave "in".

frutas = {"manzana", "banana", "naranja"}

if "manzana" in frutas:
    print("La manzana está en el conjunto de frutas")

def encontrar_numeros_unicos(lista):
    numeros_unicos = set() # Creamos un conjunto vacío para almacenar los números únicos

    for numero in lista:
        if numero not in numeros_unicos:
            numeros_unicos.add(numero) # Agregamos el número al conjunto si no está presente

    return numeros_unicos

# Ejemplo de uso:
numeros = [3, 7, 2, 5, 3, 7, 9, 2, 8, 1]
unicos = encontrar_numeros_unicos(numeros)
print("Números únicos:", unicos)            