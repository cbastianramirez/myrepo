

import math 
class Operacion:
# Caraceristicas, atributos o propiedades  

# Definicion de méNtodos o funciones
    def __init__(self,valor1, valor2): # Función recibe los valores
        self.v1 = valor1
        self.v2 = valor2

    def sumar(self):
        self.r = self.v1 + self.v2

    def restar(self):
        self.r = self.v1 - self.v2

    def multiplicar(self):
        self.r = self.v1 * self.v2

    def dividir(self):
        self.r = self.v1 / self.v2

    def modulo(self):
        self.r = self.v1 % self.v2

    def potencia(self):
        self.r = self.v1 ** 2

    def mostrar(self):
        print(self.r)
    
    def divisionentera(self):
        self.r = self.v1 // self.v2

    def square(self):
        self.r = math.sqrt(self.v1)

# Ingreso de datos o captura desde el teclado
a, b = input("ingrese:").split(",")
a = int(a)
b = int(b)

# Creación de objetos o instancias y acceso a métodos o funciones
s = Operacion(a,b)

s.sumar()
s.mostrar()
s.restar()
s.mostrar()
s.modulo()
s.mostrar()
s.divisionentera()
s.mostrar()
s.dividir()
s.mostrar()
s.square()
s.mostrar()