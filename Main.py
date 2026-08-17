from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os 
from os.path import join, dirname, realpath
import mysql.connector
from mysql.connector import Error


app = Flask(__name__)


UPLOAD_FOLDER = 'static/files'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return render_template("index.html")

@app.route("/", methods=['POST'])
def uploadFiles():
      # get the uploaded file
      uploaded_file = request.files['file']
      if uploaded_file.filename != '':
           file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
          # set the file path
           uploaded_file.save(file_path)
          # save the file
      return redirect(url_for('index'))
  

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

def parseCSV(filePath):
      # CVS Column Names
      col_names = ['Order_ID', 'Order_Date', 'Customer_Name', 'City', 'State', 'Region', 'Country', 'Category', 'Sub_Category', 'Product_Name', 'Quantity', ' Unit_Price ', ' Revenue ', ' Profit ']
      # Use Pandas to parse the CSV file
      csvData = pd.read_csv(filePath,names=col_names, header=None)
      # Loop through the Rows
      for i,row in csvData.iterrows():
             print(i,row['Order_ID'],row['Customer_Name'],row['City'],row['State'],row['Region'],row['Country'], row['Category'],row['Sub_Category'],row['Product_Name'],row['Quantity'],row[' Unit_Price '],row[' Revenue '],row[' Profit '])

if __name__ == "__main__":
    app.run(port = 5000, debug = True)