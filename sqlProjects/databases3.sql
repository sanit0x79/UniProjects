SELECT student, cursus,
CASE
	WHEN cijfer >=	6 then 'voldoende'
	WHEN cijfer <6 then 'onvoldoende'
	ELSE 'ingeschreven'
   END
FROM Tentamen
