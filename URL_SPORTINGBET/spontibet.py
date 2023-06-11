
from selenium import webdriver
import chromedriver_autoinstaller as chromedriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import getpass
import pandas as pd

# other imports
import json
chromedriver.install(cwd=True)

username = getpass.getuser()
options = Options()
options.headless = True
options.add_argument('window-size = 1920x1080')

driver = webdriver.Chrome(options=options)


time.sleep(5)
url = 'https://sports.sportingbet.com/cds-api/bettingoffer/fixtures?x-bwin-accessid=OWMwMTY1ZDEtMDhmNy00NTY5LWExOWUtMzU4MTFmNzdkODAy&lang=pt-br&country=BR&userCountry=BR&fixtureTypes=Standard&state=Latest&offerMapping=Filtered&offerCategories=Gridable&fixtureCategories=Gridable,NonGridable,Other&sportIds=4&regionIds=&competitionIds=&conferenceIds=&isPriceBoost=false&skip=0&take=30&sortBy=Tags'
driver.get(url)

jogo = {'Data': [], 'Esporte': [], 'League': [], 'Home': [],
        'Away': [], 'Odd_Home': [], 'Odd_Draw': [], 'Odd_Away': [], 'Ambas Marcam Sim': [], 'Ambas Marcam Nao': [], 'Home ou X': [], 'X ou Away': [], 'Home ou Away': [], 'Gols: 0.5 Sim': [], 'Gols: 0.5 Não': [], 'Gols: 1.5 Sim': [], 'Gols: 1.5 Não': [], 'Gols: 2.5 Sim': [], 'Gols: 2.5 Não': [], 'Gols: 3.5 Sim': [], 'Gols: 3.5 Não': []}

time.sleep(2)
api = driver.find_element("xpath", '/html/body/pre')
time.sleep(2)

data = json.loads(api.get_attribute('innerHTML'))
arquivo = '/home/aline/Documentos/PROJETO_3/SportinBET/dados.json'

with open(arquivo, "w") as aberto:
    json.dump(data, aberto)
print("Salvo com sucesso!")

time.sleep(2)
for game, _ in enumerate(data['fixtures']):
    try:
        options = data['fixtures'][game]['optionMarkets'][0]['options']

        names = [option['name']['value'] for option in options]
        jogo["Home"].append(names[0])
        jogo["Away"].append(names[2])
        odd = [option['price']['odds'] for option in options]
        jogo['Odd_Home'].append(odd[0])
        jogo['Odd_Away'].append(odd[2])
        jogo['Odd_Draw'].append(odd[1])

        data_time = data['fixtures'][game]['startDate']

        jogo['Data'].append(data_time)

        sport = data['fixtures'][game]['sport']['name']['value']

        jogo['Esporte'].append(sport)
        league = data['fixtures'][game]['competition']['name']['value']

        jogo['League'].append(league)

        # Ambas Marcam
        options = data['fixtures'][game]['optionMarkets'][3]['options']
        odd = [option['price']['odds'] for option in options] 
        jogo['Ambas Marcam Sim'].append(odd[0])
        jogo['Ambas Marcam Nao'].append(odd[1])
        # Chance Dulpa
        options = data['fixtures'][game]['optionMarkets'][1]['options']
        odd = [option['price']['odds'] for option in options] 
        jogo['Home ou X'].append(odd[0])
        jogo['X ou Away'].append(odd[1])
        jogo['Home ou Away'].append(odd[2])

        # Total de Gols
        options = data['fixtures'][game]['optionMarkets'][8]['options']
        odd = [option['price']['odds'] for option in options] 
        jogo['Gols: 0.5 Sim'].append(odd[0])
        jogo['Gols: 0.5 Não'].append(odd[1])

        options = data['fixtures'][game]['optionMarkets'][6]['options']
        odd = [option['price']['odds'] for option in options] 
        jogo['Gols: 1.5 Sim'].append(odd[0])
        jogo['Gols: 1.5 Não'].append(odd[1])

        options = data['fixtures'][game]['optionMarkets'][5]['options']
        odd = [option['price']['odds'] for option in options] 
        jogo['Gols: 2.5 Sim'].append(odd[0])
        jogo['Gols: 2.5 Não'].append(odd[1])

        options = data['fixtures'][game]['optionMarkets'][7]['options']
        odd = [option['price']['odds'] for option in options] 
        jogo['Gols: 3.5 Sim'].append(odd[0])
        jogo['Gols: 3.5 Não'].append(odd[1])

    except IndexError:
        pass
df = pd.DataFrame(list(zip(jogo['Esporte'], jogo['Data'], jogo['League'], jogo['Home'], jogo['Away'], jogo['Odd_Home'],
                  jogo['Odd_Draw'], jogo['Odd_Away'],jogo['Ambas Marcam Sim'],jogo['Ambas Marcam Nao'],jogo['Home ou X'],jogo['X ou Away'],jogo['Home ou Away'],jogo['Gols: 0.5 Sim'],jogo['Gols: 0.5 Não'],jogo['Gols: 1.5 Sim'],jogo['Gols: 1.5 Não'],jogo['Gols: 2.5 Sim'],jogo['Gols: 2.5 Não'],jogo['Gols: 3.5 Sim'],jogo['Gols: 3.5 Não'])), columns=["Esporte", "Data", "Liga", "Home", "Away", "Odd Home", "Odd Draw", "Odd Away","Ambas Marcam Sim","Ambas Marcam Não", "Home ou X", "X ou Away","Home ou Away","Gols: + 0.5","Gols : -0.5","Gols: + 1.5","Gols : -1.5","Gols: + 2.5","Gols : -2.5","Gols: + 3.5","Gols : -3.5"])
df.to_csv("/home/aline/Documentos/PROJETO_3/SportinBET/jogos.csv", index=False)
print(df)
time.sleep(5)
print("Dados dos Jogos Salvos")
