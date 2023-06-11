import sys
import time
from PySimpleGUI import PySimpleGUI as sg
import pandas as pd
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

def futebol_aovivo():
 wd_Chrome.get("https://www.flashscore.com/")


 time.sleep(2)

 # Pegando o ID dos Jogos
 id_jogos = []

 jogos = wd_Chrome.find_elements(By.CSS_SELECTOR,'div.event__match--live')
 for i in jogos:
    id_jogos.append(i.get_attribute("id"))

   
 id_jogos = [i[4:] for i in id_jogos]

 print("JOGOS AO VIVO: ", len(id_jogos))
 jogo = {'Date':[],'Time':[],'Country':[],'League':[],'Home':[],'Away':[],'ScoreH':[],'ScoreA':[],'Half':[],'Moment':[],'Odds_H':[],'Bookie_H':[],'Odds_D':[],'Bookie_D':[],'Odds_A':[],'Bookie_A':[]}

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
        if(Moment.find_elements(By.CSS_SELECTOR,'span')[0].text == 'Half Time')| (Moment.find_elements(By.CSS_SELECTOR,'span')[0].text == 'HALF TIME'):
            Moment = 'HALF TIME'
        else:
           Moment = Moment.find_elements(By.CSS_SELECTOR,'span')[1].text
        
        # Match Odds
        wd_Chrome.get(f'https://www.flashscore.com/match/{link}/#/odds-comparison/1x2-odds/full-time')
        time.sleep(2)
        celulas = wd_Chrome.find_elements(By.CSS_SELECTOR,'div.ui-table__row')
        
        Odds_H =[]
        Odds_D =[]
        Odds_A =[]
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
        
     jogo['Odds_H'].append(Odds_H[home_odd])
     jogo['Bookie_H'].append(bookie_odd[home_odd])   
     jogo['Odds_D'].append(Odds_D[dodd])
     jogo['Bookie_D'].append(bookie_odd[dodd])
     jogo['Odds_A'].append(Odds_A[away_odd])
     jogo['Bookie_A'].append(bookie_odd[away_odd])
     jogo['Date'].append(Date)
     jogo['Time'].append(Time)
     jogo['Country'].append(Country)
     jogo['League'].append(League)
     jogo['Home'].append(Home)
     jogo['Away'].append(Away)
     jogo['ScoreH'].append(ScoreH)
     jogo['ScoreA'].append(ScoreA)
     jogo['Half'].append(Half)
     jogo['Moment'].append(Moment)

 return jogo

def futebol_marcado():
    
    wd_Chrome.get("https://www.flashscore.com/")

    ## Para jogos do dia seguinte
    #wd_Chrome.find_element(By.CSS_SELECTOR,'div.calendar__navigation--tomorrow').click()
    time.sleep(2)

    # Pegando o ID dos Jogos
    id_jogos = []
    #jogod que vao acontecer
    #jogos = wd_Chrome.find_elements(By.CSS_SELECTOR,'div.event__match--scheduled')
    #jogos ao vivo
    jogos = wd_Chrome.find_elements(By.CSS_SELECTOR,'div.event__match--scheduled')
    for i in jogos:
        id_jogos.append(i.get_attribute("id"))

    # Exemplo de ID de um jogo: 'g_1_Gb7buXVt'    
    id_jogos = [i[4:] for i in id_jogos]

    print("JOGOS MARCADOS PRO DIA: ", len(id_jogos))
    jogo = {'Date':[],'Time':[],'Country':[],'League':[],'Home':[],'Away':[],'Odds_H':[],'Bookie_H':[],'Odds_D':[],'Bookie_D':[],'Odds_A':[],'Bookie_A':[]}

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
            
            Odds_H =[]
            Odds_D =[]
            Odds_A =[]
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
            
            jogo['Odds_H'].append(Odds_H[home_odd])
            jogo['Bookie_H'].append(bookie_odd[home_odd])   
            jogo['Odds_D'].append(Odds_D[dodd])
            jogo['Bookie_D'].append(bookie_odd[dodd])
            jogo['Odds_A'].append(Odds_A[away_odd])
            jogo['Bookie_A'].append(bookie_odd[away_odd])
            jogo['Date'].append(Date)
            jogo['Time'].append(Time)
            jogo['Country'].append(Country)
            jogo['League'].append(League)
            jogo['Home'].append(Home)
            jogo['Away'].append(Away)
    
    return jogo


