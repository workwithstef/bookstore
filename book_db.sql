show databases;

CREATE DATABASE books;

CREATE TABLE library
(
book_id INT IDENTITY(1,1),
book_title VARCHAR(50),
book_author VARCHAR(80),
year_published INT
)

INSERT INTO library
(book_title, book_author, year_published)
VALUES 
('Monsters of Men', 'Patrick Ness', 2010)
('The Girl with all the Gifts', 'M.R. Carey', 2014)