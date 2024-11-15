count = 0   # bijhouden hoeveel getallen er zijn ingevuld
som = 0 # bijhouden de waarde van de getallen
inp = int(input("Geef positief getal: "))   # vragen om input
while inp >= 0:  # Blijf herhalen zolang de input positief is,
    count = count + 1   #counter verhogen
    som = som + inp # nieuwe input optellen
    inp = int(input("Geef positief getal: "))   # vraag voor nieuwe input
print("som", som, 'aantal', count) # print resultaat
