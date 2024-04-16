L = [1, 42, 2, 3, 42, 5]
f
# recursive function

def count_42(l):
    # base case
    if len(l) == 0:
        return 0
    # recursive case
    if l[0] == 42:
        return 1 + count_42(l[1:])
    else:
        return count_42(l[1:])


assert count_42(L) == 2

# list comprehension

M = [x for x in L if x == 42]
total = sum(M)

M =[int(x == 42) for x in L]
total = sum(M)

m = [1 for x in L if x == 42]
total = sum(m)

assert total == 2

# for

def count_42_i(L):
    total = 0

    for x in L:
        if x == 42:
            total = total + 1

# while
l = [2, 42, 3]
total = 0
length = len(L)

while length > 0:
    if L[length - 1] == 42:
        total = total + 1
    length = length - 1

assert total == 1