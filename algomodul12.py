# Silviana Agustin - 065002400035

import pandas as pd

df = pd.read_csv(r"C:\Users\Lenovo\Downloads\algo\Negara - Negara.csv")

print(df.head())

mean = df.groupby('Benua').mean(numeric_only=True)
std = df.groupby('Benua').std(numeric_only=True)

print(df.head())
print('\nBerikut Mean Benua nya\n')
print(mean)
print('\nBerikut Standar Devisasi nya\n')
print(std)