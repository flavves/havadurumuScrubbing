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
# havadurumux scrubbing
#url 
import seleniumFonksiyonlari
import json
from unidecode import unidecode

chrome_options = Options()
#chrome_options.add_argument("--headless")
driver = webdriver.Chrome(executable_path=r'chromedriver.exe',chrome_options=chrome_options)

headers = {
    "User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
}



driver.get("https://www.metoffice.gov.uk/weather/world/turkey/list")
session_id = driver.session_id
session_cookies = driver.get_cookies()


def turkish_to_english(text):
    return unidecode(text)


def illeriCek():
    with open("iller.txt", "r", encoding="utf-8") as dosya:
        iller=dosya.readline()
    return iller


iller=illeriCek()
illerListesi=iller.split(";")
illerListesi.pop()


fonksiyonlar=seleniumFonksiyonlari.seleniumFonksiyonlari()

#cookie kabul et

fonksiyonlar.tiklaId("ccc-recommended-settings", 30, driver)


#illerin session code degerlerini cekmemiz gerekiyor.


driver



def illerinSessionCodeDegerleriniCek():
    sehirlerinSessionDegerleri={}
    #LocationSearch_input
    degisken="location-search-input"
    sure=30
    driver.get("https://www.metoffice.gov.uk/weather/world/turkey/list")
    sonSehirText=""
    
    illerMetOffice=driver.find_element_by_class_name("search-results").text
    illerMetOffice=illerMetOffice.split("\n")
    yeniIllerListesi=[]
    for metOfficeIl in illerMetOffice:
        for il in illerListesi:
            if turkish_to_english(il) == metOfficeIl:
                yeniIllerListesi.append(metOfficeIl)
                
                
    illerMetOfficeClass=driver.find_element_by_class_name("search-results")
    linkler = illerMetOfficeClass.find_elements_by_tag_name("li")
    for il in yeniIllerListesi:
        for link in linkler:       
            if il== link.text:
                print(il)
                
                href_value = link.find_element_by_tag_name('a').get_attribute('href').split("/")[-1]
                print(href_value)
                sehirlerinSessionDegerleri[il] = href_value
       
    with open("metofficeIllerSessionCode.json", "w") as json_dosya:
        json.dump(sehirlerinSessionDegerleri, json_dosya)
            

def yediGunlukVeriCek():
    with open("metofficeIllerSessionCode.json", "r") as json_dosya:
        okunan_sozluk = json.load(json_dosya)
    
    for il in okunan_sozluk:    
        
        print(okunan_sozluk[il])
        
        url="https://www.metoffice.gov.uk/weather/forecast/%s"%okunan_sozluk[il] 
        driver.get(url)
        source=driver.page_source
        veriler=source.split("dayNav")[1].split("tabDay7")[0].split('class="tab-inner">')
        veriler.pop(0)
        
        for veri in veriler:
            dereceler=veri.split('<span data-value=')
            yuksek=dereceler[1].split('"')[1]
            dusuk=dereceler[2].split('"')[1]

            print(yuksek)
            print(dusuk)




