def saludar(nombre):
    print("Hola", nombre, "Bienvenido a mi curso de Python")

nombre_usuario = "Juan"

saludar(nombre_usuario)

# Funciones con retorno

def suma(a, b):
    resultado = a + b
    return resultado

resultado_suma = suma(5, 3)
print("El resultado de la suma es: ", resultado_suma)

# Cacular área del rectángulo

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
    for i in range(2, int(numero ** 0.5) +1):
        if numero % i == 0:
            return False
    return True

num = int(input("Ingrese un número: "))
if es_primo(num):
    print(num, "es un número primo")
else:
    print(num, "no es un número primo")