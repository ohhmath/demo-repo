import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


raw_csv_data = pd.read_csv(r'C:\Users\Mathieu\Documents\Python\GSPTSE.csv')
df_comp = raw_csv_data.copy()

df_comp.Close.plot(figsize=(15,4),title= "Low graph")


df_comp.Close.plot(figsize=(10,5),title= "Low graph")
df_comp.Open.plot(figsize=(10,5),title= "Low graph")
plt.title("Open vs Close")
plt.show()

pd.to_datetime(df_comp.Date)