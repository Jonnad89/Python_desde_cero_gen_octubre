numeros = [1, 2, 3, 4, 5]
nombres = ["Alice", "Bob", "Charlie"]
mezclados = [10, "Hola", 3.14, True]

primer_elemento = numeros[0] # Resultado: 1
tercer_elemento = numeros[2] # Resultado: 3

#print(type(numeros))

frutas = ["manzana", "banana", "naranja "]
print(frutas)
frutas.append("mango") # Agrega "mango" al final
print(frutas)
frutas.insert(1, "uva") # Inserta "uva" en la posición 1
print(frutas)
frutas.remove("banana") # Elimina "banana" de la lista
print(frutas)

cuadrados = [x ** 2 for x in range(1,6)]
print(cuadrados)