from selenium import webdriver
from datetime import datetime
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.chrome.options import Options
import psycopg2 as pg
from psycopg2 import OperationalError

discionario = {
    "horario": [],
    "valor_site": [],
    "data": [],
    "hora": [],
    "cotacao_decimal": [],  
}

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options = chrome_options)
 
driver.get("https://www.google.com.br/search?q=d%C3%B3lar")
sleep(2)

elemento = driver.find_element(By.CLASS_NAME, 'SwHCTb')
agora = datetime.now() 
valor = float(elemento.text.replace(',', '.'))

discionario['horario'].append(agora)
discionario['valor_site'].append(valor)  
discionario['cotacao_decimal'].append(valor)
discionario["hora"].append(agora.strftime("%H:%M:%S"))
discionario["data"].append(agora.strftime("%Y-%m-%d"))

df = pd.DataFrame(discionario)

driver.quit()

try:
    conn = pg.connect(
        dbname="defaultdb",
        user="avnadmin",
        password="AVNS_kwaAVMuqTGFk7-vlJrq",
        host="pg-308d5cac-lucalucareli-3bb8.i.aivencloud.com",
        port="11468"
    )
    
    cursor = conn.cursor()
    
    cursor.execute("CALL inserir_valores(%s, %s, %s)", 
                   (agora.strftime("%Y-%m-%d"), agora.strftime("%H:%M:%S"), valor))
    
    conn.commit()

except OperationalError as e:
    print(f"Error: {e}")
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
        
