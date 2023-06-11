from selenium import webdriver
import chromedriver_autoinstaller as chromedriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import getpass
import pandas as pd
from bs4 import BeautifulSoup
# other imports
import json
chromedriver.install(cwd=True)

username = getpass.getuser()
options = Options()
options.headless = True
options.add_argument('window-size = 1920x1080')

driver = webdriver.Chrome(options=options)


time.sleep(5)
url = 'https://steamdb.info/'
driver.get(url)


element = driver.find_elements(By.CLASS_NAME, 'span6')

soup = BeautifulSoup(element, 'html.parser')

for table in soup.find_all("tr"):

    jogos = jogos + 1

print("Numero  : ", jogos -1)