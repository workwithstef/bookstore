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