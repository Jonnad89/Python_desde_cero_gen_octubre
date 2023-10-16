# try:
#     numero = int(input("Ingresa un número: "))
#     division = 10 / numero
# except ZeroDivisionError:
#     print("No se puede dividir por cero.")
# except ValueError:
#     print("Ingresa un número válido.")

# Bloque "else" y "finally"

try: 
    archivo = open("mi_archivo.txt", "r")
    contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no se encontró")
else:
    print("Contenido del archivo:", contenido)
finally:
    archivo.close()