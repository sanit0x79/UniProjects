# A Correct solution

L = [
    ["melk", 0.8, "pond"],
    ["brood", 1.2, "euro"],
    ["pindakaas", 2.1, "euro"],
    ["boter", 1.5, "pond"],
    ["kaas", 3.2, "euro"]
]

#euro = [[x[0], x[1] * 1.1, "euro"] for x in L if x[2] == "pond"]

#print(euro)


# B
euro = []
for x in L:
    if x[2] == "pond":
        euro += [[x[0], x[1] * 1.1, "euro"]]

print(euro)