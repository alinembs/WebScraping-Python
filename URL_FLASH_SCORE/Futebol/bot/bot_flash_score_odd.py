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

time.sleep(2)

# Pegando o ID dos Jogos
id_jogos = []

#jogos ao vivo
jogos = wd_Chrome.find_elements(By.CSS_SELECTOR,'div.event__match--live')
for i in jogos:
    id_jogos.append(i.get_attribute("id"))

# Exemplo de ID de um jogo: 'g_1_Gb7buXVt'    
id_jogos = [i[4:] for i in id_jogos]

print("JOGOS AO VIVO: ", len(id_jogos))

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
        ScoreH= wd_Chrome.find_element(By.CSS_SELECTOR,'div.detailScore__wrapper')
        ScoreH= ScoreH.find_elements(By.CSS_SELECTOR,'span')[0].text
        ScoreA= wd_Chrome.find_element(By.CSS_SELECTOR,'div.detailScore__wrapper')
        ScoreA= ScoreA.find_elements(By.CSS_SELECTOR,'span')[2].text
        Half = wd_Chrome.find_element(By.CSS_SELECTOR,'div.detailScore__status')
        Half = Half.find_elements(By.CSS_SELECTOR,'span')[0].text 
        Moment = wd_Chrome.find_element(By.CSS_SELECTOR,'div.detailScore__status')
        if Moment.find_elements(By.CSS_SELECTOR,'span')[0].text == 'Half Time':
            Moment = 'HALF TIME'
        else:
           Moment = Moment.find_elements(By.CSS_SELECTOR,'span')[1].text
        # Match Odds
        wd_Chrome.get(f'https://www.flashscore.com/match/{link}/#/odds-comparison/1x2-odds/full-time')
        time.sleep(2)
        celulas = wd_Chrome.find_elements(By.CSS_SELECTOR,'div.ui-table__row')
        
        Odds_H = []
        Odds_D = []
        Odds_A = []
        bookie_odd = []
        if 'title="bet365"' in str(wd_Chrome.find_element(By.CSS_SELECTOR,'div.ui-table.oddsCell__odds')):
            for celula in celulas:
                bookie = celula.find_element(By.CSS_SELECTOR,'img.prematchLogo')
                bookie = bookie.get_attribute('title')
                if ((bookie == 'bet365')):
                    Odds_H.append(celula.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[0].text)
                    Odds_D.append(celula.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[1].text)
                    Odds_A.append(celula.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[2].text)
                    bookie_odd.append(bookie)
                else:
                    pass
        if 'title="1xBet"' in str(wd_Chrome.find_element(By.CSS_SELECTOR,'div.ui-table.oddsCell__odds')):
            for celula in celulas:
                bookie = celula.find_element(By.CSS_SELECTOR,'img.prematchLogo')
                bookie = bookie.get_attribute('title')
                if (bookie == '1xBet'):
                    Odds_H.append(celula.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[0].text)
                    Odds_D.append(celula.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[1].text)
                    Odds_A.append(celula.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[2].text)
                    bookie_odd.append(bookie)
                else:
                    pass

        if 'title="Betano.br"' in str(wd_Chrome.find_element(By.CSS_SELECTOR,'div.ui-table.oddsCell__odds')):
            for celula in celulas:
                bookie = celula.find_element(By.CSS_SELECTOR,'img.prematchLogo')
                bookie = bookie.get_attribute('title')
                if (bookie == 'Betano.br'):
                    Odds_H.append(celula.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[0].text)
                    Odds_D.append(celula.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[1].text)
                    Odds_A.append(celula.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[2].text)
                    bookie_odd.append(bookie)
                else:
                    pass
        if 'title="Betfair"' in str(wd_Chrome.find_element(By.CSS_SELECTOR,'div.ui-table.oddsCell__odds')):
            for celula in celulas:
                bookie = celula.find_element(By.CSS_SELECTOR,'img.prematchLogo')
                bookie = bookie.get_attribute('title')
                if (bookie == 'Betfair'):
                    Odds_H.append(celula.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[0].text)
                    Odds_D.append(celula.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[1].text)
                    Odds_A.append(celula.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[2].text)
                    bookie_odd.append(bookie)
                else:
                    pass
        if 'title="Betsson"' in str(wd_Chrome.find_element(By.CSS_SELECTOR,'div.ui-table.oddsCell__odds')):  
            for celula in celulas:
                bookie = celula.find_element(By.CSS_SELECTOR,'img.prematchLogo')
                bookie = bookie.get_attribute('title')
                if  (bookie == 'Betsson'):
                    Odds_H.append(celula.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[0].text)
                    Odds_D.append(celula.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[1].text)
                    Odds_A.append(celula.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[2].text)
                    bookie_odd.append(bookie)
                else:
                    pass
        else:
            for celula in celulas:
                bookie = celula.find_element(By.CSS_SELECTOR,'img.prematchLogo')
                bookie = bookie.get_attribute('title')
                Odds_H.append(celula.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[0].text)
                Odds_D.append(celula.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[1].text)
                Odds_A.append(celula.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[2].text)
                bookie_odd.append(bookie)

    except:
        pass
    home_odd =0
    away_odd = 0
    dodd = 0
    for i in range(len(Odds_H)):
     if Odds_H[home_odd]<=Odds_H[i]:
        home_odd = i
    for i in range(len(Odds_D)):
     if Odds_D[dodd]<=Odds_D[i]:
        dodd = i
    for i in range(len(Odds_A)):
     if Odds_A[away_odd]<=Odds_A[i]:
        away_odd = i
     
    if (len(Odds_H) != 0) & (len(Odds_D) != 0) & (len(Odds_A) !=0):
     if (Half == '2ND HALF'):    
      text = '''
        🔎 Lupa - Apostas
        📅 Data: {}
        🕑 Hora: {}
        🌏: {}
        📍 Liga:{}
        🏆Confronto entre:{} X {}
        📋Status do Jogo: {} - {}
        📊 Score : {} - {}
        Maior Odd p/ Home: {} 
        🟡BookMaker: {}
        Maior Odd p/ Empate: {}
        🟢BookMaker: {}
        Maior Odd p/ Away: {}
        🔵BookMaker: {}
        '''.format(Date,Time,Country,League,Home,Away,Half,Moment,ScoreH,ScoreA,Odds_H[home_odd],bookie_odd[home_odd],Odds_D[dodd],bookie_odd[dodd],Odds_A[away_odd],bookie_odd[away_odd])

      url_base = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
      results = requests.get(url_base)       
      time.sleep(5)

   
