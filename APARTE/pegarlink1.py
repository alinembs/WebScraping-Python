from selenium import webdriver
import chromedriver_autoinstaller as chromedriver
from selenium.webdriver.chrome.options import  Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import getpass
import pandas as pd

#other imports
chromedriver.install(cwd=True)


username = getpass.getuser()
options = Options()
options.headless = True
options.add_argument('window-size = 1920x1080')

driver = webdriver.Chrome(options = options)

driver.get("https://sports.sportingbet.com/pt-br/sports/ao-vivo/aposta")

time.sleep(5)

inspect = '//*[@id="main-view"]/ms-live/ms-live-overview/ms-grid[1]'
element = driver.find_element('xpath', f'{inspect}')

html_element = element.get_attribute('outerHTML')

soup = BeautifulSoup(html_element, 'html.parser')
for link in soup.find_all('a'):
    print(link.get('href'))

