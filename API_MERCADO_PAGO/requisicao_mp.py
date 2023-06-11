##Script para Retirar Dados Bancarios pelo Mercado Pago

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.mercadopago.com.br/')
email = ''
senha = ''
time.sleep(3)


entrar_na_conta = driver.find_element("xpath",'/html/body/header/div/div/nav/div/div[2]/a[1]')
time.sleep(5)
entrar_na_conta.click()
time.sleep(5)
campo_email = driver.find_element("xpath",'//*[@id="user_id"]').send_keys(email)
time.sleep(5)
continuar = driver.find_element("xpath",'//*[@id="login_user_form"]/div[2]/button').click()
time.sleep(5)
recaptchar = driver.find_element("xpath", '//*[@id="recaptcha-anchor"]').click()
time.sleep(20)
#campo_senha = driver.find_element("xpath",'//*[@id="password"]').send_keys(senha)
#time.sleep(5)
#entrar = driver.find_element("xpath",'//*[@id="action-complete"]').click()
#time.sleep(5)
#whatsapp = driver.find_element("xpath",'//*[@id="channel-whatsapp"]').click()
#time.sleep(2)
#//*[@id="recaptcha-anchor"]

  
