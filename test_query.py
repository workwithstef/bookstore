from py_db import MYSQLConnect

test = MYSQLConnect("books")

test.sql_query("INSERT INTO library (book_title, book_author, year_published) VALUES (\"TEST\", \"TEST\", \"2077\")")

test.conn.commit()

