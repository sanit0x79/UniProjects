opbrengst_tomaten = 150
opbrengst_paprikas = 120
opbrengst_komkommers = 180
totale_opbrengst = opbrengst_komkommers + opbrengst_tomaten + opbrengst_paprikas

prijs_tomaat = 3.24
prijs_paprika = 2.87
prijs_komkommer = 1.48
totale_omzet = prijs_tomaat * opbrengst_tomaten + prijs_paprika * opbrengst_paprikas + prijs_komkommer * opbrengst_komkommers

print(totale_opbrengst)
print(totale_omzet)
