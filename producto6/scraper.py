#!/usr/bin/env python
# coding: utf-8

# # Librerias

# In[1]:


from bs4 import BeautifulSoup
import datetime
from lxml import etree
import openpyxl
import os
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time
from urllib.request import urlopen
from webdriver_manager.chrome import ChromeDriverManager
import xml.etree.ElementTree as ETree


# # Carpeta para el Producto

# In[2]:


# Creamos carpeta para el Producto Analizado
CurrentDirectory = os.getcwd()
CurrentDirectoryFolder = CurrentDirectory + '\\' + 'output' #PARAMETRO_NOMBRE


# In[3]:


# Ve si existe la carpeta del Producto Analizado, o la crea

if os.path.exists(CurrentDirectoryFolder) == True:
    print('Existe')
else:
    os.makedirs(CurrentDirectoryFolder)
    print('Creada, ahora existe')


# # Parametros para Selenium

# In[4]:


# definir ruta_descarga a gusto
ruta_descarga = CurrentDirectoryFolder 

options = Options()
options.add_experimental_option("prefs", {
  "download.default_directory": ruta_descarga, #Donde descargara
  "download.prompt_for_download": False,
  "download.directory_upgrade": True
})

options.add_argument("--headless")

#https://stackoverflow.com/questions/46937319/how-to-use-chrome-webdriver-in-selenium-to-download-files-in-python
#https://stackoverflow.com/questions/53657215/running-selenium-with-headless-chrome-webdriver


# In[5]:


# Initiate the browser
browser  = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)


# # Navegacion y Descarga

# In[6]:


# Open the Website
browser.get('https://www.investing.com/equities/falabella')


# Open the Website
# browser.get('https://www.investing.com/')

# Matar el popup
# try:
#     WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "i.popupCloseIcon.largeBannerCloser"))).click()
# except TimeoutException as to:
#     print(to)

# Buscaremos la empresa que nos interesa
# browser.find_element(By.XPATH, '/html/body/div[5]/header/div[1]/div/div[3]/div[1]/input').send_keys('FALABELLA')
# browser.find_element(By.XPATH, '/html/body/div[5]/header/div[1]/div/div[3]/div[1]/input').send_keys(Keys.ENTER)
# time.sleep(5)

# # Navegacion

# In[7]:


# Baja una Pantalla
browser.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)


# In[8]:


# Ingresa a Data Historica

try:
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/div/div/div[2]/main/div/div[7]/nav/ul/li[3]/a'))).click()
except TimeoutException as to:
    print(to)
    WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/main/div/div[7]/nav/ul/li[3]/a'))).click()
    
#browser.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div[2]/main/div/div[7]/nav/ul/li[3]/a').click()

#/html/body/div/div[2]/div/div/div[2]/main/div/div[7]/nav/ul/li[3]/a
#/html/body/div[1]/div/div/div/div[2]/main/div/div[7]/nav/ul/li[3]/a

#browser.find_element(By.XPATH, '/html/body/div/div[1]/header/div[3]/div/div/div/div/form/div[1]/button').click()


# In[9]:


# Baja una Pantalla
browser.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)


# In[10]:


# Matar el otro popup

try:
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/header/div[3]/div/div/div/div/form/div[1]/button'))).click()
except TimeoutException as to:
    print(to)
    WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/header/div[3]/div/div/div/div/form/div[1]/button'))).click()
    
#browser.find_element(By.XPATH, '/html/body/div/div[1]/header/div[3]/div/div/div/div/form/div[1]/button').click()


# In[11]:


# Click en el buscador de fechas

try:
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/div/div/div[2]/main/div/div[8]/div/div/div[2]/div[2]/div[2]/div/div[2]'))).click()
except TimeoutException as to:
    print(to)
    WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/main/div/div[8]/div/div/div[2]/div[2]/div[2]/div/div[2]'))).click()

#browser.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div[2]/main/div/div[8]/div/div/div[2]/div[2]/div[2]/div/div[2]').click()


# In[12]:


# Pasos para forzar 01-01-2022
# Si se quiere buscar Febrero 2022 -> 01/02/2022
time.sleep(5)

browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/main/div/div[8]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/input').click()
browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/main/div/div[8]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/input').clear()
browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/main/div/div[8]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/input').send_keys('01/01/2022')
browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/main/div/div[8]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/input').click()
browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/main/div/div[8]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/input').send_keys('01/01/2022')
browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/main/div/div[8]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/input').click()

browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/main/div/div[8]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/input').click()
browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/main/div/div[8]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/input').clear()
browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/main/div/div[8]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/input').send_keys('01/01/2022')
browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/main/div/div[8]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/input').click()
browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/main/div/div[8]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/input').send_keys('01/01/2022')
browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/main/div/div[8]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/input').click()

