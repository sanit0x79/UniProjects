i = 1
while i < 96:
    i = i + 5
    print(i)

j = 0
string = "Hanze"
while j < len(string):
    print (string[j])
    j += 1  


counter = 0
tel = 0
inp = 0
while inp >= 0:
    counter += 1
    inp = int(input("Geef positief getal: "))
    print(f"Getallen Gegeven: {counter}")
    tel += inp 
print(f"Getallen opgeteld: {tel}")