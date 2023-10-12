# Creación de tus propios módulos - Fin módulo 3
# Módulos y bibliotecas
# importar un módulo personalizado
"""
import mi_modulo

mi_modulo.saludar("Jonatan")

nombre_usuario = input("Ingresa tu nombre: ")
mi_modulo.saludar(nombre_usuario)

# Calcula la raíz cuadrada utilizando la bibliotaca math
import math

print(math.sqrt(25))

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr.mean()) # Calcula el promedio utilizando la biblioteca NumPy


# importar calculadora
import calculadora

resultado_suma = calculadora.suma(10, 5)
print("Suma: ", resultado_suma)

resultado_resta = calculadora.resta(25, 15)
print("Resta: ", resultado_resta)

resultado_multiplicacion = calculadora.multiplicacion(9,5)
print("Multiplicación: ", resultado_multiplicacion)
"""

from mi_paquete.calculadora.funciones import suma, resta

resultado_suma = suma(25, 50)
print("Suma: ", resultado_suma)

resultado_resta = resta(15, 8)
print("Resta: ", resultado_resta) 