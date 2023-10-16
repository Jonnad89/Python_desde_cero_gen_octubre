class MiErrorValueError(ValueError):
    def __init__(self, valor):
        mensaje = f"Se produjo un error de valor: {valor}"
        super().__init__(mensaje)

try:
    nota = int(input("Ingresa tu nota: "))
    if nota < 0 or nota > 100:
        raise MiErrorValueError(nota)
    else:
        print("Todo ha salido correctamente y estás aprobado")
except MiErrorValueError as error:
    print(error)