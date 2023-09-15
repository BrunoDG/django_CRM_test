import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root_pwd!'
)

# for the super user it's:
# user: admin
# password: admin_passwd!

# prepare a cursor object

cursorObject = dataBase.cursor()

# create a database

cursorObject.execute("CREATE DATABASE beveldrive")

print("All done!")