def esport_de_hj():

    wd_Chrome.get("https://www.flashscore.com/esports/")

    ## Para jogos do dia seguinte
    #wd_Chrome.find_element(By.CSS_SELECTOR,'div.calendar__navigation--tomorrow').click()
    time.sleep(2)

    # Pegando o ID dos Jogos
    id_jogos = []
    #jogod que vao acontecer
    #jogos = wd_Chrome.find_elements(By.CSS_SELECTOR,'div.event__match--scheduled')
    #jogos ao vivo
    jogos = wd_Chrome.find_elements(By.CSS_SELECTOR,'div.event__match--scheduled')
    for i in jogos:
        id_jogos.append(i.get_attribute("id"))

    # Exemplo de ID de um jogo: 'g_1_Gb7buXVt'   
    id_jogos = [i[5:] for i in id_jogos]
    print("JOGOS MARCADOS: ", len(id_jogos))
    jogo = {'Date':[],'Time':[],'Game':[],'League':[],'Home':[],'Away':[],'Odds_H':[],'Bookie_H':[],'Odds_A':[],'Bookie_A':[]}

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
    
        print(len(bookie_odd)) 
        print(home_odd)
        print(away_odd)
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


    return jogo


###TELA 

sg.theme('LightBlue4')

def salvar_arquivos(lower,tipo,path,i):
    i = str(i)
    data = pd.DataFrame(lower)
    data.reset_index(inplace=True, drop=True)
    data.index = data.index.set_names(['Nº'])
    data = data.rename(index=lambda x: x + 1)
    data.to_csv(f'{path}/script_{tipo}_FLASHCORE{i}.csv')
    print('Dados Salvos')

def janela_do_salvar():
    path = ''
    layout1 = [  
            [sg.Input(visible=True, enable_events=True, key='-IN-'), sg.FolderBrowse()],
            [ sg.Button('SALVAR')]  ]

    window = sg.Window('Window Title', layout1)

    while True:             # Event Loop
     event, values = window.read()
     if event in (sg.WIN_CLOSED, 'SALVAR'):
        break
     # When choice has been made, then fill in the listbox with the choices
     if event == '-IN-':
       
        path = values['-IN-'].split(';')[0].replace("[",'')
    window.close()
    return path

class LupaAPostas:


 def __init__(self):
        

    menu_layout = [['&Options',['&Help','&About']]]    
    layout = [
    [sg.Menu(menu_layout,tearoff=True, font='_ 12', key='-MENUBAR-')], 
    [sg.Text('Todos os Dados são Retirados do Site FLASHSCORE.COM', size=(35, 3))],   
    [sg.Text('JOGO AO VIVO DE FUTEBOL',size=(10,0)),sg.Button('AO VIVO FUT',size=(10,0),key='fut1')],
    [sg.Text('JOGO DE HJ DE FUTEBOL',size=(10,0)),sg.Button('DE HJ FUT',size=(10,0),key='fut2')],
    [sg.Text('JOGO AO VIVO DE E-SPORTS',size=(10,0)),sg.Button('AO VIVO E-S',size=(10,0),key='ev1')],
    [sg.Text('JOGO DE HJ DE E-SPORTS',size=(10,0)),sg.Button('DE HJ E-S',size=(10,0),key='ev2')],
    [sg.Text('', size=(10, 0)),sg.Button('Exit')],
    [sg.Output(size=(30,20))]
              ]
    
    self.janela = sg.Window('  Lupa- Apostas  ').layout(layout)


 def Iniciar(self):
   i = 0 
   while True: 
    self.button ,self.values = self.janela.Read()
   
    if self.button == "fut1":
        i += 1
        print('Pegando os Dados')
        time.sleep(3)
        self.jogo = futebol_aovivo()
        path = janela_do_salvar()
        salvar_arquivos(self.jogo,'live',path,i)

    if self.button == "fut2":
        i += 1
        print('Pegando os Dados')
        time.sleep(3)
        self.jogo = futebol_marcado()
        path = janela_do_salvar()
        salvar_arquivos(self.jogo,'hj',path,i)
        

    if self.button == "ev1":
        i += 1
        print('Pegando os Dados')
        time.sleep(3)
        self.jogo = virtuais_aovivo()
        path = janela_do_salvar()
        salvar_arquivos(self.jogo,'live',path,i)
    
    if self.button == "ev2":
        i += 1
        print('Pegando os Dados')
        time.sleep(3)
        self.jogo = esport_de_hj()
        path = janela_do_salvar()
        salvar_arquivos(self.jogo,'hj',path,i)

    if self.button in (sg.WIN_CLOSED, 'Exit'):
        break

    if self.button == 'About':

        self.janela.disappear()
        sg.popup('About this program', 'Version 1.0', 'PySimpleGUI Version', sg.get_versions())
        self.janela.reappear()
    
    if self.button == 'Help':

        self.janela.disappear()
        sg.popup('Help','Para Qualquer Problema Envie um Email para alinemariana1@hotmail.com')
        self.janela.reappear()

tela = LupaAPostas()
tela.Iniciar()



