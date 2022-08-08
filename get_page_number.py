from bs4 import BeautifulSoup
import requests
import csv
from time import sleep


r = requests.get('https://www.rankedftw.com/ladder/lotv/1v1/mmr/?f=kr,random')

soup = BeautifulSoup(r.content, features='html.parser')
rows = soup.findAll('ul', class_='pagination')

a = []
for row in rows:
    a.append(str(row).split('\n'))

row = a[0][-2][:-9].split('>')
print(int(row[-1]))
