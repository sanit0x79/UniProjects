#Schrijf onderstaande functies. Gebruik naar keuze recursie, listcomprehension, for-loop of while-loop.
#1. hoogsteTotaalBuren(l) - Geef het hoogste totaal van twee naast elkaar gelegen waardes in een lijst getallen. Als de lijst minder dan 2 elementen bevat, retourneer dan None.
#hoogsteTotaalBuren([4, -3, 20, 10, -1]) -> 30 (totalen van buren: 1, 17, 30, 9)
#hoogsteTotaalBuren([1, 0]) -> 1
#hoogsteTotaalBuren([7, 7, 7]) -> 14
#hoogsteTotaalBuren([1]) -> None (want er zijn geen buren) 

L = [1238,1244,123123,123121]

def hoogsteTotaalBuren(L):
    if len(L) < 2:
        return None
    totalen = [L[i] + L[i+1] for i in range(len(L) - 1)]

    return max(totalen)

print(hoogsteTotaalBuren(L))


# verdubbelTot20(l) - Verdubbel alle elementen van een lijst getallen, totdat 20 is bereikt. Deze functie wijzigt l en geeft True terug als 20 is bereikt, of False als 20 niet voorkomt. 
l = [123,20,23,20]

def verdubbelTot20(l):
        l = [num * 2 for num in l]
        if not [num for num in l if num < 20]:
            return True
        if not [num for num in l if num >= 20]:
            return False

print(verdubbelTot20(l))
print(l)

#b. Schrijf de functie aantalNamenMetLetterKlistcomprehension(namenlijst)
namenlijst= ["jan", "kees", "mike", "karel"]

lc = sum([1 for naam in namenlijst if 'k' in naam or 'K' in naam])

print(f"Er zijn {lc} namen waar tenminste 1 k in zit")


# a. Geef een lijst namen waarvoor geldt dat zij 3 punten of minder hebben behaald.  
scores = [["Jan", 3], ["Els", 10], ["Erik",7], ["Akke",2], ["Otto",1], ["Henk", 10], ["Mona",2], ["Karel",7]]

lc1 = [x for x in scores if x[1] <= 3]

print(f"{lc1}")

# b. Bereken met behulp van een listcomprehension (en de functies sum() en len()) de gemiddelde score van de deelnemers
def findAverage(scores):
     avg = sum([score[1] for score in scores])
     return avg / len(scores)

print(findAverage(scores))


#c. De winnaar van het spel is degene met de meeste punten. Het is mogelijk dat er meerdere personen zijn die de meeste punten hebben behaald. In dat geval zijn er meerdere winnaars.
#Geef een lijst namen van de winnaar(s). Doe dit met behulp van twee listcomprehensions en de max()-functie. 
#Sorteer-functies zijn niet toegestaan (en in dit geval ook niet heel handig).

# iterate over the list and see who has the most points, if they have more points than the previous person, they are the current winner
    # if x > previous, he is winner for now
# return names of winners and their scores, return x

lc2 = max(score[1] for score in scores)
lc3 = [score[0] for score in scores if score[1] == lc2]

print(lc3)

