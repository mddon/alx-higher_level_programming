-- List all the cities in California from the 'hbtn_0d_usa' database
SELECT cities.id, name

FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY cities.id ASC;
