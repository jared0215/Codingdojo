INSERT INTO users (first_name, last_name)
VALUES ('Jared', 'Campos'),('Paulie', 'Gista'),('Thomas', 'Smacks'),
		('Miguel', 'Tavarez'),('Mario', 'Goombats'),('Connor', 'Fiorillo');
        
SELECT * FROM users;
SELECT * FROM friendships;

INSERT INTO friendships (user_id, friend_id)
VALUES (1,2),(1,4),(1,6);

INSERT INTO friendships (user_id, friend_id)
VALUES (2,1),(2,3),(2,5);

INSERT INTO friendships (user_id, friend_id)
VALUES (3,2),(3,5);

INSERT INTO friendships (user_id, friend_id)
VALUES (4,3);

INSERT INTO friendships (user_id, friend_id)
VALUES (5,1),(5,6);

INSERT INTO friendships (user_id, friend_id)
VALUES (6,2),(6,3);

SELECT users.first_name, users.last_name, user2.first_name AS friend_first_name, user2.last_name AS friend_last_name FROM users
JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users AS user2 ON user2.id = friendships.friend_id;

SELECT users.first_name, users.last_name, user2.first_name AS friend_first_name, user2.last_name AS friend_last_name FROM users
JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users AS user2 ON user2.id = friendships.friend_id
WHERE user2.id = 1;

SELECT COUNT(friendships.id) FROM friendships;

SELECT users.id, users.first_name, users.last_name, COUNT(friendships.friend_id) AS num_of_friends
FROM users JOIN friendships ON users.id = friendships.user_id
GROUP BY users.id, users.first_name ORDER BY num_of_friends DESC;

SELECT users.first_name, users.last_name, user2.first_name AS friend_first_name, user2.last_name AS friend_last_name FROM users
JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users AS user2 ON user2.id = friendships.friend_id
WHERE users.id = 3 ORDER BY user2.first_name ASC;