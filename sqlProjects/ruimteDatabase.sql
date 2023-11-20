Vraag 1:
Schrijf een query om de namen van hemelobjecten op te halen die zowel als moederobject fungeren voor andere hemelobjecten als zelf een satelliet zijn van een ander hemelobject.

Antwoord:
SELECT DISTINCT h1.naam
FROM Hemelobject h1
WHERE h1.naam IN (SELECT moederobject FROM Hemelobject WHERE moederobject IS NOT NULL)
  AND h1.naam IN (SELECT DISTINCT moederobject FROM Hemelobject WHERE moederobject IS NOT NULL);
Vraag 2:
Bereken het gemiddelde aantal verblijfsdagen per hemelobject. Toon alleen hemelobjecten waarbij het gemiddelde aantal verblijfsdagen meer dan 5 dagen is.

Antwoord:
SELECT h.naam, AVG(b.verblijfsduur) AS gemiddeld_verblijf
FROM Hemelobject h
JOIN Bezoek b ON h.naam = b.hemelobject
GROUP BY h.naam
HAVING AVG(b.verblijfsduur) > 5;
Vraag 3:
Vind alle klanten die hebben deelgenomen aan minstens twee reizen waarvan de vertrekdatums binnen dezelfde maand vallen. Toon de klantnummers en namen.

Antwoord:
SELECT k.nr, k.naam
FROM Klant k
JOIN Deelname d ON k.nr = d.klant
JOIN Reis r1 ON d.reis = r1.nr
JOIN Reis r2 ON k.nr = d.klant AND r1.nr <> r2.nr
WHERE EXTRACT(MONTH FROM r1.vertrekdatum) = EXTRACT(MONTH FROM r2.vertrekdatum);
Vraag 4:
Update de prijs van alle reizen die meer dan 15 dagen duren met 10% verhoging.

Antwoord:
UPDATE Reis
SET prijs = prijs * 1.10
WHERE duur > 15;
Vraag 5:
Bereken het totale aantal verblijfsdagen voor elke hemelobjectnaam en toon de resultaten gesorteerd op totaal verblijfsdagen in aflopende volgorde.

Antwoord:
SELECT h.naam, SUM(b.verblijfsduur) AS totaal_verblijfsdagen
FROM Hemelobject h
LEFT JOIN Bezoek b ON h.naam = b.hemelobject
GROUP BY h.naam
ORDER BY totaal_verblijfsdagen DESC;

Vraag 6:
Selecteer de namen van klanten die hebben deelgenomen aan minstens één reis naar een hemelobject met een diameter groter dan 5000 kilometer.

Antwoord:
SELECT DISTINCT k.naam
FROM Klant k
JOIN Deelname d ON k.nr = d.klant
JOIN Reis r ON d.reis = r.nr
JOIN Bezoek b ON r.nr = b.reis
JOIN Hemelobject h ON b.hemelobject = h.naam
WHERE h.diameter > 5000;
Vraag 7:

Bereken het gemiddelde aantal deelnames per klant. Toon alleen klanten waarvan het gemiddelde aantal deelnames meer dan 2 is.

Antwoord:
SELECT k.nr, k.naam, AVG(deelnames_per_klant) AS gemiddelde_deelnames
FROM Klant k
LEFT JOIN (SELECT klant, COUNT(reis) AS deelnames_per_klant FROM Deelname GROUP BY klant) d
ON k.nr = d.klant
GROUP BY k.nr, k.naam
HAVING AVG(deelnames_per_klant) > 2;
Vraag 8:
Vind alle hemelobjecten die niet zijn bezocht tijdens reizen. Toon de namen van deze hemelobjecten.

Antwoord:
SELECT h.naam
FROM Hemelobject h
LEFT JOIN Bezoek b ON h.naam = b.hemelobject
WHERE b.hemelobject IS NULL;
Vraag 9:
Bereken het aantal unieke klanten dat heeft deelgenomen aan reizen met een prijs hoger dan het gemiddelde van alle reizen.

Antwoord:
SELECT COUNT(DISTINCT k.nr) AS aantal_unieke_klanten
FROM Klant k
JOIN Deelname d ON k.nr = d.klant
JOIN Reis r ON d.reis = r.nr
WHERE r.prijs > (SELECT AVG(prijs) FROM Reis);
Vraag 10:
Update de geboortedatum van een specifieke klant (bijvoorbeeld klantnummer 2) naar een nieuwe datum (bijvoorbeeld '1990-05-15').

Antwoord:
UPDATE Klant
SET geboortedatum = '1990-05-15'
WHERE nr = 2;
Vraag 11:
Verwijder alle reizen waarvoor geen bezoeken zijn geregistreerd.

Antwoord:
DELETE FROM Reis
WHERE nr NOT IN (SELECT DISTINCT reis FROM Bezoek);
Vraag 12:
Vind het hemelobject met de kleinste afstand tot een moederobject. Toon de naam van het hemelobject en de bijbehorende afstand.

