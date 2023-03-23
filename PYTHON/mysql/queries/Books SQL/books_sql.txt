INSERT INTO users (fname, lname, email, age)
VALUES ('Jane', 'Amsden','jane0613@gmail.com', '26'),('Emily', 'Dixon','emily0512@gmail.com', '24'),('Theodore', 'Dostoevsky','theo1127@gmail.com', '32'),('William', 'Shapiro','william0901@gmail.com', '34'),('Lao', 'Xiu','lao0216@gmail.com', '29');

SELECT * FROM users;

INSERT INTO books (title, num_of_pages)
VALUES ('C Sharp', '324'),('Java', '243'),('Python', '605'),('PHP', '1024'),('Ruby', '865');

SELECT * FROM books;

UPDATE books SET title = 'C#' WHERE id = 1;

UPDATE users SET fname = 'Bill' WHERE id = 4;

INSERT INTO favorites (book_id, user_id)
VALUES (1,1),(2, 1);

SELECT * FROM favorites;

INSERT INTO favorites (book_id, user_id)
VALUES (1,2),(2,2),(3,2);

INSERT INTO favorites (book_id, user_id)
VALUES (1,3),(2,3),(3,3),(4,3);

INSERT INTO favorites (book_id, user_id)
VALUES (1,4),(2,4),(3,4),(4,4),(5,4);

SELECT users.fname, users.lname, favorites.book_id, favorites.id FROM users
JOIN favorites ON users.id = favorites.user_id WHERE book_id = 3;

DELETE FROM favorites WHERE id = 5;

INSERT INTO favorites (book_id, user_id)
VALUES (2,5);

SELECT users.fname, users.lname, favorites.book_id, favorites.id FROM users
JOIN favorites ON users.id = favorites.user_id WHERE book_id = 5;