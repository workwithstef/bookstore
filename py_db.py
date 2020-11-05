import mysql.connector


class MYSQLConnect:

    def __init__(self, database, host="localhost", user="root", passwd="ssss"):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.database = str(database)
        self.conn = self._establish_connection()
        self.cur = self.conn.cursor()

    def _establish_connection(self):

        connect = mysql.connector.connect(host=self.host, user=self.user, passwd=self.passwd, database=self.database)

        return connect

    def sql_query(self, query):
        if "ALTER TABLE" in query:
            print("Inappropriate Operation")
        else:
            return self.cur.execute(str(query))


books = MYSQLConnect("books")


# all_books = books.sql_query("select * from library")

monster_book = books.sql_query("select * from library where book_title IN ('Monster')")

# print(all_books.fetchone())

# mydb = mysql.connector.connect(host="localhost", user="root", passwd="ssss", database="books")
# cursor = mydb.cursor()
# book_list = cursor.execute("select * from library")

for i in books.cur:
    print(i)

