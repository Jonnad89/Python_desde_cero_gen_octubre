# Parámetro con valores predeterminados

def saludar(nombre="amigo"):
    print("Hola",nombre, "bienvenido a la clase")

saludar()

def celsius_a_fehrenheit(celsius):
    fahrenheit = (celsius * 9/5) +32
    return fahrenheit

grados_celsius = 30
grados_fahrenheit = celsius_a_fehrenheit(grados_celsius)
print(grados_celsius, "grados Celsius son equivalentes a", grados_fahrenheit, "grados Fahrenheit")

# Cálculo del factorial de un número

def calcular_factorial(numero):
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return factorial
    
num = 5 
factorial_resultado = calcular_factorial(num)
print("El factorial de ",num, "es :", factorial_resultado)

# Verificación de un palíndromo

def es_palindromo(cadena):
    cadena = cadena.lower().replace(" ", "")
    return cadena == cadena[::-1]

texto = "Anita lava la tina"
if es_palindromo(texto):
    print("El texto es un palíndromo")
else:
    print("El texto no es un palíndromo")

# Uso de *args y kwargs

def mostrar_argumentos(*args, **kwargs):
    print("Argumentos posicionales: ", args)
    print("Argumentos con nombre: ", kwargs)

# LLamado a la función con argumentos posicionales

mostrar_argumentos(1, 2, 3, 4, 5)

# Llamada con argumentos con nombre
mostrar_argumentos(nombre="Juan", edad=25, ciudad="Madrid")

# LLamada con argumentos posicionales y con nombre
mostrar_argumentos(10, 20, nombre="Ana", apellido="Garcia")

# Llamada con argumentos posicionales y con nombre usando *args y **kwargs

argumentos_posicionales = (5, 10, 15)
argumentos_con_nombre = {"nombre" : "Luis", "profesión" : "Ingeniero"}
mostrar_argumentos(*argumentos_posicionales, **argumentos_con_nombre)