# Only returns the names that have 3 letters out of the list
names = ["Mark", "Pete", "Jacob", "Mary", "Mae"]

def onlyThreeLetters(l):
    if not l:
        return []  # empty list
    elif len(l[0]) == 3:
        return [l[0]] + onlyThreeLetters(l[1:])
    else:
        return onlyThreeLetters(l[1:])

result = onlyThreeLetters(names)
print(result)
