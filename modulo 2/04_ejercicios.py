# numero = int(input("Ingresa un número: "))

# if numero % 2 == 0:
#     print(numero, "Es un número par.")
# else: 
#     print(numero, "Es un número impar.")

# numero = int(input("ingresa un número: "))

# for i in range(1,11):
#     resultado = numero * i
#     print(numero, "x", i, "=", resultado)

def calcular_promedio(lista):
    suma = sum(lista)
    promedio = suma / len(lista)
    return promedio
numero = [5, 8, 12, 3, 10]
promedio_resultado = calcular_promedio(numero)
print("El promedio de la lista es: ", promedio_resultado)