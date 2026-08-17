import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('product_sales.csv')
df.columns = df.columns.str.strip()