Antwoord:
SELECT h.naam, h.afstand
FROM Hemelobject h
WHERE h.afstand = (SELECT MIN(afstand) FROM Hemelobject WHERE moederobject IS NOT NULL);

Vraag 13:
Bereken het totale aantal unieke klanten dat heeft deelgenomen aan reizen met een verblijfsduur van meer dan 7 dagen.

Antwoord:
SELECT COUNT(DISTINCT k.nr) AS totaal_unieke_klanten
FROM Klant k
JOIN Deelname d ON k.nr = d.klant
JOIN Reis r ON d.reis = r.nr
WHERE r.duur > 7;
Vraag 14:
Update de diameter van een specifiek hemelobject (bijvoorbeeld 'Aarde') naar een nieuwe waarde (bijvoorbeeld 12742).

Antwoord:
UPDATE Hemelobject
SET diameter = 12742
WHERE naam = 'Aarde';
Vraag 15:
Verwijder alle deelnames van een specifieke klant (bijvoorbeeld klantnummer 3).

Antwoord:
DELETE FROM Deelname
WHERE klant = 3;
Vraag 16:
Vind alle reizen met een duur tussen 5 en 10 dagen, inclusief de bijbehorende transportinformatie.

Antwoord:
SELECT r.nr, r.vertrekdatum, r.duur, r.prijs, t.omschrijving AS transport_omschrijving
FROM Reis r
JOIN Transport t ON r.transport = t.code
WHERE r.duur BETWEEN 5 AND 10;
Vraag 17:
Bereken het gemiddelde van de prijzen van alle reizen.

Antwoord:
SELECT AVG(prijs) AS gemiddelde_prijs
FROM Reis;
Vraag 18:
Vind alle hemelobjecten die geen satellieten hebben. Toon de namen van deze hemelobjecten.

Antwoord:
SELECT h.naam
FROM Hemelobject h
LEFT JOIN Hemelobject sat ON h.naam = sat.moederobject
WHERE sat.moederobject IS NULL;

Waarschijnlijk: 
SELECT h.naam
FROM Hemelobject h
WHERE h.moederobject IS NULL;

Vraag 19:
Update de afstand van een specifieke hemelobjectnaam (bijvoorbeeld 'Mars') naar een nieuwe waarde (bijvoorbeeld 0.52).

Antwoord:
UPDATE Hemelobject
SET afstand = 0.52
WHERE naam = 'Mars';
Vraag 20:
Verwijder alle bezoeken aan hemelobjecten met een afstand groter dan 100 lichtjaar.

Antwoord:
DELETE FROM Bezoek
WHERE hemelobject IN (SELECT naam FROM Hemelobject WHERE afstand > 100);
Vraag 21:
Vind het hoogste reisnummer dat nog niet is gebruikt.

Antwoord:
SELECT MAX(nr) + 1 AS nieuw_reisnummer
FROM Reis;
Vraag 22:
Bereken het totale aantal reizen per transportmiddel. Toon de transportcode en het bijbehorende totale aantal reizen.

Antwoord:
SELECT r.transport, COUNT(r.nr) AS totaal_reizen
FROM Reis r
GROUP BY r.transport;
Vraag 23:
Verwijder alle hemelobjecten waarvan de diameter kleiner is dan het gemiddelde van alle diameters.

Antwoord:
DELETE FROM Hemelobject
WHERE diameter < (SELECT AVG(diameter) FROM Hemelobject);



Basisqueriess:

Schrijf een SQL-query om alle transportcodes en bijbehorende omschrijvingen uit de "Transport" tabel op te halen.
Haal de naam en geboortedatum op van alle klanten in de "Klant" tabel.
Join-operaties:

Schrijf een query die de naam van de klant, het reisnummer en de vertrekdatum ophaalt voor alle deelnames in de "Deelname" tabel.
Haal de omschrijving van het transportmiddel, de vertrekdatum en de duur op voor alle reizen in de "Reis" tabel.
Filtering en Sortering:

Selecteer de naam en diameter van hemelobjecten waarvan de diameter groter is dan 100, gesorteerd op naam.
Haal de transportcodes op voor reizen waarvan de prijs groter is dan 500.
Groepering en Aggregatie:

Schrijf een query om het gemiddelde van de duur van alle reizen te berekenen.
Bepaal het aantal bezoeken aan elk hemelobject.
Subqueries:

Geef de naam en vertrekdatum van reizen waarbij het transport een bepaalde omschrijving heeft (gebruik een subquery).
Haal de namen op van hemelobjecten die door geen enkel ander hemelobject worden omcirkeld.
Geavanceerde Joins:

Schrijf een query om de naam van het moederobject, de naam van het hemelobject en de vertrekdatum van de bijbehorende reis op te halen.
Haal de naam en geboortedatum van klanten op die hebben deelgenomen aan reizen met een bepaalde duur (gebruik een INNER JOIN).
Zorg ervoor dat de vragen voldoende uitdagend zijn, maar ook haalbaar voor studenten op basis van de gegeven databasestructuur.




Basisqueries:

