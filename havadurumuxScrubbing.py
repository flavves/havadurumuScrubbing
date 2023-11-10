# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 21:58:26 2023

@author: okmen
"""

#kütüphaneler

import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
global session_id,session_cookies
from unidecode import unidecode
import json
# havadurumux scrubbing
#url 
havaDurumuxUrl="https://www.havadurumux.net/api.php?dcr=%23d0d0d0&apr=%23eeeeee&icr=%23d2d2d2&ikap=%23ffffff&fr=%23000000&br=%232f6395&dr=%233570a9&wt=yatay&cityurl=321"

chrome_options = Options()
#chrome_options.add_argument("--headless")
driver = webdriver.Chrome(executable_path=r'chromedriver.exe',chrome_options=chrome_options)

headers = {
    "User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
}
driver.get("https://www.havadurumux.net")
session_id = driver.session_id
session_cookies = driver.get_cookies()

#illeri çekme işlemi
def illeriCek():
    element=driver.find_element_by_xpath('//*[@id="iller"]')
    
    iller=element.text.split("\n")
    iller.pop(0)
    
    illerListesi=[]
    for il in iller:
        il=il.replace(" ","")
        illerListesi.append(il)
    
    
    with open("iller.txt", "w", encoding="utf-8") as dosya:
        for ilYaz in illerListesi:       
            dosya.write(ilYaz+";")
    
    
    

with open("iller.txt", "r", encoding="utf-8") as dosya:
    gelendeneme=dosya.readline()

def turkish_to_english(text):
    return unidecode(text)


illerListesi=gelendeneme.split(";")
illerListesi.pop()

with open("illerPlakaKodlari.json", "r", encoding="utf-8") as json_dosya:
    illerinPlakalari = json.load(json_dosya)


for il in illerListesi:
    driver.get('https://www.havadurumux.net/%s-hava-durumu/'%turkish_to_english(il))
    #htmlKodu=driver.page_source
    havaVerileri=driver.find_element_by_id("hor-minimalist-a").text.split("\n")
    havaVerileri.pop(0)
    havaVerileri=havaVerileri[0:14]
    
    
    for dereceler in havaVerileri:
        if "°" in dereceler:
            yuksek=dereceler.split(" ")[0].replace("°","")
            dusuk=dereceler.split(" ")[1].replace("°","")
        
















