SELECT student, cursus,
CASE
	WHEN cijfer >=	6 then 'voldoende'
	WHEN cijfer <6 then 'onvoldoende'
	ELSE 'ingeschreven'
   END
FROM Tentamen




SELECT student, cursus, datum, cijfer,
CASE
  WHEN volgnr = 1 then 'poging 1'
  WHEN volgnr = 2 then 'poging 2'
  END as poging
where cijfer >= 6
FROM Tentamen


SELECT naam, acr, vakgroep as vakgroep_docent, vervanger
from docent 