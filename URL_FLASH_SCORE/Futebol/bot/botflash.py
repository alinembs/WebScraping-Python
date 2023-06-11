from selenium import webdriver
import telegram
import requests
import json
token = ''
chat_id = ''
# Instanciando o Objeto ChromeOptions
options = webdriver.ChromeOptions()

# Passando algumas opções para esse ChromeOptions
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Criação do WebDriver do Chrome
wd_Chrome = webdriver.Chrome('chromedriver',options=options)

"""# Importando as Bibliotecas"""

import pandas as pd
import time
from tqdm import tqdm
from selenium.webdriver.common.by import By

"""# Iniciando a Raspagem de Dados"""

# Com o WebDrive a gente consegue a pedir a página (URL)
wd_Chrome.get("https://www.flashscore.com/")

## Para jogos do dia seguinte
#wd_Chrome.find_element(By.CSS_SELECTOR,'div.calendar__navigation--tomorrow').click()
time.sleep(2)

# Pegando o ID dos Jogos
id_jogos = []
#jogod que vao acontecer
#jogos = wd_Chrome.find_elements(By.CSS_SELECTOR,'div.event__match--scheduled')
#jogos ao vivo
jogos = wd_Chrome.find_elements(By.CSS_SELECTOR,'div.event__match--live')
for i in jogos:
    id_jogos.append(i.get_attribute("id"))

# Exemplo de ID de um jogo: 'g_1_Gb7buXVt'    
id_jogos = [i[4:] for i in id_jogos]

print("JOGOS AO VIVO: ", len(id_jogos))
jogo = {'Date':[],'Time':[],'Country':[],'League':[],'Home':[],'Away':[],'Odds_H':[],'Odds_D':[],'Odds_A':[]}

for link in tqdm(id_jogos, total=len(id_jogos)):
    wd_Chrome.get(f'https://www.flashscore.com/match/{link}/#/match-summary')
    
    # Pegando as Informacoes Básicas do Jogo
    try:
        Date = wd_Chrome.find_element(By.CSS_SELECTOR,'div.duelParticipant__startTime').text.split(' ')[0]
        Time = wd_Chrome.find_element(By.CSS_SELECTOR,'div.duelParticipant__startTime').text.split(' ')[1]
        Country = wd_Chrome.find_element(By.CSS_SELECTOR,'span.tournamentHeader__country').text.split(':')[0]
        League = wd_Chrome.find_element(By.CSS_SELECTOR,'span.tournamentHeader__country')
        League = League.find_element(By.CSS_SELECTOR,'a').text
        Home = wd_Chrome.find_element(By.CSS_SELECTOR,'div.duelParticipant__home')
        Home = Home.find_element(By.CSS_SELECTOR,'div.participant__participantName').text
        Away = wd_Chrome.find_element(By.CSS_SELECTOR,'div.duelParticipant__away')
        Away = Away.find_element(By.CSS_SELECTOR,'div.participant__participantName').text
        
        # Match Odds
        wd_Chrome.get(f'https://www.flashscore.com/match/{link}/#/odds-comparison/1x2-odds/full-time')
        time.sleep(2)
        celulas = wd_Chrome.find_elements(By.CSS_SELECTOR,'div.ui-table__row')
        
        Odds_H = 0
        Odds_D = 0
        Odds_A = 0
        
        if 'title="bet365"' in str(wd_Chrome.find_element(By.CSS_SELECTOR,'div.ui-table.oddsCell__odds')):
            for celula in celulas:
                bookie = celula.find_element(By.CSS_SELECTOR,'img.prematchLogo')
                bookie = bookie.get_attribute('title')
                if ((bookie == 'bet365') & (Odds_H == 0)) | ((bookie == 'Betfair') & (Odds_H == 0)):
                    Odds_H = celula.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[0].text
                    Odds_D = celula.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[1].text 
                    Odds_A = celula.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[2].text
                else:
                    pass
        else:
            for celula in celulas:
                Odds_H = celula.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[0].text
                Odds_D = celula.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[1].text 
                Odds_A = celula.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[2].text
    
    except:
        pass

    text = '''
        Data:{}
        Hora:{}
        🌏:{}
        Liga:{}
        Confronto entre :
           🏆{} X {}
        ODD do Mante:{} 
        ODD de Empate:{}
        ODD dede Casa:{}
        '''.format(Date,Time,Country,League,Home,Away,Odds_H,Odds_D,Odds_A)

    url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
    results = requests.get(url_base)       
    time.sleep(2)

   
