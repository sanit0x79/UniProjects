def over_hundred(L):
    result = 0
    for i in L:
        result += i
        if result > 100:
            return True
        return False

lc = [x for x in range(12, 15)]
lc2 = [20,30,40,50]
lc3 = [i for i in range(10,35,5)]
assert over_hundred(lc) == False
assert over_hundred(lc2) == True
assert over_hundred(lc3) == False