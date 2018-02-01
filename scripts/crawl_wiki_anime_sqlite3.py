import csv
import re
from urllib.request import urlopen

from bs4 import BeautifulSoup

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 日本のテレビアニメ作品一覧 (2010年代 後半。2015~))
with open('anime.csv', 'w') as f_csv, urlopen('https://goo.gl/vFjEp5') as f_url:
    writer = csv.writer(f_csv, lineterminator='\n')

    soup = BeautifulSoup(f_url, "html.parser")
    counter = 0
    # クールごとのアニメ
    for i in range(0, 13):
        table = soup.find_all('table', {'class': 'wikitable'})[i]
        h3_span = soup.find_all('h3')[i].find_all('span')[1].text
        year = h3_span[:4]
        season = h3_span[6:h3_span.find('月')]
        for tr in table.find_all('tr'):
            a = tr.find('a')
            if a:
                # url = a.get('href')
                counter += 1
                writer.writerow([counter, a.text, year, season])
