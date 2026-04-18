#userName = input("Enter your name: ")

#length = len(userName)
#print(length)

#print("Welcome to Band Name Generator")
#grewUpCity = input("What is the city you grew up from?\n")
#petName = input("What is your pet name?\n")
#combinedName = grewUpCity + " " + petName
#print("Your Band Name is "+combinedName)

#print(type("Hello"))
#print(type(12.5))
#print(type(True))

#Building a Tip Calculator
"""
print("Welcome to the tip calculator")
totalBill = float((input("What was the total bill? $")))
tip = int(input("How much tip would you like to give? 10, 12,or 15? ")) /100
people = int(input("How many people are there to share the bill? "))
tipToPay = totalBill * tip
eachPerson = (totalBill + tipToPay) / people

print(f"Each person should pay: ${round(eachPerson, 2)}")


checkNumber = int(input("Enter a number to check if it is an even or odd number: "))
if checkNumber % 2 == 0:
    print(f"{checkNumber} is an even number.")
else:
    print(f"{checkNumber} is an odd number.")

"""


pizzaAmount= 0

print("Welcome to PizzaSquare")
size = input("What size pizza do you want? S, M, or L: ")
if size == "S":
    pizzaAmount += 15
elif size == "M":
    pizzaAmount += 20
elif size == "L":
    pizzaAmount += 25
else:
    print("Invalid input.")

pepperoni = input("Do you want pepperoni on your Pizza? (y/n): ")
if pepperoni == "y":
    if size == "S":
        pizzaAmount += 2
    else:
        pizzaAmount += 3

extraCheese =input("How many extra cheese do you want?: y/n ")
if extraCheese == "y":
    pizzaAmount += 1
print(f"Your total bill is ${round(pizzaAmount, 2)}")





