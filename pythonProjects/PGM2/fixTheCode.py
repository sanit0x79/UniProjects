def over_hundred(L):
    result = 0
    for i in L:
        result += i
        if result > 100:
            return True
    return False

lc = [x for x in range(12, 15)]
print(over_hundred(lc))

assert over_hundred([123,12,13,4]) == True
assert over_hundred([12, 80, 7]) == False