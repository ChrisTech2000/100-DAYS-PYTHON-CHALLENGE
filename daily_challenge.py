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

extraCheese =input("How much extra cheese do you want?: y/n ")
if extraCheese == "y":
    pizzaAmount += 1
print(f"Your total bill is ${round(pizzaAmount, 2)}")


print("Welcome to Treasure Island \nYour mission is to find the treasure")
leftOrRight = input("Which side do you want? (left, or right): ").upper()
if leftOrRight == "left":
    swimOrWait = input("Which one do you want? (swim or wait): ")
    if swimOrWait == "wait":
        whichDoorColor = input("Which door color do you want? (red, yellow or blue): ")
        if whichDoorColor == "yellow":
            print("You win! Congratulations")
        else:
            print("You loose! You lose")
    else:
        print("You can't do that, game over")
else:
    print("Gosh, game over")



#import script

#rand_number = random.randint(1, 100)

#print(rand_number)

#print(script.my_number)

random_number = random.randint(0, 1)
if random_number == 0:
    print("Tail")
else:
    print("Head")

"""


import random

# list_of_friends = ["Sam", "Mikee", "Max", "Dozie", "Chris"]
# random_number = random.randint(0, 4)
# if random_number == 0:
#     print(list_of_friends[0])
# elif random_number == 1:
#     print(list_of_friends[1])
# elif random_number == 2:
#     print(list_of_friends[2])
# elif random_number == 3:
#     print(list_of_friends[3])
# else:
#     print(list_of_friends[4])

# print(list_of_friends[random_number])
#
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# fruits[-1] = "Melons"
# fruits.append("Lemons")
# print(fruits)
#
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
#
# dirty_dozen = [fruits, vegetables]
#
# print(dirty_dozen[0][0])


#Rock Paper Scissors Project

# choices = ["Rock", "Paper", "Scissor"]
# print("--Welcome to Rock Paper Scissor Game--")
# user_input = input("Select 0 for Rock, 1 for Paper, 2 for Scissor: ").strip()
#
# if user_input not in ("0", "1", "2"):
#     print("Invalid input. Put either 0 for Rock, 1 for Paper, 2 for Scissor.")
#
# else:
#     user_index = int(user_input)
#     user_choices = choices[user_index]
#
#
#     computer_choice = random.choice(choices)
#     print(f"\nYou chose: {user_choices.capitalize()}")
#     print(f"Computer chose: {computer_choice.capitalize()}")
#
#     if user_choices == computer_choice:
#         print("It's a tie!")
#     elif user_choices == "Rock" and computer_choice == "Scissor":
#         print("You win!, Rock breaks scissor")
#     elif user_choices == "Paper" and computer_choice == "Rock":
#         print("You win!, Paper covers rock")
#     elif user_choices == "Scissor" and computer_choice == "Paper":
#         print("You win!, Scissor cut paper")
#     else:
#         print("You lose, the computer wins this time")

# sum_of_number = 0
# for number in range(1, 101):
#     sum_of_number += number
# print(sum_of_number)


# for number in range(1, 101):
#     if number % 3 == 0 and number % 5==0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print ("Buzz")
#     else:
#         print(number)

#Password Generator
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E","F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to Password Generator")
number_of_letters = int(input("How many letters do you want to include in your password?: "))
number_of_symbols = int(input("How many symbols do you want to include in your password?: "))
number_of_numbers = int(input("How many numbers do you want to include in your password?: "))

# password = ""
# for char in range(1, number_of_letters + 1):
#     password += random.choice(letters)
#     # print(password)
# for char2 in range(1, number_of_symbols + 1):
#         password += random.choice(symbols)
#         # print(password)
# for char3 in range(1, number_of_numbers + 1):
#         password += random.choice(numbers)
# print(password)

#To be reshuffling it after generation so hackers cannot predict

password_list = []
for char in range(1, number_of_letters + 1):
    password_list.append(random.choice(letters))
    # print(password)
for char2 in range(1, number_of_symbols + 1):
        password_list.append(random.choice(symbols))
        # print(password)
for char3 in range(1, number_of_numbers + 1):
        password_list.append(random.choice(numbers))
#You can then change the order of the password in the list using random.shuffle
random.shuffle(password_list)
password = "".join(password_list)
print(password)





