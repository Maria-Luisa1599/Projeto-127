from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from bs4 import BeautifulSoup
import time

start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser = webdriver.Chrome("C:/Users/Juinior/Desktop/Maria/PYTHON/Aula 127/chromedriver.exe")
scrape_data = []

browser.get(start_url)
time.sleep(10)

def scrape():
    soup = BeautifulSoup(browser.page_source, "html.parser")

    bright_star_table = soup.find("table", attrs={"class", "wikitable"})
    table_body = bright_star_table.find('tbody')
    table_rows = table_body.find_all('tr')
    
    for row in table_rows:
        table_cols = row.find_all('td')
        row_data = []
        for col_data in table_cols:
            data = col_data.text.strip()
            print(data)
            row_data.append(data)
        scrape_data.append(row_data)
            
scrape()

stars_data = []

for i in range(0, len(scrape_data)):
    nome = scrape_data[i][1]
    distancia = scrape_data[i][3]
    massa = scrape_data[i][5]
    raio = scrape_data[i][6]
    luminosidade = scrape_data[i][7]
    
    required_data = [nome, distancia, massa, raio, luminosidade]
    stars_data.append(required_data)

headers = ["NOME", "DISTÂNCIA", "MASSA", "RAIO", "LUMINOSIDADE"]

df = pd.DataFrame(stars_data, columns=headers)
df.to_csv('scraped_data.csv', index = True, index_label="id")
