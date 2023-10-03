-- Inner join: retourneert records met overeenkomende waarden in beide tabellen

-- Left (outer) join: retourneert alle records uit de linkertabel en de overeenkomende records uit de rechtertabel

-- Right (outer) join: retourneert alle records uit de rechtertabel en de overeenkomende records uit de linkertabel

-- Full (outer) join: retourneert alle records als er een overeenkomst is in de linker- of rechtertabel

-- 7.1
select cast(I.datum as varchar(12)) as datum, I.student, C.naam, I.cijfer, I.vrijstelling from inschrijving i
join cursus c on i.cursus = c.code
where I.cursus = C.code
   and (I.cijfer is null or I.cijfer <= 5)
   and (I.vrijstelling is False or I.vrijstelling is null)
	
	
select * from inschrijving i
join cursus c on i.cursus = c.code

select cast(I.datum as varchar(12)) as datum, I.student, C.naam, I.cijfer, I.vrijstelling from inschrijving i

-- 7.6
select C.code, C.naam, C.credits, C.examinator, D.naam
from Cursus C
	join Docent D on C.examinator = D.acr
where C.credits >= 4

-- 7.7
select C.code, C.naam, 
COALESCE(d.acr, 'Geen examinator') examinator, 
COALESCE(D.naam, 'Geen examinator') naam,
COALESCE(d.vervanger, 'Geen vervanger') Vervanger
from Cursus C
	left outer join Docent D on C.examinator = D.acr
	
-- 7.8 



-- 8.2
select count(*) from cursus c
join docent d on c.examinator = d.acr
where d.naam = 'C.date';
