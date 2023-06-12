from selenium import webdriver
import chromedriver_autoinstaller as chromedriver
from selenium.webdriver.chrome.options import  Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import getpass
import pandas as pd
from tqdm import tqdm
import telegram
import requests
import json
token = ''
chat_id = ''
#other imports
chromedriver.install(cwd=True)


username = getpass.getuser()
options = Options()
options.headless = True
options.add_argument('window-size = 1920x1080')

driver = webdriver.Chrome(options = options)

driver.get("https://www.rivalry.com/pt/esports")

time.sleep(5)

#inspect = '//*[@id="__layout"]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div'
inspect = '//*[@id="__layout"]/div/div[1]/div[1]/div[2]/div[2]/div[2]'
element = driver.find_element('xpath', f'{inspect}')

html_element = element.get_attribute('outerHTML')


soup = BeautifulSoup(html_element, 'html.parser')


links = []
um = 0
dois = 0
tres = 0
aov = 0
njogos = 0
ant = ''

for link in soup.find_all("span",{"class": "inline-block mr-1 rounded bg-red-light"}):  

       njogos = njogos + 1
       
for link in range(njogos):

 try:
    
     headers = soup.find_all("div",{"class": "flex flex-col ml-2"})
     Liga = headers[um].text
     Liga = Liga.replace("Vencedor da partida","")

     participantes = soup.find_all("div", {"class": "outcome-name"})
     Home = participantes[dois].text
     Away= participantes[dois + 1].text

     odd = soup.find_all("div",{"class": "outcome-odds"})
     OddHome = odd[tres].text
     OddHome = OddHome.replace("\n\t","")
     OddAWay = odd[tres+1].text
     OddAway = OddAWay.replace("\n\t","")
 except:
    pass

 text = '''
        🔎 Lupa - Apostas
      🎮 BookMaker  - RIVALRY
     ❗❗ AO VIVO ❗❗ 
     📍 Liga: {}
     🏆Confronto entre:{} X {}
     🔵 Odd p/ Home:{} 
     🟣Odd p/ Away:{}
                      '''.format(Liga,Home,Away,OddHome,OddAWay)

 url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
 results = requests.get(url_base)       
 time.sleep(5)

 um = um + 1 
 dois = dois + 2
 tres = tres + 2
 aov = aov + 3
