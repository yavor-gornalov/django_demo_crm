import mysql.connector

dataBase = mysql.connector.connect(
    host = 'your_host',
    user = 'your_user',
    password = 'your_password'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE your_database_name")

print("All Done!")