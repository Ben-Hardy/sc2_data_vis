from bs4 import BeautifulSoup
import requests
import csv
from time import sleep



# NA
# protoss
r = requests.get('https://www.rankedftw.com/ladder/lotv/1v1/mmr/?f=am,protoss')

servers = ['am', 'eu', 'kr', 'cn']
races = ['protoss', 'zerg', 'terran', 'random']

for server in servers:
    for race in races:
        r = requests.get('https://www.rankedftw.com/ladder/lotv/1v1/mmr/?f={},{}'.format(server, race))

        soup = BeautifulSoup(r.content, features='html.parser')
        rows = soup.findAll('ul', class_='pagination')

        a = []
        for row in rows:
            a.append(str(row).split('\n'))

        numpages = int(a[0][-2][:-9].split('>')[-1])
        print('{} in {}: {}'.format(race, server, numpages))


        rows = soup.find_all('a', class_='row')
        header = ['rank', 'tier', 'name', 'mmr', 'points', 'wins', 'losses', 'played', 'winrate', 'age']
        player_file = csv.writer(open('{}_{}_players.csv'.format(server.upper(), race), 'w'))
        player_file.writerow(header)

        for i in rows:
            row = [j for j in i.get_text().split('\n') if len(j) > 0]
            player_file.writerow(row)


        off_sets = [i*100 for i in range(1,numpages)]

        for off_set in off_sets:
            r = requests.get('https://www.rankedftw.com/ladder/lotv/1v1/mmr/?f={},{}&offset={}'.format(server, race, off_set))
            soup = BeautifulSoup(r.content, features='html.parser')
            rows = soup.find_all('a', class_='row')

            for i in rows:
                row = [j for j in i.get_text().split('\n') if len(j) > 0]
                player_file.writerow(row)
            print("on page {}".format(1+ off_set//100))
            sleep(1)
