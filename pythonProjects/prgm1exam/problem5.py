# A Beschrijf in eigen woorden met welke strategie zij dit probleem kunnen oplossen
"""
Dief krijgt een beker.
Als de beker leeg is fluistert hij 0 naar linker buur
And pakt hij een nummer en geeft de rest van de beker aan de rechterbuur
Wacht op het antwoord van de buur.
Als de dief wel een 42 heeft getrokken, dan telt hij 1 op bij het getal dat hij van de buur kreeg en fluistert
dat resultaat naar zijn linkerbuur
Als de dief niet 42 heeft getrokken, dan fluistert het gekregen getal naar zijn linkerbuur.
"""

# B Schrijf de functie count_42(L) die een lijst L als parameter accepteert en het aantal keer dat 42 zich in de 
# lijst bevindt als resultaat teruggeeft.

def count_42(L):
    if len(L) == 0:
        return 0
    ik = L[0]
    buur = count_42(L[1:])
    if ik == 42:
        return 1 + buur
    else:
        return buur
