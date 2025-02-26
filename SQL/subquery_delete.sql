CREATE TABLE us_counties_2010_top10 AS 
SELECT * FROM us_counties_2010;

DELETE FROM us_counties_2010_top10
WHERE p0010001 < (
	SELECT percentile_cont(.9) WITHIN GROUP (ORDER BY p0010001)
	FROM us_counties_2010_top10
);