"""
numeros = [1, 2, 3, 4, 5]
nombre = ["Alice", "Bob", "Charlie"]
meclados = [10, "Hola", 3.14, True]

primer_elemento = numeros[0]
print(primer_elemento)

tercer_elemento = numeros[2]
print(tercer_elemento)

print(type(numeros))
print(type(primer_elemento))
print(type(tercer_elemento))
"""

frutas = ["manzana", "banana", "naranja"]
print(frutas)
frutas.append("pera") # Agrega "pera" al final de la lista
print(frutas)
frutas.insert(1, "uva")# Inserta "uva" en la posición 1
print(frutas)
frutas.remove("banana")# Elimina "banana" de la lista
print(frutas)

cuadrados = [x ** 2 for x in range(1,6)]
print(cuadrados)