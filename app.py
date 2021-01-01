import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# pd.set_option('display.max_rows', 10)
df=pd.read_csv('Stamp(final).csv')

df1=df['Country']
df2=df['Qty']
plt.bar(df1,df2)
plt.xticks(rotation=90)
plt.show()