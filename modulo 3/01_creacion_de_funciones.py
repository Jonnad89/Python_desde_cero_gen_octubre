"""
def saludar(nombre):
    print("Hola", nombre, "bienvenido a mi curso de Python")

nombre_usuario = "Juan"

saludar(nombre_usuario)


def suma(a, b):
    resultado = a + b
    return resultado

resultado_suma = suma(5,3)
print("El resultado de la suma es: ", resultado_suma)


# Calcular área del rectángulo

def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area

base_rectangulo = 5
altura_rectangulo = 3
area_resultado = calcular_area_rectangulo(base_rectangulo, altura_rectangulo)
print("El área del rectángulo es: ", area_resultado)


# Verificar si un número es primo

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

num = int(input("Ingresa un número: "))
if es_primo(num):
    print(num, "es un número primo")
else:
    print(num, "no es un número primo")    
 

# Conversión de grados Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

grados_celsius = 30
grados_fahrenheit = celsius_a_fahrenheit(grados_celsius)
print(grados_celsius, "grados Celsius son equivalente a", grados_fahrenheit, "grados Fahrenheit")


# Cálculo del factorial de un número

def calcular_factorial(numero):
    factorial = 1 
    for i in range(1, numero + 1):
        factorial *= i
    return factorial

num = 5
factorial_resultado = calcular_factorial(num)
print("El factorial de", num, "es: ", factorial_resultado)
"""

# Verificación de un palíndromo
def es_palindromo(cadena):
    cadena = cadena.lower().replace(" ", "")
    return cadena == cadena[::-1]

texto = "Anita lava la tina"
if es_palindromo(texto):
    print("El texto es un palíndromo")
else:
    print("El texto no es un palíndromo")