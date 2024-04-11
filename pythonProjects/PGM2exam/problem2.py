def find_max_even(L):
    max_even = 1
    for x in L:
        if x > max_even and x % 2 == 0:
            max_even = x
    return max_even

lc = [x for x in range(12, 15)]
print(find_max_even(lc))

assert find_max_even(lc) == 14
assert find_max_even([1, 3, 10, 9]) == 10