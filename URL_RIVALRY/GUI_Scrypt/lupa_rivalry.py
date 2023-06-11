from selenium import webdriver
import chromedriver_autoinstaller as chromedriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import getpass
import pandas as pd
from tqdm import tqdm
import datetime
from PySimpleGUI import PySimpleGUI as sg
import pandas as pd

# other imports
chromedriver.install(cwd=True)


username = getpass.getuser()
options = Options()
options.headless = True
options.add_argument('window-size = 1920x1080')

driver = webdriver.Chrome(options=options)


def odd_picantes():

    driver.get("https://www.rivalry.com/pt/esports")

    time.sleep(5)

    inspect = '//*[@id="__layout"]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div'
    element = driver.find_element('xpath', f'{inspect}')

    html_element = element.get_attribute('outerHTML')

    soup = BeautifulSoup(html_element, 'html.parser')

    jogo = {'Leauge': [], 'Home': [], 'Away': [], 'Odds_H': [], 'Odds_A': []}
    links = []
    um = 0
    dois = 0
    tres = 0
    aov = 0
    njogos = 0
    ant = ''
    for link in soup.find_all("a", {"class": "betline-date-and-props"}):
        if (link.get('href') != ant):
            # print(link.get('href'))
            njogos = njogos + 1
            ant = link.get('href')

    print("Jogos com ODDS PICANTES: ", njogos)
    for link in range(njogos):

        try:

            headers = soup.find_all("div", {"class": "flex flex-col ml-2"})
            jogo['Leauge'].append(headers[um].text)
            jogo['Leauge'][um] = jogo['Leauge'][um].replace(
                "Vencedor da partida", "")

            participantes = soup.find_all("div", {"class": "outcome-name"})
            jogo['Home'].append(participantes[dois].text)
            jogo['Away'].append(participantes[dois + 1].text)

            odd = soup.find_all("div", {"class": "outcome-odds"})
            jogo['Odds_H'].append(odd[tres].text)
            jogo['Odds_H'][um] = jogo['Odds_H'][um].replace("\n\t", "")
            jogo['Odds_A'].append(odd[tres+1].text)
            jogo['Odds_A'][um] = jogo['Odds_A'][um].replace("\n\t", "")
        except:
            pass

        um = um + 1
        dois = dois + 2
        tres = tres + 2
        aov = aov + 3
    return jogo


def virtuais_de_hj():

    driver.get("https://www.rivalry.com/pt/esports")

    time.sleep(5)

    inspect = '//*[@id="__layout"]/div/div[1]/div[1]/div[2]/div[2]/div[2]'
    element = driver.find_element('xpath', f'{inspect}')

    html_element = element.get_attribute('outerHTML')

    soup = BeautifulSoup(html_element, 'html.parser')

    jogo = {'Leauge': [], 'Home': [], 'Away': [], 'Odds_H': [], 'Odds_A': []}
    links = []
    um = 0
    dois = 0
    tres = 0
    aov = 0
    njogos = 0
    hora = ''
    njogos1 = 0
    dia = datetime.date.strftime(datetime.date.today(), "%d/%m/%Y")

    diah = dia[0]+dia[1]

    for link1 in soup.find_all("span", {"class": "inline-block mr-1 rounded bg-red-light"}):

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

            headers = soup.find_all("div", {"class": "flex flex-col ml-2"})
            jogo['Leauge'].append(headers[njogos1+um].text)
            jogo['Leauge'][um] = jogo['Leauge'][um].replace(
                "Vencedor da partida", "")

            participantes = soup.find_all("div", {"class": "outcome-name"})
            jogo['Home'].append(participantes[2*njogos1+dois].text)
            jogo['Away'].append(participantes[2*njogos1+dois+1].text)

            odd = soup.find_all("div", {"class": "outcome-odds"})
            jogo['Odds_H'].append(odd[2*njogos1+tres].text)
            jogo['Odds_H'][um] = jogo['Odds_H'][um].replace("\n\t", "")
            jogo['Odds_A'].append(odd[2*njogos1+tres+1].text)
            jogo['Odds_A'][um] = jogo['Odds_A'][um].replace("\n\t", "")
        except:
            pass

        um = um + 1
        dois = dois + 2
        tres = tres + 2
        aov = aov + 3

    return jogo


