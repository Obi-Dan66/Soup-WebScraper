# Web Scraping of title names and perexes from https://udalosti247.cz/
from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://udalosti247.cz/').text # input url and and.text at the end
soup = BeautifulSoup(html_text, 'lxml')
main_titles = soup.find_all('div',class_='homepage-new-top-part') #33:10, 55:49
tertial_titles = soup.find_all('div', class_ = 'tertial-articles')

for title in main_titles:
    main_title = title.find('div',class_='title').text
    perex_main = title.find('div',class_='description').text
    print (f'''Hlavní článek:  {main_title.strip()}''')
    print (f'''Perex:  {perex_main.strip()}''')
    print('')

for title in tertial_titles:
    other_title = title.find('div',class_='title').text
    perex_other = title.find('div',class_='description').text
    print('Další články:  ')
    print('')
    print (f'''Nadpis:  {other_title.strip()}''')
    print (f'''Perex:  {perex_other.strip()}''')