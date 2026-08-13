from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
@app.route('/csv.data')
def csv_to_html():
    df = pd.read_csv('product_sales.csv')
    html_table = df.to_html()
    return render_template("index.html", table=html_table)

if __name__ == "__main__":
    app.run(debug = True)