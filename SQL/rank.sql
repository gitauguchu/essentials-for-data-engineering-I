CREATE TABLE widget_companies(
	id bigserial,
	company varchar(30) NOT NULL,
	widget_output integer NOT NULL
);

INSERT INTO widget_companies(company, widget_output)
VALUES
	('Morse Widgets', 125000),
	('Springfield Widget Masters', 143000),
	('Best Widgets', 196000),
	('Acme Inc.', 133000),
	('District Widget Inc.', 201000),
	('Clarke Amalgamated', 620000),
	('Stavesacre Industries', 244000),
	('Bowers Widget Emporium', 201000);

SELECT
	company,
	widget_output,
	rank() OVER (ORDER BY widget_output DESC),
	dense_rank() OVER (ORDER BY widget_output DESC)
FROM widget_companies;