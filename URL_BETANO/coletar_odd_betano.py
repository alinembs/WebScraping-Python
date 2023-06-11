from selenium import webdriver
import chromedriver_autoinstaller as chromedriver
from selenium.webdriver.chrome.options import  Options
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import getpass
import pandas as pd



chromedriver.install(cwd=True)
username = getpass.getuser()
options = Options()
options.headless = True
options.add_argument('window-size = 1920x1080')


driver = webdriver.Chrome(options = options)

driver.get("https://br.betano.com/live/")

time.sleep(5)

inspect = '/html/body/div[1]/div/section[2]/div[5]/div[2]/div/div/div[3]/div/div'
element = driver.find_element('xpath', f'{inspect}')


html_element = element.get_attribute('outerHTML')

soup = BeautifulSoup(html_element, 'html.parser')
#print(soup.prettify())

header = []
tempo = []
participante1 = []
participante2 = []
resultado1 = []
resultado2 = []
odd1 = []
odd2 = []
odd3 = []
 

um = 0
dois = 0
tres = 0


for i in range(1000):
   try:
     headers = soup.find_all("div",{
         "class":"live-events-league__header live-events-league__header--clickable"})
     content = str(headers[i].contents[1].text)
     content = content[3:len(content)-3]
     final = int(content[-2:-1])
     for i in range(final):
       header.append(content)
   except:
    pass


   um = 0 
   dois = 0
   tres = 0

#print(header)
for i in range(1000):
    try:

     participantes = soup.find_all("span", {"class": "live-event__participants__participant-name"})
     participante1.append(participantes[dois].text)
     participante2.append(participantes[dois + 1].text)

     result = soup.find_all("span", {"class":"live-event__scores__score__text"})
     resultado1.append(result[dois].text)
     resultado2.append(result[dois+1].text)

     odds = soup.find_all("span",{"class":"selections__selection__odd"})
     odd1.append(odds[tres].text)
     odd2.append(odds[tres+1].text)
     odd3.append(odds[tres+2].text)

    except:
     pass

    um = um + 1 
    dois = dois + 2
    tres = tres + 3


df = pd.DataFrame(list(zip(header,participante1,participante2,resultado1,resultado2,odd1,odd2,odd3)),columns= ["liga","time1","time2","placartime1","palcartime2","odd1_vencedor_1","odd2_vencedor_2","odd3_vencedor_3"]).replace("\n","",regex = True)
#df.to_csv("/home/aline/Documentos/Projetos/teste.csv", index=False)
print(df)
