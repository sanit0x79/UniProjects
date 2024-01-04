#!/usr/bin/env python3

# Greeting the customer
print("Hello! Welcome to the coffee shop!")

# Asking input for name and saving it in a variable
name = input("What is your name?\n")
# Setting value for variable menu and price
menu = ["Black coffee" , "Flat white", "Frappucino"]


print("Hello " + name + ", what would you like to order today?\n" + "We offer the following selection of coffee: " + ", " .join(menu) + ".")

# Asking input for their choice and saving it in a variable
choice = input("")
if choice not in menu:
    print("We do not offer that type of coffee here!")
else:
    if choice == "Frappucino":
        price = 8
        print("Do you want extra whipped cream? ")
        whipped_cream = input("")
        if whipped_cream == "Yes" or whipped_cream == "yes":
            price = 10
        elif whipped_cream == "No" or whipped_cream == "no":
            price = 8
    if choice == "Black coffee":
        price = 3
    if choice == "Flat white":
        price = 5
    print("How many " + choice + " would you like?")


amount = input()
total = price * int(amount)

print("Your total comes out to: €" + str(total))

if amount.isdigit():
    number = int(amount)
    print(amount + " " + choice + " coming right up!")
else:
    print("That is not a valid amount.")
