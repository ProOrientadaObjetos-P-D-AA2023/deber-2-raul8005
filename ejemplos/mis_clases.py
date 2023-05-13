"""

"""

# Crear dos clases en Python
# Usted defina el nombre y los atributos
# Puede usar las mismas clases usadas en Java en los ejemplos estudiados

# clase 01

class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    #def mostrar_datos(self):
     #   print(f"Nombre: {self.nombre}\nEdad: {self.edad}\n")

class Compra:
    def __init__(self, producto, preciop, cantidad):
        self.nombre = producto
        self.precio = preciop
        self.cantidad = cantidad

    def calcular_precio_total(self):
        return self.precio * self.cantidad

