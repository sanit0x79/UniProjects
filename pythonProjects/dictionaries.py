#!/usr/bin/env python3

import csv

with open("cijfers.csv") as file:
    reader = csv.DictReader(file)

    totaal = 0
    aantal = 0

    for row in reader:
#        print(row["cijfers"])

        totaal += float(row["cijfers"])
        aantal += 1

    print("Gemiddeld Cijfer", totaal / aantal)
