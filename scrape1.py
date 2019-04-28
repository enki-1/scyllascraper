import requests
from bs4 import BeautifulSoup

url = 'https://scylla.sh'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0'
}


# get the data
data = requests.get(url, headers=headers)


# load data into bs4
soup = BeautifulSoup(data.text, 'html.parser')

scylla = []
dbs = soup.find( 'table', { 'id' : 'dbs'})

for tr in dbs.find_all('tr'):
    urls = tr.find_all('td')[0].text.strip()
    print('https://scylla.sh/static/dbs/{}'.format(urls))
