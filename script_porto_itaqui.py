# imports


from selenium import webdriver
import chromedriver_autoinstaller as chromedriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import getpass
import pandas as pd


# other imports

chromedriver.install(cwd=True)


username = getpass.getuser()
options = Options()
options.headless = True
options.add_argument('window-size = 1920x1080')

driver = webdriver.Chrome(options=options)

driver.get("https://www.portodoitaqui.com/porto-agora/navios")

time.sleep(5)

n_esp = 'atracados'
n_atra = 'esperados'
n_fundi = 'fundeados'

element1 = driver.find_element(By.ID, f'{n_esp}')
element2 = driver.find_element(By.ID, f'{n_atra}')
element3 = driver.find_element(By.ID, f'{n_fundi}')


html_element1 = element1.get_attribute('outerHTML')
html_element2 = element2.get_attribute('outerHTML')
html_element3 = element3.get_attribute('outerHTML')

soup1 = BeautifulSoup(html_element1, 'html.parser')
soup2 = BeautifulSoup(html_element2, 'html.parser')
soup3 = BeautifulSoup(html_element3, 'html.parser')

Navios_Atracados = {'Berco': [], 'IMO': [], 'NAVIO': [], 'Operacao': [], 'Bordo': [
], 'Comp(m)': [], 'DWT': [], 'Carga': [], 'QTD.CARGA': [], 'Calado': [], 'Agencia': [],'Prev de Chegada':[], 'Ultima_Atualizao': []}
Navios_Esperando = {'Berco': [], 'IMO': [], 'NAVIO': [], 'Operacao': [], 'Bordo': [
], 'Comp(m)': [], 'DWT': [], 'Carga': [], 'QTD.CARGA': [], 'Calado': [], 'Agencia': [], 'Ultima_Atualizao': []}
Navios_Fundeados = {'Berco': [], 'IMO': [], 'NAVIO': [], 'Operacao': [], 'Bordo': [
], 'Comp(m)': [], 'DWT': [], 'Carga': [], 'QTD.CARGA': [], 'Calado': [], 'Agencia': [], 'Ultima_Atualizao': []}

navios_esp = 0
navios_fundi = 0
navios_atrac = 0

for n_navio in soup1.find_all("tr"):

    navios_esp = navios_esp + 1

print("Numero de Navios Esperandos : ", navios_esp - 1)

for n_navio in soup2.find_all("tr"):

    navios_atrac = navios_atrac + 1

print("Numero de Navios Atracados: ", navios_atrac - 1)

for n_navio in soup3.find_all("tr"):

    navios_fundi = navios_fundi + 1

print("Numero de Navios Fundeados : ", navios_fundi - 1)


colun1 = 0
colun2 = 1
colun3 = 2
colun4 = 3
colun5 = 4
colun6 = 5
colun7 = 6
colun8 = 7
colun9 = 8
colun10 = 9
colun11 = 10
colun12 = 11

for esp in range(navios_esp):

    try:
        coluna = soup1.find_all("td")

        Navios_Esperando['Berco'].append(coluna[colun1].text)
        Navios_Esperando['IMO'].append(coluna[colun2].text)
        Navios_Esperando['NAVIO'].append(coluna[colun3].text)
        Navios_Esperando['Operacao'].append(coluna[colun4].text)
        Navios_Esperando['Bordo'].append(coluna[colun5].text)
        Navios_Esperando['Comp(m)'].append(coluna[colun6].text)
        Navios_Esperando['DWT'].append(coluna[colun7].text)
        Navios_Esperando['Carga'].append(coluna[colun8].text)
        Navios_Esperando['QTD.CARGA'].append(coluna[colun9].text)
        Navios_Esperando['Calado'].append(coluna[colun10].text)
        Navios_Esperando['Agencia'].append(coluna[colun11].text)
        Navios_Esperando['Ultima_Atualizao'].append(coluna[colun12].text)

        colun1 = colun1 + 12
        colun2 = colun2 + 12
        colun3 = colun3 + 12
        colun4 = colun4 + 12
        colun5 = colun5 + 12
        colun6 = colun6 + 12
        colun7 = colun7 + 12
        colun8 = colun8 + 12
        colun9 = colun9 + 12
        colun10 = colun10 + 12
        colun11 = colun11 + 12
        colun12 = colun12 + 12

    except:
        pass
    