def virtuais_ao_vivo():

    driver.get("https://www.rivalry.com/pt/esports")

    time.sleep(5)

    inspect = '//*[@id="__layout"]/div/div[1]/div[1]/div[2]/div[2]/div[2]'
    # inspect = '//*[@id="__layout"]/div/div[1]/div[1]/div[2]/div[2]/div[1]'
    element = driver.find_element('xpath', f'{inspect}')

    html_element = element.get_attribute('outerHTML')

    soup = BeautifulSoup(html_element, 'html.parser')

    jogo = {'Leauge': [], 'Home': [], 'Away': [], 'Odds_H': [], 'Odds_A': []}
    links = []
    um = 0
    dois = 0
    tres = 0
    aov = 0
    njogos = 0

    for link in soup.find_all("span", {"class": "inline-block mr-1 rounded bg-red-light"}):

        njogos = njogos + 1

    print("Jogos AO VIVO: ", njogos)
    for link in range(njogos):

        try:

            headers = soup.find_all("div", {"class": "flex flex-col ml-2"})
            jogo['Leauge'].append(headers[um].text)
            jogo['Leauge'][um] = jogo['Leauge'][um].replace(
                "Vencedor da partida", "")

            participantes = soup.find_all("div", {"class": "outcome-name"})
            jogo['Home'].append(participantes[dois].text)
            jogo['Away'].append(participantes[dois + 1].text)

            odd = soup.find_all("div", {"class": "outcome-odds"})
            jogo['Odds_H'].append(odd[tres].text)
            jogo['Odds_H'][um] = jogo['Odds_H'][um].replace("\n\t", "")
            jogo['Odds_A'].append(odd[tres+1].text)
            jogo['Odds_A'][um] = jogo['Odds_A'][um].replace("\n\t", "")
        except:
            pass

        um = um + 1
        dois = dois + 2
        tres = tres + 2
        aov = aov + 3
    return jogo


def futebol_ao_vivo():
    driver.get("https://www.rivalry.com/pt/sports/apostas-football")

    time.sleep(5)

    inspect = '//*[@id="__layout"]/div/div[1]/div[1]/div[2]/div[2]/div[1]'
    element = driver.find_element('xpath', f'{inspect}')

    html_element = element.get_attribute('outerHTML')

    soup = BeautifulSoup(html_element, 'html.parser')

    jogo = {'Leauge': [], 'Home': [], 'Away': [],
            'Odds_H': [], 'Odds_D': [], 'Odds_A': []}
    links = []
    um = 0
    dois = 0
    tres = 0
    njogos = 0

    for link in soup.find_all("span", {"class": "inline-block mr-1 rounded bg-red-light"}):

        njogos = njogos + 1

    print("Jogos AO VIVO: ", njogos)
    for link in range(njogos):

        try:

            headers = soup.find_all("div", {"class": "flex flex-col ml-2"})
            jogo['Leauge'].append(headers[um].text)
            jogo['Leauge'][um] = jogo['Leauge'][um].replace("Vencedor", "")

            participantes = soup.find_all("div", {"class": "outcome-name"})
            jogo['Home'].append(participantes[dois].text)
            jogo['Away'].append(participantes[dois + 2].text)

            odd = soup.find_all("div", {"class": "outcome-odds"})
            jogo['Odds_H'].append(odd[tres].text)
            jogo['Odds_H'][um] = jogo['Odds_H'][um].replace("\n\t", "")
            jogo['Odds_D'].append(odd[tres+1].text)
            jogo['Odds_D'][um] = jogo['Odds_D'][um].replace("\n\t", "")
            jogo['Odds_A'].append(odd[tres+2].text)
            jogo['Odds_A'][um] = jogo['Odds_A'][um].replace("\n\t", "")
        except:
            pass

        um = um + 1
        dois = dois + 3
        tres = tres + 3

    return jogo


def futebol_de_hj():

    driver.get("https://www.rivalry.com/pt/sports/apostas-football")

    time.sleep(5)

    inspect = '//*[@id="__layout"]/div/div[1]/div[1]/div[2]/div[2]/div[1]'

    element = driver.find_element('xpath', f'{inspect}')

    html_element = element.get_attribute('outerHTML')

    soup = BeautifulSoup(html_element, 'html.parser')

    jogo = {'Leauge': [], 'Home': [], 'Away': [],
            'Odds_H': [], 'Odds_D': [], 'Odds_A': []}
    links = []
    um = 0
    dois = 0
    tres = 0
    aov = 0
    njogos = 0
    hora = ''
    njogos1 = 0
    dia = datetime.date.strftime(datetime.date.today(), "%d/%m/%Y")

    diah = dia[0]+dia[1]

    for link1 in soup.find_all("span", {"class": "inline-block mr-1 rounded bg-red-light"}):

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

            headers = soup.find_all("div", {"class": "flex flex-col ml-2"})
            jogo['Leauge'].append(headers[njogos1+um].text)
            jogo['Leauge'][um] = jogo['Leauge'][um].replace("Vencedor", "")

            participantes = soup.find_all("div", {"class": "outcome-name"})
            jogo['Home'].append(participantes[3*njogos1+dois].text)
            jogo['Away'].append(participantes[3*njogos1+dois + 2].text)

            odd = soup.find_all("div", {"class": "outcome-odds"})
            jogo['Odds_H'].append(odd[3*njogos1+tres].text)
            jogo['Odds_H'][um] = jogo['Odds_H'][um].replace("\n\t", "")
            jogo['Odds_D'].append(odd[3*njogos1+tres+1].text)
            jogo['Odds_D'][um] = jogo['Odds_D'][um].replace("\n\t", "")
            jogo['Odds_A'].append(odd[3*njogos1+tres+2].text)
            jogo['Odds_A'][um] = jogo['Odds_A'][um].replace("\n\t", "")
        except:
            pass

        um = um + 1
        dois = dois + 3
        tres = tres + 3
    return jogo

