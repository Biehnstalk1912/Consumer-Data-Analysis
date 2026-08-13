from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os 
from os.path import join, dirname, realpath

app = Flask(__name__)
app.config["Debug"] = True

UPLOAD_FOLDER = 'static/files'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return render_template("index.html")
def parseCSV(filePath):
      # CVS Column Names
      col_names = ['Order_ID', 'Order_Date', 'Customer_Name', 'City', 'State', 'Region', 'Country', 'Category', 'Sub_Category', 'Product_Name', 'Quantity', ' Unit_Price ', ' Revenue ', ' Profit ']
      # Use Pandas to parse the CSV file
      csvData = pd.read_csv(filePath,names=col_names, header=None)
      # Loop through the Rows
      for i,row in csvData.iterrows():
             print(i,row['Order_ID'],row['Customer_Name'],row['City'],row['State'],row['Region'],row['Country'], row['Category'],row['Sub_Category'],row['Product_Name'],row['Quantity'],row[' Unit_Price '],row[' Revenue '],row[' Profit '])
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

if __name__ == "__main__":
    app.run(port = 5000)