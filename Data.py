import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('product_sales.csv')

# 2. Drop null values and assign to a new variable (or use inplace=True)
df_clean = df.dropna()

# 3. Extract data from the DataFrame
x_values = df_clean['City']
y_values = df_clean['Unit_Price']

# 4. Plot using the extracted data
plt.bar(x_values, y_values)
plt.show()