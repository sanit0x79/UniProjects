#!/usr/bin/env python3

print("Hello! Welcome to the coffee shop!")

name = input("What is your name?\n")
menu = ("Black coffee, Flat White")
print("Hello " + name + ", what would you like to order today?\n" + "We offer the following selection of items: " + menu)

choice = input("")
if choice != "Black coffee" and choice != "Flat White":
    print("We do not offer that type of coffee here.")
elif choice == "Black coffee" or choice == "Flat White":
    print("Your " + choice + " is coming right up " + name + "!")
