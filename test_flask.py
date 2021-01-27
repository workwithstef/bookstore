from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('add_book.html')


if __name__ == '__main__':
    app.run(debug=True, host='192.168.10.100')
