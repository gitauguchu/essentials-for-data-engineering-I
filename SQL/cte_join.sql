WITH
	counties(st, population) AS
	(SELECT state_us_abbreviation, sum(population_count_100_percent)
	 FROM us_counties_2010
	 GROUP BY state_us_abbreviation),

	 plants(st, plants) AS 
	 (SELECT st, count(*) AS plants
	  FROM meat_poultry_egg_inspect
	  GROUP BY st)

SELECT counties.st,
	   population,
	   plants,
	   round(plants/population::numeric(10,1) * 1000000, 1) AS per_million
FROM counties JOIN plants
ON counties.st = plants.st
ORDER BY per_million DESC;