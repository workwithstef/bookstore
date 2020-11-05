# Project Experience

## Creating virtual env

- `python -m venv <venv_dir_name>` - creates directory for venv
- Activate venv: Different methods for this step depending on OS/CLI.

Windows Command Prompt; `venv_dir_name\Scripts\activate.bat`
Windows GitBash; `. venv_dir_name/Scripts/activate`

- If successfully activated '(venv_dir_name)' should appear over each line in CLI
- Use `where python` to show paths where python venv exist - your new venv directory should be listed
- At this point `pip list` should only show minimal packages (pip & setuptools)
- Now have a clean slate to install only required packages for the project
- `pip freeze` - outputs pip installed packages in a format that can be easily installed from a 'requirements.txt' file
 
## Connecting MySQL
Prerequisites:
- `pip3 install mysql-connector`
- `pip3 install mysql-connector-python`

In Python:
``` 
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="ssss", database="books")
```

## Executing Queries
- As shown in the py_db.py file, the mysql connection process and query execution has been abstracted via OOP.
- *NOTE: Although the query is executed using self.cursor().execute(), the result is saved to self.cursor()*
- self.conn.commit() method used to commit any changes to the mysql database

## Booksite Plan

Flask App Prerequisites
- `pip install flask`

In Python: 
```from flask import Flask, render_template```
render_template allows you to use pre-made .html files for the resultant flask web paths

### Home Page
- "Welcome to site, feel free to explore functionality"

*Grid Style links:*
- Library link
- Add Book link

### Library Page

- Print list of all the books; in a table (Title, Author, Genre, Published Year)
- Search bar functionality (type in title should print list of books where Title/author/genre/year=input)

### Add Book Page

- Add book functionality; form style
- Should update Library page

### Forms

Process of using front end user input as parameters for back end code

Front-End Side:
- Using HTML Forms attributes: 'action','method' and 'submit', input data can be saved to be later accessed via GET/POST requests.
- `<form action= "#"  method="post">` - 'action' specifies which url to handle submitted data. '#' means data is handled on the current url. 'method' refers to the HTTP method; can be "get" or "post". *post method is more encrypted and wouldn't be seen by the user.*
- Below is a form input example:
`<input type="text" id="book-title" name="book-title" class="form-control" placeholder="Title">`
- the 'name' attribute is used to specify the key for when the data is parsed into json (dictionary) format; as per the HTTP request. The value as part of the 'key-value' pair will be the user form input.

Back-End Side:
- Python Flask is the framework used for this webapp. Flask module includes methods 'requests', 'url_get', 'redirect' - which were used for the following steps
- To access the submitted data use requests.form method e.g >> `requests.method([<key>])`. This will select the value associated with the 'key'.
Remember 'key' == 'name' used previously when defining form input.  
- The user data can now be implemented in the python script as seen fit.

Below is a code example:

``` 
@app.route('/add-book', methods=['POST', 'GET'])
def add_book():
    if request.method == "POST":
        book_title = (request.form['book-title'])

        book_db.sql_query(f"""SELECT * FROM library WHERE name == '{book_title}';""")
        return redirect(url_for("added"), title=book_title)
    else:
        return render_template('add_book.html')

@app.route("/book-added")
def added(title):
    return f"<h1>{title} selected! </h1>"
```

- First when defining the class method decorator state ['POST', 'GET'] as the HTTP method parameters.
- Set if-else condition if HTTP method is POST (which is the case for the form), then run some code, which includes that form data. Else return a specified page; else being 'GET' and the specified page is the current one.
- A 'GET' method is called when navigating web urls so refreshing the page or simply going to it would use 'GET' request. So in that case we simply want to go to the page.
- On the other hand, after the some code is run, the page is redirected to '/book-added' - the url for `def added():`. Useful way of validating the form submission.
- Also the redirect method can save variables from the current function to be used as parameters in the resultant redirected function; as illustrated.
