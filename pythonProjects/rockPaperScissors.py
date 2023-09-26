from random import choice

user = input("Jouw keus? ")
comp = choice(["steen", "papier", "schaar"])

print(user)
print(comp)

if comp == user:
    print("Gelijkspel... ")
else:
    if comp == "steen":
        if user == "schaar":
            print("Ik win!")
        else:
            print("Jij Wint!")
    else:
        if comp == "papier":
            if user == "steen":
                print("Ik Win!")
            else:
                print("Jij wint!")
if comp == user:
    print("Gelijkspel...")
elif: comp == "steen" or comp == "papier":
    
