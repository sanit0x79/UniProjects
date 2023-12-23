
"""
def calculate_product(L):
    if len(L) == 0:
        return 0
    else:
        return L * calculate_product(L[0:])
"""
# A Edit this code so that it works
def calculate_product(L):
    if len(L) == 0:
        return 1
    else:
        return L[0] * calculate_product(L[1:])
# B Voeg een docstring toe aan de functie, waarin je beschrijft wat de functie 
# doet en de parameter die het accepteert. Neem hier de code van vraag a over en vul het aan
def calculate_product(L):
    """
    Geeft het product van alle getallen in een lijst terug.
    Parameter: Een lijst van integers
    Out: Integer
    """
    if len(L) == 0:
        return 1
    else:
        return L[0] * calculate_product(L[1:])
# C Voeg drie extra assertions toe om de functie te testen. Het is voldoende om hier alleen de assertions
# te schrijven
assert calculate_product ([3, 4, 5]) == 60
assert calculate_product ([1, 1, 1]) == 3
assert calculate_product ([3, 4, 5]) == 60
# etc.
