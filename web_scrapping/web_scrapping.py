import time
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json

# 1. Pegar conteúdo HTML a partir da URL
url = "https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2021"

option = Options()
option.headless = False #  Oculta a execução do anvegador
driver = webdriver.Firefox(options=option)

driver.get(url)

driver.find_element_by_xpath("/html[1]/body[1]/div[1]/header[1]/div[1]/nav[1]/ul[1]/li[3]").click()
driver.implicitly_wait(15)
# driver.find_element_by_xpath("/html[1]/body[1]/div[1]/header[1]/div[1]/nav[1]/ul[1]/li[3]/div[1]/ul[1]/li[2]")
# driver.implicitly_wait(15)

time.sleep(10)


# 2. Parsear o conteúdo HTML - BeautifulSoup
# 3. Estruturar coteúdo em Data Frame - Pandas
# 4. Transformar os Dados em um dicionário de dados próprio
# 5. Converter e salvar em arquivo JSON
driver.quit()