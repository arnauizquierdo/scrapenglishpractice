# Control + K + C --> Comentar text
# Control + K + U --> Descomentar text

from cgi import print_arguments
from cgitb import text
import requests 
from bs4 import BeautifulSoup
import os

HOME_URL = 'https://www.english-practice.at/b1/grammar/tenses/b1-tenses-index.htm'

def main():
    try:
        response = requests.get(HOME_URL)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            listpdf = getListOfPdfLink(soup)

            if len(listpdf) != 0: 
                writePdf(listpdf)

    except ValueError as ve:
            print(ve)
    

def getListOfPdfLink(soup_content):

    listpdf = []

    for link in soup_content.find_all('a'):
        if link.get("href")[-4:] == ".pdf":
            pdf = "https://www.english-practice.at/b1/grammar/tenses/" + link.get("href")
            listpdf.append(pdf)
    
    return listpdf
        
def writePdf(listpdf):
    
    for i in range(len(listpdf)):
        try:
            response = requests.get(listpdf[i])
            if response.status_code == 200:
                pdf = open("pdf_list/" + listpdf[i].split("/")[6], 'wb')
                pdf.write(response.content)
                pdf.flush()
                pdf.close()

        except ValueError as ve:
                print(ve)

if __name__ == "__main__":
    main()

