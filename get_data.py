import pandas as pd

df = pd.read_csv('qm9.csv')
df = df.sample(n=20000, random_state=5)
df.to_csv('data.csv', index = False)
