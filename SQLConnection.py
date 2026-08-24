import pymysql

db = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "flask_project"
)
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
db.close()
