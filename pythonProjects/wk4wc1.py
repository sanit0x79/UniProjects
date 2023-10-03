# def driehoek(n):
    # if n == 0:
        # return
    # print("*"*n)
    # driehoek(n-1)

# print(driehoek(5))


# def fac(n):
    # if n == 0:
        # return 1
    # else:
        # return n * fac(n-1)
# print(fac(5))

# def aantalPs(s):
    # if not s:
        # return 0
    # else:
        # return (s[0] == 'P' + aantalPs(s[1:]))
# print(aantalPs('Pannenkoekenpan'))

def aantalPs(s):
    if not s:
        return 0
    if s[0] == 'P':
        aantal = 1
    else:
        aantal = 0
    return aantal + aantalPs(s[1:])
print(aantalPs("PannenkoekenPan"))