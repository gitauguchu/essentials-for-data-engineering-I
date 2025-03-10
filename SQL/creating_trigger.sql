CREATE TRIGGER grades_update
AFTER UPDATE
ON grades
FOR EACH ROW
EXECUTE PROCEDURE record_if_grades_changed();