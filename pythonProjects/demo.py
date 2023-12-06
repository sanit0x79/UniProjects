""" lst=[3, 10, 2, 10, -1]
i = 0
while i<len(lst) and lst[i]!=10:
    i+=1
if i<len(lst):
    lst[i] = -10
print(lst) """

i = 1
while (i<101):
    print(i)
    i = i + 5

l = "Hanze"
i = 0
while (i < len(l)):
    print(l[i])
    i += 1

i = 0
l = [5, 20, 30, 2]
while (i<len(l)):
    print(l[i]*2)
    i += 1

i = 0
l = [5, 20, 30, 2]

while (i<len(l) - 1):
    print(l[i] + l[i + 1])
    i += 1


def aantalKlinkers(s):
# 1. resultaat-variabelen maken
    aantalKlinkers = 0
# 2. loop
    for letter in s:
        if letter in 'aeiouyAEIOUY':
            aantalKlinkers += 1
# 3. return
    return aantalKlinkers
print(aantalKlinkers('Ierland'))

def fac_loop(n):

    # 1. Resultaat-variabelen maken
    uitkomst = 1
    # 2. Loop
    for i in range (1, n+1):
        uitkomst *= i
    # 3. Return
    return uitkomst
    
print (fac_loop(5))