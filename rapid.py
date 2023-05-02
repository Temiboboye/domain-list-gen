from bs4 import BeautifulSoup as BS
import requests
from texter import iplist

ip = '172.217.3.174'
page = requests.get(f'https://rapiddns.io/sameip{ip}/#result')

print(page.text.prettify())
