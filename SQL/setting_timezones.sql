SET timezone TO 'US/Pacific';

CREATE TABLE time_zone_test (
	test_data timestamp with time zone
);
INSERT INTO time_zone_test VALUES ('2020-01-01 4:00');

SELECT test_data
FROM time_zone_test;

SET timezone TO 'US/Eastern';

SELECT test_data
FROM time_zone_test;

SELECT test_data AT TIME ZONE 'Asia/Seoul'
FROM time_zone_test;