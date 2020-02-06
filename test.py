from createDBConnection import MySQLConnection


def main():
    connection = MySQLConnection('carpentry_business')
    connection.get_mycursor().execute("CALL CreateAllTables;")


main()
