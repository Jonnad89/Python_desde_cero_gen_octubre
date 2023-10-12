# Los diccionarios son una poderosa estructura de datos que nos permiten almacenar datos en pares clave-valor.

persona = {
    "nombre" : "Alice",
    "edad" : 25,
    "profesion" : "ingenieria"
}

print(type(persona))
print(persona)

# Acceder a los valores en un diccionario utilizando las clases correspondientes.

nombre = persona["nombre"]
edad = persona["edad"]

print(nombre)
print(edad)

# Podemos agregar nuevos pares clave-valor o modificar valores existentes en un diccionario.

persona["ubicación"] = "Nueva York"
persona["edad"] = 26

print(persona)

# Eliminar un par clave-valor utilizando la palabra clave "del".

del persona["edad"]
print(persona)