df = pd.DataFrame(list(zip(Navios_Esperando['Berco'], Navios_Esperando['IMO'], Navios_Esperando['NAVIO'], Navios_Esperando['Operacao'], Navios_Esperando['Bordo'], Navios_Esperando['Comp(m)'], Navios_Esperando['DWT'],
                  Navios_Esperando['Carga'], Navios_Esperando['QTD.CARGA'], Navios_Esperando['Calado'], Navios_Esperando['Agencia'], Navios_Esperando['Ultima_Atualizao'])), columns=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"])
df.to_csv("/home/aline/Documentos/PROJETO_3/dados_dos_navios_esperando.csv", index=False)
# print(df)
print("Dados dos Navios - Esperando Salvos")

colun1 = 0
colun2 = 1
colun3 = 2
colun4 = 3
colun5 = 4
colun6 = 5
colun7 = 6
colun8 = 7
colun9 = 8
colun10 = 9


for esp in range(navios_fundi):

    try:
        coluna = soup3.find_all("td")

        #Navios_Fundeados['Berco'].append(coluna[colun1].text)
        Navios_Fundeados['IMO'].append(coluna[colun1].text)
        Navios_Fundeados['NAVIO'].append(coluna[colun2].text)
        Navios_Fundeados['Operacao'].append(coluna[colun3].text)
        #Navios_Fundeados['Bordo'].append(coluna[colun5].text)
        Navios_Fundeados['Comp(m)'].append(coluna[colun4].text)
        Navios_Fundeados['DWT'].append(coluna[colun5].text)
        Navios_Fundeados['Carga'].append(coluna[colun6].text)
        Navios_Fundeados['QTD.CARGA'].append(coluna[colun7].text)
        Navios_Fundeados['Calado'].append(coluna[colun8].text)
        Navios_Fundeados['Agencia'].append(coluna[colun9].text)
        Navios_Fundeados['Ultima_Atualizao'].append(coluna[colun10].text)

        colun1 = colun1 + 10
        colun2 = colun2 + 10
        colun3 = colun3 + 10
        colun4 = colun4 + 10
        colun5 = colun5 + 10
        colun6 = colun6 + 10
        colun7 = colun7 + 10
        colun8 = colun8 + 10
        colun9 = colun9 + 10
        colun10 = colun10 + 10
        


    except:
        pass
    
df = pd.DataFrame(list(zip( Navios_Fundeados['IMO'], Navios_Fundeados['NAVIO'], Navios_Fundeados['Operacao'], Navios_Fundeados['Comp(m)'], Navios_Fundeados['DWT'],
                  Navios_Fundeados['Carga'], Navios_Fundeados['QTD.CARGA'], Navios_Fundeados['Calado'], Navios_Fundeados['Agencia'], Navios_Fundeados['Ultima_Atualizao'])), columns=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
df.to_csv("/home/aline/Documentos/PROJETO_3/dados_dos_navios_fundeados.csv", index=False)
# print(df)
print("Dados dos Navios -  Fundeados Salvos")

colun1 = 0
colun2 = 1
colun3 = 2
colun4 = 3
colun5 = 4
colun6 = 5
colun7 = 6
colun8 = 7
colun9 = 8
colun10 = 9
colun11 = 10


for esp in range(navios_atrac):

    try:
        coluna = soup2.find_all("td")

        #Navios_Atracados['Berco'].append(coluna[colun1].text)
        Navios_Atracados['IMO'].append(coluna[colun1].text)
        Navios_Atracados['NAVIO'].append(coluna[colun2].text)
        Navios_Atracados['Operacao'].append(coluna[colun3].text)
        #Navios_Atracados['Bordo'].append(coluna[colun5].text)
        Navios_Atracados['Comp(m)'].append(coluna[colun4].text)
        Navios_Atracados['DWT'].append(coluna[colun5].text)
        Navios_Atracados['Carga'].append(coluna[colun6].text)
        Navios_Atracados['QTD.CARGA'].append(coluna[colun7].text)
        Navios_Atracados['Calado'].append(coluna[colun8].text)
        Navios_Atracados['Agencia'].append(coluna[colun9].text)
        Navios_Atracados['Prev de Chegada'].append([colun10].text)
        Navios_Atracados['Ultima_Atualizao'].append(coluna[colun11].text)

        colun1 = colun1 + 11
        colun2 = colun2 + 11
        colun3 = colun3 + 11
        colun4 = colun4 + 11
        colun5 = colun5 + 11
        colun6 = colun6 + 11
        colun7 = colun7 + 11
        colun8 = colun8 + 11
        colun9 = colun9 + 11
        colun10 = colun10 + 11
        colun11 = colun11 + 11
      


    except:
        pass
       


df = pd.DataFrame(list(zip(Navios_Atracados['IMO'], Navios_Atracados['NAVIO'], Navios_Atracados['Operacao'], Navios_Atracados['Comp(m)'], Navios_Atracados['DWT'],
                  Navios_Atracados['Carga'], Navios_Atracados['QTD.CARGA'], Navios_Atracados['Calado'], Navios_Atracados['Agencia'],Navios_Atracados['Prev de Chegada'], Navios_Atracados['Ultima_Atualizao'])), columns=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"])
df.to_csv("/home/aline/Documentos/PROJETO_3/dados_dos_navios_atracados.csv", index=False)
# print(df)
print("Dados dos Navios - Atracados Salvos")
