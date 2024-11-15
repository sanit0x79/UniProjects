def over_hundred(L):
    result = 0
    for i in range(len(L)):
        result = result + L[i]
        if result > 100:
            return True
    return False

test = [12,13,14,23921]
print(over_hundred(test))
