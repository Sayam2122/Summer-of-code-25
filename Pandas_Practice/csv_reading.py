import pandas as pd

df = pd.read_csv('data.csv')
filtered = df[df['Age'] > 25]
