# Control + K + C --> Comentar text
# Control + K + U --> Descomentar text

from cgi import print_arguments
from cgitb import text
import requests 
from bs4 import BeautifulSoup
import os

#HOME_URL = 'https://www.english-practice.at/'
HOME_URL = 'https://www.english-practice.at/b1/grammar/tenses/b1-tenses-index.htm'

try:
    response = requests.get(HOME_URL)
    if response.status_code == 200:
        notice = response.content.decode('utf-8')
        #print("hola")

except ValueError as ve:
        print(ve)

soup = BeautifulSoup(response.content, 'html.parser')

#print(soup.prettify())
#print(soup.find_all('a'))

allpdfs = []

for link in soup.find_all('a'):
    pdf = "https://www.english-practice.at/b1/grammar/tenses/" + link.get("href")
    print(pdf)


