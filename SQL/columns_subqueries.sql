SELECT geo_name,
	   state_us_abbreviation AS st,
	   p0010001 AS total_pop,
	   (SELECT percentile_cont(.5) WITHIN GROUP (ORDER BY p0010001) 
	   FROM us_counties_2010) AS us_median,
	   p0010001 - (SELECT percentile_cont(.5) WITHIN GROUP (ORDER BY p0010001)
	   				FROM us_counties_2010) AS diff_from_median
FROM us_counties_2010
WHERE (p0010001 - (SELECT percentile_cont(.5) WITHIN GROUP (ORDER BY p0010001)
				    FROM us_counties_2010))
		BETWEEN -1000 AND 1000;