#/html/body/div/div[2]/div/div/div[2]/main/div/div[8]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/input
#/html/body/div[1]/div/div/div/div[2]/main/div/div[8]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/input


# In[13]:


try:
    WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/div/div/div[2]/main/div/div[8]/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/button'))).click()
except TimeoutException as to:
    print(to)
    WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/main/div/div[8]/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/button'))).click()   
#/html/body/div/div[2]/div/div/div[2]/main/div/div[8]/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/button
#/html/body/div[1]/div/div/div/div[2]/main/div/div[8]/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/button


# # Scrapear Tabla
# 
# Con el Navegador ya abierto e interactuado

# In[14]:


time.sleep(15)
#browser.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.PAGE_DOWN)
#browser.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.PAGE_DOWN)
#browser.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.PAGE_DOWN)
#browser.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.PAGE_DOWN)
#browser.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div[2]/main/div/div[8]/div/div/div[3]/div/table/tbody').click()


# In[15]:


source = browser.page_source


# In[16]:


content_page = BeautifulSoup(source, "html.parser")


# In[17]:


# dom = etree.HTML(str(content_page))


# In[18]:


# la ruta es: //*[@id="__next"]/div[2]/div/div/div[2]/main/div/div[8]/div/div/div[3]/div/table/tbody
# El //text() es para que me regrese todos los textos
# datos = dom.xpath('//*[@id="__next"]/div[2]/div/div/div[2]/main/div/div[8]/div/div/div[3]/div/table/tbody//text()')


# In[19]:


# Extraemos la tabla y la guardamos en una lista
contador = 0

valores = content_page.find_all('tbody', {'class':'datatable_body__3EPFZ'})

for valor in valores[1]: #Es la segunda la que nos interesa
    for val in valor:
        
        contador = contador + 1
    
        if contador == 1:
            Raw_Data = pd.DataFrame({'valor':val.get_text()}, index=[contador-1])
        else:
            Raw_Data = pd.concat([Raw_Data, pd.DataFrame({'valor':val.get_text()}, index=[contador-1]) ])
        
        #print(val.get_text())


# In[20]:


# Separamos la lista anterior en un dataframe trabajable
i = 0
j = 0

iteraciones = int(len(Raw_Data)/7)


cols = ['Date', 'Price', 'Open', 'High', 'Low', 'Vol', 'ChangePercent']
datos_df = pd.DataFrame(columns=cols, index=range(iteraciones))

while iteraciones > j:

    datos_df.loc[j].Date = Raw_Data.valor.loc[i + 0]
    datos_df.loc[j].Price = Raw_Data.valor.loc[i + 1]
    datos_df.loc[j].Open = Raw_Data.valor.loc[i + 2]
    datos_df.loc[j].High = Raw_Data.valor.loc[i + 3]
    datos_df.loc[j].Low = Raw_Data.valor.loc[i + 4]
    datos_df.loc[j].Vol = Raw_Data.valor.loc[i + 5]
    datos_df.loc[j].ChangePercent = Raw_Data.valor.loc[i + 6]
                      
    i = i + 7
    j = j + 1


# In[21]:


# Limpiaremos la Informacion
datos_df_limpio = datos_df.copy()


# In[22]:


datos_df_limpio['Date'] = pd.to_datetime(datos_df_limpio['Date'].astype(str) , format= '%m/%d/%Y')
datos_df_limpio['Price'] = datos_df_limpio['Price'].str.replace(',','').astype('float')
datos_df_limpio['Open'] = datos_df_limpio['Open'].str.replace(',','').astype('float')
datos_df_limpio['High'] = datos_df_limpio['High'].str.replace(',','').astype('float')
datos_df_limpio['Low'] = datos_df_limpio['Low'].str.replace(',','').astype('float')
datos_df_limpio['ChangePercent'] = datos_df_limpio['ChangePercent'].str.replace('%','').astype('float')


# In[23]:


datos_df_limpio


# In[24]:


#Exportamos Resultado -- Cambiar Ruta a ruta del proyecto

datos_df_limpio.to_csv(CurrentDirectoryFolder + '\\' + 'FALABELLA.csv', index=False, sep=';') #PARAMETRO_NOMBRE

#import openpyxl
#datos_df_limpio.to_excel(CurrentDirectoryFolder + '\\' + 'FALABELLA.xlsx', index=False) #PARAMETRO_NOMBRE


# In[25]:


# Limpiamos por espacio
del Raw_Data
del datos_df
del datos_df_limpio


# In[26]:


browser.close()

