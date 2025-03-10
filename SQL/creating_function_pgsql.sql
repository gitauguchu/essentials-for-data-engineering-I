CREATE OR REPLACE FUNCTION update_personal_days()
RETURNS void AS $$
BEGIN 
	UPDATE teachers
	SET personal_days = 
		CASE WHEN (now() - hire_date) BETWEEN '5 years'::interval AND '10 years'::interval THEN 4
			 WHEN (now() - hire_date) > '10 years'::interval THEN 5
			 ELSE 3
		END;
	RAISE NOTICE 'personal_days updated!';
END;
$$ LANGUAGE plpgsql;