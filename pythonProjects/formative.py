# 1 foot = 12 inch
# 1 inch = 2.54 cm
# 1 foot = 30,48 cm

# feet = 6
# inches = 3
# inches_to_cm = 2.54
# feet_to_inches = 12

# total_inches = feet * feet_to_inches + inches
# centimeters = total_inches * inches_to_cm

# meters = centimeters // 100
# centimeters %= 100

# print("Lengte : {} meter en {} centimeter".format(meters, centimeters))

# s = 20 # Je kunt hier de gewenste windsnelheid invullen

# if s >= 252:
    # print("Categorie 5")
# elif s >= 209:
    # print("Categorie 4")
# elif s >= 178:
    # print("Categorie 3")
# elif s >= 154:
    # print("Categorie 2")
# elif s >= 119:
    # print("Categorie 1")
# elif s >= 63:
    # print("Tropical Storm")
# else:
    # print("Tropical Depression")



# def remove_double(L):
    # if len(L) == 0:
        # return
    # if L[0] in L:
        # return remove_double(L[:1])
    # return L[0] + remove_double(L[:1])

# assert remove_double([1, 4, 2, 3, 2]) == [1, 4, 3, 2]


def remove_double(L):

    """
Verwijdert dubbele cijfers uit een lijst terwijl de oorspronkelijke volgorde hetzelfde blijft

Parameters: 
L: De invoerlijst

Returns:
De nieuwe lijst zonder dubbele elementen
"""
    if len(L) == 0:
        return L
    elif L[0] in L[1:]:
        return remove_double(L[1:])
    else:
        return [L[0]] + remove_double(L[1:])

# Test de functie
assert remove_double([1, 4, 2, 3, 2]) == [1, 4, 3, 2]



# opgave 4
def check_extensions(s, e):
    #Als string e leeg is, geeft true terug
    if not e:
        return True
    
    if not s:
        return False
    
    if e[-1] !=s [-1]:
        return False
     
    
    return check_extensions(s[:-1], e[:-1])
    
# opgave 5


def all_even(L):
    if not L:
        return True
    if L[0] % 2 == 0:
        return all_even(L[1:])
    else:
        return False


# opgave 6

# Controleer op de basecase lengte van s gelijk aan 0. in dat geval retourneer resultaat True
# Controleer op de tweede basecase lengte van g gelijk aan 0. In dat geval retourneer resultaat True

# In de recursive case: controleer of de eerste letters van G en s overeen komen.
# Zo nee, retourneer dan False.
# Zo ja, roep dan starts_with nogmaals met g en s zonder eerste letter en retourneer dat resultaat

# opgave 6-b

def starts_with(g, s):
    if not g:
        return True
    if not s:
        return False
    if s[0] == g[0]:
        return starts_with(g[1:], s[1:])
    else:
        return False
        
        
def greetings(s):
    if starts_with("hello", s):
        return 0
    if starts_with("h", s):
        return 20
    return 100 # anders
