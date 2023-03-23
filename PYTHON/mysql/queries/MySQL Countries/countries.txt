SELECT language FROM Languages;
SELECT * FROM cities;
SELECT * FROM countries;

-- Query #1
SELECT countries.name AS country, languages.language,languages.percentage FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE languages.language = 'Slovene';

-- Query #2
SELECT countries.name AS country, COUNT(cities.name) AS num_of_cities FROM cities
JOIN countries ON countries.id = cities.country_id
GROUP BY countries.name ORDER BY num_of_cities DESC;

-- Query #3
SELECT countries.name AS country, cities.population FROM cities
JOIN countries ON countries.id = cities.country_id
WHERE countries.name = 'Mexico' AND cities.population > 500000
GROUP BY countries.name, cities.population ORDER BY cities.population DESC;

-- Query #4
SELECT countries.name AS country, languages.language,languages.percentage FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE languages.percentage > 0.89 ORDER BY percentage DESC;

-- Query #5
SELECT countries.name AS country, countries.population, countries.surface_area FROM countries
WHERE countries.population > 100000 AND countries.surface_area < 501
ORDER BY countries.name;

-- Query #6
SELECT countries.name, countries.government_form, countries.capital, countries.life_expectancy FROM countries
WHERE countries.government_form = 'Constitutional Monarchy' AND countries.capital > 200 AND countries.life_expectancy > 75.0
ORDER BY countries.name;

-- Query #7
SELECT countries.name AS country, cities.name AS city, cities.district, cities.population FROM cities
JOIN countries ON countries.id = cities.country_id
WHERE countries.name = 'Argentina' AND cities.district = 'Buenos Aires' AND cities.population > 500000
GROUP BY countries.name, cities.name, cities.district, cities.population
ORDER BY cities.population DESC;

-- Query #8
SELECT region, COUNT(id) AS num_of_countries FROM countries
GROUP BY region ORDER BY num_of_countries DESC;