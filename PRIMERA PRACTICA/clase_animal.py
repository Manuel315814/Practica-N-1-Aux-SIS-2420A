# Creamos una clase animal
# Con los siguientes atributos --nombre --edad --imprime sonido
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def emite_sonido(self):
        print("Este animal realiza un sonido")
# CREAMOS LAS TRES CLASES HIJAS
class Perro(Animal):
    def emite_sonido(self):
        print("Guau Guau")

class Gato(Animal):
    def emite_sonido(self):
        print("Miau")

class Pajaro(Animal):
    def emite_sonido(self):
        print("Pío pío")
# Función con polimorfismo
def hacer_emite_sonido(animales: list):
    for animal in animales:
        animal.emite_sonido()

animales = [Perro("ROCKY", 3),Gato("STUARD", 1),Pajaro("PIOLIN", 5)
]
hacer_emite_sonido(animales)

