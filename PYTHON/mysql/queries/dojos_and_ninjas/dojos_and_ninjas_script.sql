SET SQL_SAFE_UPDATES = 0;

-- Creates 3 dojos
INSERT INTO dojos (name, created_at, updated_at)
VALUES ('WORLDWIDE', NOW(), NOW()),('NEW JERSEY', NOW(), NOW()),('NEW YORK', NOW(), NOW());

-- Deletes the 3 dojos I just added
DELETE FROM dojos;

-- Creats 3 dojos
INSERT INTO dojos (name, created_at, updated_at)
VALUES ('WORLDWIDE', NOW(), NOW()),('NEW JERSEY', NOW(), NOW()),('NEW YORK', NOW(), NOW());

-- Creates 3 Ninjas that belong to the first dojo
INSERT INTO ninjas (dojo_id, first_name, last_name, age)
VALUES (1, 'Jape', 'Fiorillo', '25'),(1, 'Hector', 'Triana', '24'),(1, 'Mario', 'Grano', '25');

-- Creates 3 Ninjas that belong to the second dojo
INSERT INTO ninjas (dojo_id, first_name, last_name, age)
VALUES (2, 'Michael', 'Tavarez', '25'),(2, 'Nathan', 'Mirkov', '25'),(2, 'Jayson', 'Campos', '22');

-- Creates 3 Ninjas that belong to the third dojo
INSERT INTO ninjas (dojo_id, first_name, last_name, age)
VALUES (3, 'Cait', 'Artese', '22'),(3, 'Jeter', 'Campos', '31'),(3, 'Diana', 'Rodriguez', '50');

-- Retrieve all the ninjas from the first dojo
SELECT * FROM ninjas WHERE dojo_id = 1;

-- Retrieve all the ninjas from the last dojo
SELECT * FROM ninjas WHERE dojo_id = 3;

-- Retrieves the last ninja's dojo
SELECT * FROM ninjas WHERE dojo_id = 3 ORDER BY id DESC LIMIT 1;

SELECT * FROM dojos;
SELECT * FROM ninjas;