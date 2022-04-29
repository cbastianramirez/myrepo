#print("Hola", "jei", sep=' * ', end=' - ', flush=False)
#print(25%13)
#anything = input("Tell me anything...")
#print("Hmm...", anything, "... Really?")
#print(type(anything))
#y = 33%24 
#print(y)

"""
a = input("Ingrese su nombre: ")
for x in a:
    if x == "a" or x == "A":
        print("--> Hay una \"a\"")
    else:
        print("No es una \"a\"")

-------------------------------

one = int(input("Enter number 1: "))
two = int(input("Enter number 2: "))
three = int(input("Enter number 3: "))

if one > two and one > three :
    greatest = one
if three > two and three > one:
    greatest = three
if two > one and two > three:
    greatest = two

greatest = max(one, two, three)
print("Greatest number is: ", greatest, ";-)")

-----------------------------

x = "si"
while x == "si" or x == "SI" or x == "Si" or x == "sI":
    name = input("Ingrese su nombre: ")
    print("Hola ", name)
    x = input("Desea continuar? ")

-----------------------------------------------------------
x = input("What's ur favourite plant? ")

while x != "":

    if x == "Spathiphyllum":
        print("Yes - Spathiphyllum is the best plant ever!")
    elif x == "spathiphyllum":
        print("No, I want a big Spathiphyllum!")
    elif x == "salir":
        quit("Adios")
    else:
        print("Spathiphyllum! Not ",x,"!")
    x = input("What's ur favourite plant? ")



#----------------------------------------TAX calculator
income = float(input("Enter the annual income: "))

if income > 0 and income <= 85528:
    tax = ((income*0.18)-556.2)
    if tax <= 0:
        tax = 0.0
elif income > 85528:
    tax = (14839.2+((income-85528)*0.32))
elif income < 0:
    tax = 0.0
tax = round(tax, 0)
print("The tax is:", tax, "thalers")


#-----------------------------Leap year or not
year = int(input("Enter a year: "))

if year < 1582:
    print("Not within the Gregorian calendar period")
elif year%4 != 0:
    print("It's a common year")
elif year%4 == 0 and year%100 != 0:
    print("It's a leap year")
elif year%4 == 0 and year%400 != 0:
    print("It's a common year")
else:
    print("It's a leap year")


word = input("Enter a word: ")

while word != "chupacabra":
    if word == "chupacabra":
        break
    else:
        word = input("Enter a word: ")
print("You've successfully left the loop.")


user_word = input("Enter a word: ")
user_word = user_word.upper()

for letter in user_word:
    if letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
        continue
    else:
        print(letter)

#----------------------------------------------------------
word_without_vowels = ""
user_word = input("Enter a word: ")
user_word = user_word.upper()


for letter in user_word:
    if letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
        continue
    word_without_vowels = word_without_vowels + letter
print(word_without_vowels)


#-------------Collatz's hypothesis
c0 = int(input("Enter a positive integer to evaluate: "))
steps = 0

while c0 > 0:
    if c0%2 == 0:
        c0 = c0//2
        print(c0)
        steps += 1
    if c0 == 1:
        break
    if c0%2 != 0:
        c0 = (3*c0)+1
        print(c0)
        steps += 1
if c0 <= 0:
    print("Not a valid number, number>0")
else:
    print(f"Steps= {steps}")

#_____________________________________________________


def sum(a, b):
    print(a+b)

sum(int(input("1 numero: ")), int(input("2 numero: ")))


nombre = "sebas"
edad = 35
ciudad = "Bello"
print("Hola mi nombre es {}, tengo {} años y vivo en la ciudad de {}".format(nombre, edad, ciudad))


#----------------------------------------
a = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

import collections
print([item for item, count in collections.Counter(a).items() if count > 1])

#------------------------------------------

mmy_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list = []


for i in my_list:
    if my_list[i] not in new_list:
        new_list.append(my_list[i])
my_list = new_list[:]
print("The list with unique elements only:")
print(my_list)

------------------------------Eval
a = eval("2+3")
print(a)

#___________________________ test class
class persona:
    def __init__(self, name, lastName, year):
        self.name = name
        self.lastName = lastName
        self.year = year
    
    def mostrar(self):
        print("Hola soy {} {} y tengo {} años.".format(self.name, self.lastName, (2022-self.year)))

persona1 = persona((input("Nombre: ")),(input("Apellido: ")),(int(input("Año nacimiento: "))))
persona1.mostrar()

#______________calculo interes invserion
class calcular:
    def __init__(self, inversion, meses):
        self.inversion = inversion
        self.meses = meses
        
    def calculoInteres(self):
        total = self.inversion + (self.inversion * (((15/100)/12)*self.meses))
        print(total)

resultado = calcular(int(input("Cuanto va a invertir? ")), int(input("A cuanto tiempo? ")))
resultado.calculoInteres()


#_______________descuento compra por color bolita
import random

bolitas = ["blanca", "amarilla", "azul", "roja", "verde"]
bolita = random.choice(bolitas)
print("Sacaste bolita color: {}".format(bolita))
valorCompra = (int(input("Valor de compra: ")))

if bolita == "blanca":
    aPagar = valorCompra-(valorCompra*1)
elif bolita == "amarilla":
    aPagar = valorCompra-(valorCompra*0.9)
elif bolita == "amarilla":
    aPagar = valorCompra-(valorCompra*0.75)
elif bolita == "azul":
    aPagar = valorCompra-(valorCompra*0.5)
elif bolita == "roja":
    aPagar = valorCompra-(valorCompra*0)

print("Total a pagar: $", aPagar)



#_______________GUI tkinter
import tkinter
import _tkinter

HEIGHT = 700
WIDTH = 800

root = tkinter.Tk()

canvas = tkinter.Canvas(root, height = HEIGHT, width=WIDTH)
canvas.pack()

frame = tkinter.Frame(root, bg='red')
frame.pack()

root.mainloop()
"""
import random
from re import X 
class guessNumber:
    def __init__(self, b, n):
        self.b = b
        self.n = n
    
    def guess(self):
        attempts = 0
        #print(self.b)
        while self.n != self.b:
            if self.n <= 0 or self.n > 100:
                print("¡Te saliste del intervalo!")
            elif self.n > self.b:
                print("¡Ups! Te pasaste")
                attempts += 1
            elif self.n < self.b:
                print("¡Ups! Estás por debajo!")
                attempts += 1
            self.n = int(input("Ingrese un número: "))
        print(f"¡LO LOGRASTE! Usaste {attempts+1} intentos")

play = guessNumber((random.randint(0,100)),(int(input("Ingrese un número: "))))
play.guess()

"""
#______suma numeros
z=0
for x in range(1,6):
    z += x
print(z)

x=0
z=0
while x < 3:
    x=x+1
    z += x
    print(z)

"""