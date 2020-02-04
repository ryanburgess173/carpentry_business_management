import mysql.connector


class MySQLConnection:
    __mydb = None
    __mycursor = None

    def __init__(self, db):
        self.__mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database=db
        )
        self.__mycursor = self.__mydb.cursor()

    def get_mydb(self):
        return self.__mydb

    def set_mydb(self, mydb):
        self.__mydb = mydb

    def get_mycursor(self):
        return self.__mycursor

    def set_mycursor(self, mycursor):
        self.__mycursor = mycursor
