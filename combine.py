import pandas as pd

servers = ['AM', 'EU', 'KR', 'CN']
races = ['protoss', 'zerg', 'terran', 'random']

output_filename = 'SC2_ladder_data.csv'

header = ['rank', 'tier', 'name', 'mmr', 'points', 'wins', 'losses', 'played', 'winrate', 'age', 'race', 'region']

output = pd.DataFrame(columns=header)
print(output.head())

for server in servers:
    for race in races:
        input_df = pd.read_csv('{}_{}_players.csv'.format(server.upper(), race))
        input_df['race'] = race
        input_df['region'] = server
        print(input_df.head())
        output = output.append(input_df)

print(output.shape[0])
output.to_csv(output_filename, index=False)
