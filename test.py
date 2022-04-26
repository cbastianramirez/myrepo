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
"""
#___________________________ test class
class persona:
    def __init__(self, name, lastName, year):
        self.name = name
        self.lastName = lastName
        self.year = year
    
persona1 = persona((input("Nombre: ")),(input("Apellido: ")),(int(input("Año nacimiento: "))))
calcAge = 2022 - persona1.year
print("Hola soy {} {} y tengo {} años.".format(persona1.name, persona1.lastName, calcAge))



