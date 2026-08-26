from flask import Flask, render_template, request, redirect, url_for
import os 
from SQLConversion import parseCSV
from sqlalchemy import create_engine




app = Flask(__name__)

TABLE_NAME = "orders_table"
UPLOAD_FOLDER = 'static/files'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
engine = create_engine('mysql+pymysql://root:@localhost/flask_project', echo=True)

@app.route("/", methods=['POST'])
def uploadFiles():
      # get the uploaded file
      uploaded_file = request.files['file']
      if uploaded_file.filename != '':
           file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
          # set the file path
           uploaded_file.save(file_path)
           parseCSV(file_path, table_name = TABLE_NAME)
          # save the file
      return redirect(url_for('index'))
  

@app.route('/')
def index():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(port = 5000, debug = True)