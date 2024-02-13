# A Schrijf de functie transform(c) die een enkele letter c accepteerd en transformeert naar zijn leet waarde
# Write a function transform(c) that transforms a singular letter c to its l33t equivalent
def transform (c):
    if c == "a":
        return "4"
    if c == "b":
        return "8"
    if c == "e":
        return "3"
    
# B De functie translate zal met behulp van de functie transform een string letter voor letter moet omzetten naar leet
# Beschrijf hoe je een recursief algoritme kan gebruiken om de functie translate te schrijven
"""
Base Case:
als de string leeg is, geef lege string terug

Recursie Case:
Eerste letter transformeren met de transform functie en plak daaraan de rest van de string die weer de functie ingaat.
"""

# C Schrijf de functie translate(w) die als parameter een string w accepteert. Deze functie zal het woord w vertalen
# naar leet zoals je zojuist hebt bedacht
# maak gebruik van hulpfunctie transform(c)
# Write the function translate(w) that takes string w and uses function transform(c) to convert the string into l33t
def transform (c):
    if c == "a":
        return "4"
    if c == "b":
        return "8"
    if c == "e":
        return "3"

def translate(W):
    if W == "":
        return ""
    else:
        return transform(W[0]) + translate(W[1:])
