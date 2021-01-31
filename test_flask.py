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


if __name__ == '__main__':
    app.run(debug=True, host='192.168.10.100')
