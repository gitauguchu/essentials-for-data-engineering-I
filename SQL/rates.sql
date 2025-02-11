SELECT 
	city,
	st,
	population,
	property_crime,
	round(
		(property_crime::numeric / population) * 1000, 1
		--we convert the numerator to numeric to make the result include decimal places
	) AS pc_per_1000

FROM fbi_crime_data_2015
WHERE population >= 500000
ORDER BY (pc_per_1000) DESC;