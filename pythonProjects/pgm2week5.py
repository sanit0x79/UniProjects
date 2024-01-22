#!/usr/bin/env python3
#def f(x=2, y=11):
 #   return x + 3 * y

# Problem 1

def f(x=2, y=11):
    return x + 3 * y
print(f("Lala", "la"))

''' problem 3
y = 60
x = -6

def f(y=x, x=y):
    return x + 3 * y
print(f(y=x, x=y))
'''

width = 4
s = " ",

for col in range(width):
    s += str(col), " "
