from flask import Flask, render_template
from py_db import MYSQLConnect

app = Flask(__name__)

book_db = MYSQLConnect("books")

# book_db.sql_query("""INSERT INTO library
#                     (book_title, book_author, year_published)
#                     VALUES
#                     ('Moby Dick', 'Herman Melville', 1851)
#                     """)

# must use .commit() to commit changes to mysql database
book_db.conn.commit()


all_books = book_db.sql_query("select * from library")

# library = book_db.cur

lib = []
for i in book_db.cur:

    books = {
       'title': i[1],
       'author': i[2],
       'year': i[3]
    }

    lib.append(books)


@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/library')
def library():
    return render_template('library.html', lib=lib)

@app.route('/add-book')
def add_book():
    return render_template('add_book.html')


# meaning this condition is only true if you run this script directly.
# app will run in debug mode, meaning changes to the script will seamlessly reflect on the web app
if __name__ == '__main__':
    app.run(debug=True)