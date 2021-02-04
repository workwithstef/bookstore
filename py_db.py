import mysql.connector
from shhh.py import *

class MYSQLConnect:

    def __init__(self, database, host="localhost", user="root", passwd=MY_SQL):
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


