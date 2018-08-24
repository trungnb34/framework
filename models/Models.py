from mysql.connector import (connection)
from lib.env import *

class Models:

    def __init__(self):
        self.con = None

    def connect(self):
        try:
            con = connection.MySQLConnection(user=env("USER_NAME"), password=env("PASSWORD"), host=env("HOST"), database=env("DATABASE_NAME"))
            return con
        except mysql.connector.Error as error:
            return error
    
    def query(self, str_query):
        con = self.connect()
        cur = con.cursor()
        try:
            cur.execute(str_query)
            con.close()
            return cur.fetchall()
        except:
            con.close()
            return error