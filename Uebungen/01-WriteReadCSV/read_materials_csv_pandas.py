import pandas as pd
df=pd.read_csv('materials.csv')
print('Printing first rows:')
print(df.head())
print('Mean values of numeric values:')
print(df.mean(numeric_only=True))
print('Median values of numeric values:')
print(df.median(numeric_only=True))
