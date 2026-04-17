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
print("Welcome to the tip calculator")
totalBill = float((input("What was the total bill? $")))
tip = float(input("How much tip would you like to give? 10, 12,or 15? $"))
people = float(input("How many people are there to share the bill? "))
eachPerson = (totalBill + tip) / people

print(f"Each person should pay: ${round(eachPerson, 2)}")