Alle transportcodes en bijbehorende omschrijvingen:
SELECT code, omschrijving FROM Transport;
Naam en geboortedatum van alle klanten:
SELECT naam, geboortedatum FROM Klant;
Join-operaties:

Naam van de klant, reisnummer en vertrekdatum voor alle deelnames:
SELECT k.naam, d.reis, r.vertrekdatum
FROM Klant k
JOIN Deelname d ON k.nr = d.klant
JOIN Reis r ON d.reis = r.nr;
Omschrijving van het transportmiddel, vertrekdatum en duur voor alle reizen:
SELECT t.omschrijving, r.vertrekdatum, r.duur
FROM Reis r
JOIN Transport t ON r.transport = t.code;
Filtering en Sortering:

Naam en diameter van hemelobjecten waarvan de diameter groter is dan 100, gesorteerd op naam:

SELECT naam, diameter
FROM Hemelobject
WHERE diameter > 100
ORDER BY naam;
Transportcodes voor reizen waarvan de prijs groter is dan 500:
SELECT r.transport
FROM Reis r
WHERE r.prijs > 500;
Groepering en Aggregatie:

Gemiddelde duur van alle reizen:

SELECT AVG(duur) AS gemiddelde_duur
FROM Reis;
Aantal bezoeken aan elk hemelobject:

SELECT hemelobject, COUNT(*) AS aantal_bezoeken
FROM Bezoek
GROUP BY hemelobject;
Subqueries:

Naam en vertrekdatum van reizen met een bepaalde omschrijving (bijvoorbeeld 'Trein'):

SELECT naam, vertrekdatum
FROM Reis
WHERE transport IN (SELECT code FROM Transport WHERE omschrijving = 'Trein');
Namen van hemelobjecten die door geen enkel ander hemelobject worden omcirkeld:

SELECT naam
FROM Hemelobject
WHERE naam NOT IN (SELECT moederobject FROM Hemelobject WHERE moederobject IS NOT NULL);
Geavanceerde Joins:

Naam van het moederobject, naam van het hemelobject en vertrekdatum van de bijbehorende reis:

SELECT h1.naam AS moederobject, h2.naam AS hemelobject, r.vertrekdatum
FROM Hemelobject h1
JOIN Hemelobject h2 ON h1.naam = h2.moederobject
JOIN Bezoek b ON h2.naam = b.hemelobject
JOIN Reis r ON b.reis = r.nr;
Namen en geboortedatums van klanten die hebben deelgenomen aan reizen met een bepaalde duur:

SELECT k.naam, k.geboortedatum
FROM Klant k
JOIN Deelname d ON k.nr = d.klant
JOIN Reis r ON d.reis = r.nr
WHERE r.duur = <bepaalde duur>;

Gecombineerde Queries:

Haal de namen van klanten op die hebben deelgenomen aan reizen met een duur langer dan 5 dagen en waarvan de prijs minder dan 1000 is.

SELECT k.naam
FROM Klant k
JOIN Deelname d ON k.nr = d.klant
JOIN Reis r ON d.reis = r.nr
WHERE r.duur > 5 AND r.prijs < 1000;
Gebruik van LIKE:

Toon de omschrijvingen van transportmiddelen die het woord 'Bus' bevatten.

SELECT omschrijving
FROM Transport
WHERE omschrijving LIKE '%Bus%';
Subqueries met Aggregatiefuncties:

Vind het aantal bezoeken aan elk hemelobject, maar toon alleen die hemelobjecten waarvan het aantal bezoeken groter is dan het gemiddelde aantal bezoeken.

SELECT hemelobject, COUNT(*) AS aantal_bezoeken
FROM Bezoek
GROUP BY hemelobject
HAVING COUNT(*) > (SELECT AVG(aantal_bezoeken) FROM (SELECT hemelobject, COUNT(*) AS aantal_bezoeken FROM Bezoek GROUP BY hemelobject) AS gemiddelde_bezoeken);
Gebruik van JOIN met meerdere voorwaarden:

Haal de namen en geboortedatums van klanten op die hebben deelgenomen aan een reis met een duur langer dan 7 dagen en waarbij het transport per vliegtuig was.

SELECT k.naam, k.geboortedatum
FROM Klant k
JOIN Deelname d ON k.nr = d.klant
JOIN Reis r ON d.reis = r.nr
JOIN Transport t ON r.transport = t.code
WHERE r.duur > 7 AND t.omschrijving = 'Vliegtuig';
Gebruik van CASE:

Toon de naam en type (kort/lang) van reizen op basis van de duur (minder dan of gelijk aan 5 dagen wordt als 'kort' beschouwd, anders als 'lang').

SELECT nr, vertrekdatum, 
       CASE 
           WHEN duur <= 5 THEN 'kort'
           ELSE 'lang'
       END AS type
FROM Reis;
Gebruik van LIMIT:

Selecteer de eerste 5 klanten in de tabel "Klant" op basis van hun geboortedatum, gesorteerd van jongste naar oudste.

SELECT naam, geboortedatum
FROM Klant
ORDER BY geboortedatum DESC
LIMIT 5;