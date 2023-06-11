from selenium import webdriver
import chromedriver_autoinstaller as chromedriver
from selenium.webdriver.chrome.options import  Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import datetime 
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

driver.get("https://www.rivalry.com/pt/sports/apostas-football")

time.sleep(5)

inspect = '//*[@id="__layout"]/div/div[1]/div[1]/div[2]/div[2]/div[1]'

element = driver.find_element('xpath', f'{inspect}')

html_element = element.get_attribute('outerHTML')


soup = BeautifulSoup(html_element, 'html.parser')

jogo = {'Leauge':[],'Home':[],'Away':[],'Odds_H':[],'Odds_D':[],'Odds_A':[]}
links = []
um = 0
dois = 0
tres = 0
aov = 0
njogos = 0
hora = ''
njogos1=0
dia = datetime.date.strftime(datetime.date.today(), "%d/%m/%Y")

diah = dia[0]+dia[1]

for link1 in soup.find_all("span",{"class": "inline-block mr-1 rounded bg-red-light"}):  

       njogos1 = njogos1 + 1
         
for link in soup.find_all("strong"):  
      vr = link.text
      vr = vr[4] + vr[5]   
      if(vr == diah):
        njogos = njogos + 1
print("jogos ao vivo:", njogos1)       
print("Jogos para HJ: ", njogos)
for link in range(njogos):

 try:
    
     headers = soup.find_all("div",{"class": "flex flex-col ml-2"})
     jogo['Leauge'].append(headers[njogos1+um].text)
     jogo['Leauge'][um] = jogo['Leauge'][um].replace("Vencedor","")

     participantes = soup.find_all("div", {"class": "outcome-name"})
     jogo['Home'].append(participantes[3*njogos1+dois].text)
     jogo['Away'].append(participantes[3*njogos1+dois + 2].text)

     odd = soup.find_all("div",{"class": "outcome-odds"})
     jogo['Odds_H'].append(odd[3*njogos1+tres].text)
     jogo['Odds_H'][um] = jogo['Odds_H'][um].replace("\n\t","")
     jogo['Odds_D'].append(odd[3*njogos1+tres+1].text)
     jogo['Odds_D'][um] = jogo['Odds_D'][um].replace("\n\t","")
     jogo['Odds_A'].append(odd[3*njogos1+tres+2].text)
     jogo['Odds_A'][um] = jogo['Odds_A'][um].replace("\n\t","")
 except:
    pass

     
 um = um + 1 
 dois = dois + 3
 tres = tres + 3


df = pd.DataFrame(list(zip(jogo['Leauge'],jogo['Home'],jogo['Away'],jogo['Odds_H'],jogo['Odds_D'],jogo['Odds_A'])),columns= ["Liga","TIME 1","TIME 2","ODD do TIme 1",'ODD de Empate',"ODD do Time 2"]) #.replace("\n","",regex = True)
df.to_csv("/home/aline/Documentos/Projetos/futebol_rivalryaovivo.csv", index=False)
print(df)
