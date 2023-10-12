class Coche:
    cantidad_ruedas = 4 # Atributo de clase

    def __init__(self, marca, modelo):
        self.marca = marca # Atributo de instancia
        self.modelo = modelo # Atributo de instancia

    @classmethod
    def cambiar_ruedas(cls, cantidad):
        cls.cantidad_ruedas = cantidad  

    def persentase(self):
        return f"Soy un {self.marca} {self.modelo} con {self.cantidad_ruedas} ruedas"
    
# Creación de objetos:
coche1 = Coche("Toyota", "Corolla")
coche2 = Coche("Ford", "Mustang")

print(coche1.persentase())
print(coche2.persentase())

# Camio de cantidad de ruedas usando método de clase

Coche.cambiar_ruedas(6)

print(coche1.persentase())
print(coche2.persentase())