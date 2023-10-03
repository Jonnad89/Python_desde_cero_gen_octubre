# Este es un comentario de una sola línea
print("Hola, mundo") # También puedo agregar comentarios al final del código

"""
Este es un comentario
de varias líneas.
Puede abarcar varias líneas 
sin necesidad de usar el "#" en cada línea.
"""
print("Hola, mundo")
"""
    # Cálculo del área de un triángulo
    area = (base * altura) / 2
    return area
"""

texto_largo = "Este es un texto muy largo que excede el límite de 79 carácteres"
print(texto_largo)

texto_largo = ("Este es un texto largo que se divide usando paréntesis para mejorar la legibilidad") 
print(texto_largo)

def funcion1():
    #código de la función

def funcion2():
    #código de la función

def calcular_area(base, altura):
    """
    Función para calcular el área de un triángulo

Parámetros:
base (float): La base del triángulo.
atura (float): La altura del triángulo.

Retorna:
float: El área del triángulo
    """

    area = ( base * altura) / 2
    return area

# Usar mayúsculas para nombres de constantes:

PI = 3.14159
GRAEDAD = 9.81

# Evitar comentarios innecesarios y explicar solo lo necesario:
numero = 10
# La siguiente línea suma 5 al número (ESTO NO LO HAGAN)
resultado = numero + 5

# Comentarios claros y concisos:
# Calcular el promedio de una lista de números

def calcular_promedio(lista):
    # Código para calcular el promedio


# Alinear elementos en listas o diccionarios para mejorar la lebibilidad:

lista_numeros = [
    1, 2, 3, 
    4, 5, 6
]

diccionario_datos = {
    "nombre" : "Juan",
    "edad" : 30,
    "ciudad" : "Madrid",
}