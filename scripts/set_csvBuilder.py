#build a python dictionary from set file to parse as json

#D-BT01-001|Vairina_Valiente|3|Dragon_Empire|Persona_Ride|RRR+SP
#   ID          NAME        GRADE       CLAN     RIDE_SKILL     RARITY


import csv
import os
import requests
from html.parser import HTMLParser
from bs4 import BeautifulSoup

request =requests.get('https://cardfight.fandom.com/wiki/Vairina')
#print(request) #CODE 200 OK

src = request.content
# https://lxml.de/installation.html
# https://github.com/html5lib/html5lib-python
soup = BeautifulSoup(src,'lxml')
print(soup.td.get_text())
