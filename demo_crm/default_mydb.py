import mysql.connector

dataBase = mysql.connector.connect(
    host="your host", user="your user", password="your password"
)

cursorObject = dataBase.cursor()

try:
    cursorObject.execute("CREATE DATABASE your db name")
    print("All Done!")
except Exception as ex:
    print(str(ex))
