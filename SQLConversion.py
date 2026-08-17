import pandas as pd
import mysql.connector
from mysql.connector import Error
import sqlalchemy


try:
    # Establish connection
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="flask_project"
    )
    
    # Verify connection
    if mydb.is_connected():
        print("Successfully connected to the database")
        
        # Example: Create a cursor and execute a query
        cursor = mydb.cursor()
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        print(f"Current database: {record}")

except Error as e:
    print(f"Error connecting to MySQL: {e}")

finally:
    # Close connection if it exists
    if 'mydb' in locals() and mydb.is_connected():
        cursor.close()
        mydb.close()
        print("MySQL connection is closed")

def parseCSV(filePath, table_name):
      csvData = pd.read_csv(filePath, header=None)
      csvData.columns = csvData.columns = csvData.columns.astype(str).str.strip().str.title()
      engine = sqlalchemy.create_engine('mysql+pymysql://root:@localhost/flask_project', echo=True)
      csvData.to_sql(table_name, con=engine, if_exists='append', index=False)

UPLOAD_FOLDER = 'static/files'
