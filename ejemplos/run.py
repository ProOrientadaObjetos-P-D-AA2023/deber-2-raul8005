"""

"""
# Crear dos objetos de la clase 01

#import mis_clases.py
# objeto 01
#objeto = mi_clase.py.MiClase.py()
# crear
from mis_clases.py import Persona

from mis_clases.py import Compra

# crear ingresando valores por teclado
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")

Persona = Persona(nombre, edad)
# Presentar objeto; usar el método __st__
def __init__(self, nombre, edad):
    self.valor = nombre
    self.valor = edad

def __str__(self):
    return f"Datos persona: {self.valor, nombre, edad}"


# Presentar objeto
producto = input("Ingrese el producto que va a comprar :" )
preciop = input("Ingrese el valor del producto que va a comprar :" )
cantidad = input("Ingrese la cantidad de productos que va a comprar: ")

compra = Compra(producto, preciop, cantidad)
precio_total = compra.calcular_precio_total()
print(f"Precio total del producto: ${precio_total}")






