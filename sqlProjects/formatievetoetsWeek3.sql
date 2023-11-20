-- 1.Een overzicht van de omschrijving en de prijzen van alle artikelen. Het opschrift van de verkoopprijs moet PRIJS worden.
SELECT omschrijving, verkoopprijs as prijs FROM artikel

-- 2.Een overzicht van alle categorieën met artikelen met een verkoopprijs boven 100 euro. Elke categorie mag maar één keer getoond worden.
SELECT DISTINCT categorie FROM artikel WHERE verkoopprijs > 100;

-- 3.Van de artikelen uit de categorieën 'Hockey' en 'Running' de volgende output:
SELECT omschrijving, verkoopprijs FROM artikel WHERE categorie IN ('Hockey', 'Running')

-- 4.Een overzicht waarbij van de artikelen die een verkoopprijs boven 80 euro hebben de tekst “Te duur” in beeld verschijnt. 
-- Heeft een artikel een verkoopprijs van maximaal 50 euro dan de tekst ‘Past in budget’. 
-- Heeft het artikel een prijs tussen 50 en 80 euro dan de tekst ‘Nog even sparen!’. budget”.
SELECT omschrijving, verkoopprijs,
CASE
	WHEN verkoopprijs > 80 THEN 'Te duur'
	WHEN verkoopprijs <= 50 THEN 'Past in Budget'
	ELSE 'Nog even Sparen'
END
FROM artikel;

-- 5.Een overzicht, naam, adres, plaats van de tabel winkel, waarbij in de plaatsnaam de lettercombinatie 
-- ‘dam’ moet voorkomen en in het telefoonnummer de combinatie (67).
SELECT * FROM winkel WHERE plaats LIKE '%dam%' AND telefoonnr LIKE '%67%'

-- 6.Een overzicht van de records uit de tabel artikel, (omschrijving en prijs). 
-- Verder moet het woord ‘schoen’ voorkomen in de omschrijving. 
-- De output moet geordend worden op verkoopprijs en omschrijving.
SELECT omschrijving, verkoopprijs FROM artikel
WHERE omschrijving LIKE '%schoen%'
ORDER BY verkoopprijs ASC;

-- 7.Een overzicht van alle dagen waarop ‘Kean Sport’ een bestelling geplaatst heeft.
SELECT cast(besteldatum as varchar(12)) as besteldatum, wcode
FROM bestelling
WHERE wcode = 'KE23'
-- OR
SELECT besteldatum
FROM winkel w
JOIN bestelling b ON w.wcode = b.wcode
AND w.naam = 'Kean Sport'
