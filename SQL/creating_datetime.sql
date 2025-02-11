SELECT make_date(2018, 2, 22); --Returns a value of type date
SELECT make_time(18, 4, 30.3); --Returns a value of type time without timezone
SELECT make_timestamptz(2018, 2, 22, 18, 4, 30.3, 'Africa/Nairobi'); -- Returns a timestamp with time zone
