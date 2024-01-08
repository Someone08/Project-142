import pandas as pd
import numpy as np

df1 = pd.read_csv('path/to/articles.csv')

df2 = df1.sort_values(by='total_events', ascending=False)

df3 = df2.head(20)
print(df3)