from flask import Flask, render_template, request, url_for, redirect
from py_db import MYSQLConnect

app = Flask(__name__)

book_db = MYSQLConnect("books")



@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/library')
def library():
    book_db.sql_query("select * from library")

    lib = []
    for i in book_db.cur:
        books = {
            'title': i[1],
            'author': i[2],
            'year': i[3]
        }

        lib.append(books)
    return render_template('library.html', lib=lib)

@app.route('/add-book', methods=['POST', 'GET'])
def add_book():
# I want to collect add_book user input data and update the library page
    if request.method == "POST":
        book_title = (request.form['book-title'])
        book_author = (request.form['book-author'])
        pub_year = (request.form['pub-year'])

        book_db.sql_query(f"""INSERT INTO library
                    (book_title, book_author, year_published)
                    VALUES
                    ("{book_title}", "{book_author}", "{pub_year}")
                    """)
        book_db.conn.commit()  # must use .commit() to commit changes to mysql database
        return redirect(url_for("added"))
    else:
        return render_template('add_book.html')


@app.route("/book-added")
def added():
    return f"<h1>Book added to Library!</h1>"

# @app.route('/handle_data', methods=['POST'])
# # I want to collect add_book user input data and update the library page
# def handle_data():
#     book_title = (request.form['book-title'])
#     book_author = (request.form['book-author'])
#     pub_year = (request.form['pub-year'])
#
#     new_book = book_db.sql_query(f"""INSERT INTO library
#                     (book_title, book_author, year_published)
#                     VALUES
#                     ("{book_title}", "{book_author}", "{pub_year}")
#                     """)
#
#     book_db.conn.commit()  # must use .commit() to commit changes to mysql database
#
#     return


# meaning this condition is only true if you run this script directly.
# app will run in debug mode, meaning changes to the script will seamlessly reflect on the web app
if __name__ == '__main__':
    app.run(debug=True)