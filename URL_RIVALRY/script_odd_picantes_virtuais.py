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
#other imports
chromedriver.install(cwd=True)


username = getpass.getuser()
options = Options()
options.headless = True
options.add_argument('window-size = 1920x1080')

driver = webdriver.Chrome(options = options)

driver.get("https://www.rivalry.com/pt/esports")

time.sleep(5)

inspect = '//*[@id="__layout"]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div'
element = driver.find_element('xpath', f'{inspect}')

html_element = element.get_attribute('outerHTML')


soup = BeautifulSoup(html_element, 'html.parser')

jogo = {'Leauge':[],'Home':[],'Away':[],'Odds_H':[],'Odds_A':[]}
links = []
um = 0
dois = 0
tres = 0
aov = 0
njogos = 0
ant = ''
for link in soup.find_all("a",{"class": "betline-date-and-props"}):  
    if (link.get('href') != ant):
       #print(link.get('href'))
       njogos = njogos + 1
       ant = link.get('href')
       
print("Jogos com ODDS PICANTES: ", njogos)
for link in range(njogos):

 try:
    
     headers = soup.find_all("div",{"class": "flex flex-col ml-2"})
     jogo['Leauge'].append(headers[um].text)
     jogo['Leauge'][um] = jogo['Leauge'][um].replace("Vencedor da partida","")

     participantes = soup.find_all("div", {"class": "outcome-name"})
     jogo['Home'].append(participantes[dois].text)
     jogo['Away'].append(participantes[dois + 1].text)

     odd = soup.find_all("div",{"class": "outcome-odds"})
     jogo['Odds_H'].append(odd[tres].text)
     jogo['Odds_H'][um] = jogo['Odds_H'][um].replace("\n\t","")
     jogo['Odds_A'].append(odd[tres+1].text)
     jogo['Odds_A'][um] = jogo['Odds_A'][um].replace("\n\t","")
 except:
    pass

     
 um = um + 1 
 dois = dois + 2
 tres = tres + 2
 aov = aov + 3


df = pd.DataFrame(list(zip(jogo['Leauge'],jogo['Home'],jogo['Away'],jogo['Odds_H'],jogo['Odds_A'])),columns= ["Liga","TIME 1","TIME 2","ODD do TIme 1","ODD do Time 2"]) #.replace("\n","",regex = True)
df.to_csv("/home/aline/Documentos/Projetos/URL_RIVALRY/CVSDOSJOGOS/Odd_Picantes.csv", index=False)
#print(df)

