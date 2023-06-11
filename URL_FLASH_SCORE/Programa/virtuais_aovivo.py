from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
wd_Chrome = webdriver.Chrome('chromedriver',options=options)


import pandas as pd
import time
from tqdm import tqdm
from selenium.webdriver.common.by import By


def virtuais_aovivo():
 wd_Chrome.get("https://www.flashscore.com/esports/")


 time.sleep(2)

 id_jogos = []

 jogos = wd_Chrome.find_elements(By.CSS_SELECTOR,'div.event__match--live')
 for i in jogos:
   id_jogos.append(i.get_attribute("id"))

   
 id_jogos = [i[5:] for i in id_jogos]
 #print("JOGOS AO VIVO: ", len(id_jogos))

 jogo = {'Date':[],'Time':[],'Game':[],'League':[],'Home':[],'Away':[],'ScoreH':[],'ScoreA':[],'Half':[],'Odds_H':[],'Bookie_H':[],'Odds_A':[],'Bookie_A':[]}

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
        Half = Half.find_element(By.CSS_SELECTOR,'span').text
        
        
        
        # Match Odds
        wd_Chrome.get(f'https://www.flashscore.com/match/{link}/#/odds-comparison/home-away/full-time')
        time.sleep(2)
        celulas = wd_Chrome.find_elements(By.CSS_SELECTOR,'div.ui-table__row')
        
        Odds_H =[]
        Odds_A =[]
        bookie_odd = []
        if 'title="bet365"' in str(wd_Chrome.find_element(By.CSS_SELECTOR,'div.ui-table.oddsCell__odds')):
            for celula in celulas:
                bookie = celula.find_element(By.CSS_SELECTOR,'img.prematchLogo')
                bookie = bookie.get_attribute('title')
                if ((bookie == 'bet365')):
                    Odds_H.append(celula.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[0].text)
                    Odds_A.append(celula.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[1].text)
                    bookie_odd.append(bookie)
                else:
                    pass
        if 'title="1xBet"' in str(wd_Chrome.find_element(By.CSS_SELECTOR,'div.ui-table.oddsCell__odds')):
            for celula in celulas:
                bookie = celula.find_element(By.CSS_SELECTOR,'img.prematchLogo')
                bookie = bookie.get_attribute('title')
                if (bookie == '1xBet'):
                    Odds_H.append(celula.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[0].text)
                    Odds_A.append(celula.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[1].text)
                    bookie_odd.append(bookie)
                else:
                    pass

        if 'title="Betano.br"' in str(wd_Chrome.find_element(By.CSS_SELECTOR,'div.ui-table.oddsCell__odds')):
            for celula in celulas:
                bookie = celula.find_element(By.CSS_SELECTOR,'img.prematchLogo')
                bookie = bookie.get_attribute('title')
                if (bookie == 'Betano.br'):
                    Odds_H.append(celula.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[0].text)
                    Odds_A.append(celula.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[1].text)
                    bookie_odd.append(bookie)
                else:
                    pass
        if 'title="Betfair"' in str(wd_Chrome.find_element(By.CSS_SELECTOR,'div.ui-table.oddsCell__odds')):
            for celula in celulas:
                bookie = celula.find_element(By.CSS_SELECTOR,'img.prematchLogo')
                bookie = bookie.get_attribute('title')
                if (bookie == 'Betfair'):
                    Odds_H.append(celula.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[0].text)
                    Odds_A.append(celula.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[1].text)
                    bookie_odd.append(bookie)
                else:
                    pass
        if 'title="Betsson"' in str(wd_Chrome.find_element(By.CSS_SELECTOR,'div.ui-table.oddsCell__odds')):  
            for celula in celulas:
                bookie = celula.find_element(By.CSS_SELECTOR,'img.prematchLogo')
                bookie = bookie.get_attribute('title')
                if  (bookie == 'Betsson'):
                    Odds_H.append(celula.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[0].text)
                    Odds_A.append(celula.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[1].text)
                    bookie_odd.append(bookie)
                else:
                    pass
        else:
            for celula in celulas:
                bookie = celula.find_element(By.CSS_SELECTOR,'img.prematchLogo')
                bookie = bookie.get_attribute('title')
                Odds_H.append(celula.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[0].text)
                Odds_A.append(celula.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[1].text)
                bookie_odd.append(bookie)
    
    except:
        
        pass
    
      
    home_odd =0
    away_odd = 0
    for i in range(len(Odds_H)):
     if Odds_H[home_odd]<=Odds_H[i]:
        home_odd = i
    for i in range(len(Odds_A)):
     if Odds_A[away_odd]<=Odds_A[i]:
        away_odd = i
   
      
    if (len(Odds_H) != 0) & (len(Odds_A) !=0):
        
     jogo['Odds_H'].append(Odds_H[home_odd])
     jogo['Bookie_H'].append(bookie_odd[home_odd])   
     jogo['Odds_A'].append(Odds_A[away_odd])
     jogo['Bookie_A'].append(bookie_odd[away_odd])
     jogo['Date'].append(Date)
     jogo['Time'].append(Time)
     jogo['Game'].append(Country)
     jogo['League'].append(League)
     jogo['Home'].append(Home)
     jogo['Away'].append(Away)
     jogo['ScoreH'].append(ScoreH)
     jogo['ScoreA'].append(ScoreA)
     jogo['Half'].append(Half)


 return jogo