sg.theme('TanBlue')


def salvar_arquivos_futebol(jogo, path, i, type):
    i = str(i)
    data = pd.DataFrame(list(zip(jogo['Leauge'], jogo['Home'], jogo['Away'], jogo['Odds_H'], jogo['Odds_D'], jogo['Odds_A'])), columns=[
                        "Liga", "TIME 1", "TIME 2", "ODD do TIme 1", 'ODD de Empate', "ODD do Time 2"])  # .replace("\n","",regex = True)
    data.reset_index(inplace=True, drop=True)
    data.index = data.index.set_names(['Nº'])
    data = data.rename(index=lambda x: x + 1)
    data.to_csv(f'{path}/script_futebol_{type}_rivalry{i}.csv')
    print('Dados Salvos')


def salvar_arquivos_virtuais(jogo, path, i, type):
    i = str(i)
    data = pd.DataFrame(list(zip(jogo['Leauge'], jogo['Home'], jogo['Away'], jogo['Odds_H'], jogo['Odds_A'])), columns=[
                        "Liga", "TIME 1", "TIME 2", "ODD do TIme 1", "ODD do Time 2"])  # .replace("\n","",regex = True)
    data.reset_index(inplace=True, drop=True)
    data.index = data.index.set_names(['Nº'])
    data = data.rename(index=lambda x: x + 1)
    data.to_csv(f'{path}/script_virtuais_{type}_rivalry{i}.csv')
    print('Dados Salvos')


def janela_do_salvar():
    path = ''
    layout1 = [
            [sg.Input(visible=True, enable_events=True,
                      key='-IN-'), sg.FolderBrowse()],
            [sg.Button('SALVAR')]]

    window = sg.Window('SALVAR ARQUIVOS', layout1)

    while True:             # Event Loop
     event, values = window.read()
     if event in (sg.WIN_CLOSED, 'SALVAR'):
        break
     # When choice has been made, then fill in the listbox with the choices
     if event == '-IN-':

        path = values['-IN-'].split(';')[0].replace("[", '')
    window.close()
    return path


class LupaAPostas:

 def __init__(self):

    menu_layout = [['&Options',['&Help','&About']]]

    layout = [
    [sg.Menu(menu_layout,tearoff=True, font='_ 12', key='-MENUBAR-')],
    [sg.Text('Todos os Dados são Retirados do Site RIVALRY.COM ', size=(35, 3))],
    [sg.Text('JOGOS DE FUTEBOL AO VIVO', size=(10, 0)),
             sg.Button('Ao Vivo', size=(10, 0), key='fut1')],
    [sg.Text('JOGOS DE FUTEBOL DE HJ', size=(10, 0)),
             sg.Button('Jogos de Hj', size=(10, 0), key='fut2')],
    [sg.Text('E-Sports AO VIVO', size=(10, 0)),
             sg.Button('Virtuais AO VIVO', size=(10, 0), key='ev1')],
    [sg.Text('ODDs PICANTES', size=(10, 0)), sg.Button(
        'Picantes', size=(10, 0), key='ev2')],
    [sg.Text('E-Sports de Hj', size=(10, 0)),
             sg.Button('Virtuais de Hj', size=(10, 0), key='ev3')],
    [sg.Text('', size=(10, 0)), sg.Button('Exit', size=(10, 2))],
    [sg.Output(size=(30, 20))]
              ]

    self.janela = sg.Window('  Lupa- Apostas  ').layout(layout)

 def Iniciar(self):

   i = 0
   while True:
    self.button, self.values = self.janela.Read()

    if self.button == "fut1":
        i += 1
        print('Pegando os Dados')
        time.sleep(3)
        self.jogo = futebol_ao_vivo()
        path = janela_do_salvar()
        salvar_arquivos_futebol(self.jogo, path, i, 'aovivo')

    if self.button == "fut2":
        i += 1
        print('Pegando os Dados')
        time.sleep(3)
        self.jogo = futebol_de_hj()
        path = janela_do_salvar()
        salvar_arquivos_futebol(self.jogo, path, i, 'dehj')

    if self.button == "ev1":
        i += 1
        print('Pegando os Dados')
        time.sleep(3)
        self.jogo = virtuais_ao_vivo()
        path = janela_do_salvar()
        salvar_arquivos_virtuais(self.jogo, path, i, 'aovivo')

    if self.button == "ev2":
        i += 1
        print('Pegando os Dados')
        time.sleep(3)
        self.jogo = odd_picantes()
        path = janela_do_salvar()
        salvar_arquivos_virtuais(self.jogo, path, i, 'picantes')

    if self.button == "ev3":
        i += 1
        print('Pegando os Dados')
        time.sleep(3)
        self.jogo = virtuais_de_hj()
        path = janela_do_salvar()
        salvar_arquivos_virtuais(self.jogo, path, i, 'dehj')

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


