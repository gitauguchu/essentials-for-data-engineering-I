SELECT census.state_us_abbreviation AS st,
	   census.st_population,
	   plants.plant_count,
	   round(plants.plant_count/census.st_population::numeric(10,1)*1000000,1)
AS plants_per_million
FROM (
	SELECT st,
		count(*) AS plant_count
	FROM meat_poultry_egg_inspect
	GROUP BY st
)
	AS plants
JOIN
	(
		SELECT state_us_abbreviation,
			sum(p0010001) AS st_population
		FROM us_counties_2010
		GROUP BY state_us_abbreviation
	)
	AS census
ON plants.st = census.state_us_abbreviation
ORDER BY plants_per_million DESC;