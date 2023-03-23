-- Creates 3 new users in the same line 
INSERT INTO users_schema.users (first_name, last_name, email, created_at, updated_at)
VALUES ('Jared', 'Campos', 'jared0215@hotmail.com', NOW(), NOW()), ('Michael', 'Tavarez', 'tallmantav@gmail.com', NOW(), NOW()), ('Mario', 'Grano', 'mariospizza@gmail.com', NOW(), NOW());

-- Selects all users
SELECT * FROM users;

-- Select the first user by their specific email
SELECT * FROM users WHERE email = 'jared0215@hotmail.com';

-- Selects last user by id no matter how many users we have
SELECT * FROM users ORDER BY id DESC LIMIT 1;

-- Changes the user with the id of 3s last name to Pancakes
UPDATE users SET last_name = 'Pancakes' WHERE id = 3;

-- Delets user with the id of 2
DELETE FROM users WHERE id = 2;

-- Sorts users by first name
SELECT * FROM users ORDER BY first_name DESC;