SELECT * FROM inschrijving ORDER BY cijfer asc

select * from cursus
where uren > 100
and credits < 5
order by uren desc, naam asc;


-- 6.7
SELECT naam, uren - 28*credits AS Verschil
FROM cursus
ORDER BY verschil desc, naam asc;

select student, cursus, volgnr, cijfer
from Tentamen
where volgnr >= 2
union
select student, cursus, volgnr, cijfer
from Tentamen
where cijfer <= 5
-- 6.9
select distinct order_, volgnr
from Klacht

-- 6.10

select 'Artikel' || nr || ' kost '
       || cast(round(verkoopprijs * 1.19, 2) as numeric(6,2))
       || ' euro ' prijslijst
from Artikel;


select upper(substring(omschrijving from 2 for 2)) from artikel ORDER BY verkoopprijs desc
-- 6.11

select upper(substring(omschrijving from 1 for 1)) ||
       lower(substring(omschrijving from 2)) artikel
from artikel
-- 6.13

SELECT nr, omschrijving, COALESCE(artikelgroep, 'los artikel')
from Artikel
order by 3,1 