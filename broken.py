import pandas as pd

df = pd.read_csv('SC2_ladder_data.csv', dtype='unicode')

played = df['played']
played = pd.to_numeric(played)

print(type(played[0]))