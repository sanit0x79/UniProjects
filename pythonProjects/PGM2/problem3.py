
L = []
inp = 0

while inp >= 0:
    inp = int(input("Geef positief getal: "))

    if inp >= 0:
        L += [inp]

L_sum = 0
for i in L:
    L_sum += i

print("Numbers given: ", str(len(L)))
print("Numbers summed: ", str(L_sum))
print()