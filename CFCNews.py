from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

__author__= 'Adeleke Omotayo'

web_page = urlopen("https://www.dailymail.co.uk/sport/teampages/chelsea.html")
soupy = BeautifulSoup(web_page, 'html.parser')
cluby = soupy.find('h2', attrs={'class':'linkro-darkred'})
ally = soupy.find_all('p')

print('*****This Chelsea news feed has 50 entries***** ', '\n')

for j in ally[:-2]: 
    print(j.get_text())

print('\n Courtesy: DailyMail Sport')
