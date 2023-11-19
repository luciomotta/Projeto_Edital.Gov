"""
#PARA SABER SE O SITE PERMITE QUE VOCÊ MEXA COM ROBO COLOQUE
          AO FINAL DO LIIIIIINK /robots.txt
abrir o PROMPT ANACONDA ----> Pip install selenium & o pip install webdriver-manager
NO TOPO DO CÓDIGO
from time import sleep
import time

3Linhas de código p criar uma web no SELENIUM"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time 
servico = Service(ChromeDriverManager().install()) #Instalar a versão certa sozinha
navegador = webdriver.Chrome(service=servico) #----> Abrir navegador

#Entrar no Navegador
link = 'https://sso.acesso.gov.br'
navegador.get(url=link)
#passo2
navegador.maximize_window()
time.sleep(1)
# Encontra elementos pelo ID
elementos = navegador.find_elements(by='xpath', value='//*[@id="accountId"]')

# Verifica se pelo menos um elemento foi encontrado
if elementos:
    # Clica no primeiro elemento encontrado
    elementos[0].send_keys('05693833151')
else:
    print("Nenhum elemento encontrado com o ID especificado.")

elementos = navegador.find_elements(by='xpath', value='//*[@id="login-button-panel"]/button')
elementos[0].click()
time.sleep(2)
elementos = navegador.find_elements(by='xpath', value='//*[@id="password"]')
elementos[0].send_keys('90405Mae.')
elementos = navegador.find_elements(by='xpath', value='//*[@id="submit-button"]')
elementos[0].click()
time.sleep(60)

pass