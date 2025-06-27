import pandas as pd

data = {'Dept': ['IT', 'HR', 'IT', 'HR'], 'Salary': [50000, 40000, 55000, 45000]}
df = pd.DataFrame(data)
grouped = df.groupby('Dept').mean()
