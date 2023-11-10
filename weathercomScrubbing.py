# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 13:33:43 2023

@author: okmen
"""

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

chrome_options = Options()
#chrome_options.add_argument("--headless")
driver = webdriver.Chrome(executable_path=r'chromedriver.exe',chrome_options=chrome_options)

headers = {
    "User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
}



driver.get("https://weather.com/tr-TR/")
session_id = driver.session_id
session_cookies = driver.get_cookies()



def illeriCek():
    with open("iller.txt", "r", encoding="utf-8") as dosya:
        iller=dosya.readline()
    return iller


iller=illeriCek()
illerListesi=iller.split(";")
illerListesi.pop()


fonksiyonlar=seleniumFonksiyonlari.seleniumFonksiyonlari()

#illerin session code degerlerini cekmemiz gerekiyor.

def illerinSessionCodeDegerleriniCek():
    sehirlerinSessionDegerleri={}
    #LocationSearch_input
    degisken="LocationSearch_input"
    sure=30
    driver.get("https://weather.com/tr-TR/")
    sonSehirText=""
    for il in illerListesi:  
        keys=il
        element=fonksiyonlar.idElementDondur(degisken, sure, driver)
        driver.execute_script("arguments[0].value = '';", element)
        fonksiyonlar.tiklaIdKeys(degisken, sure, keys, driver)
        time.sleep(0.1)
        onay=True      
        while onay:
            try:
                element=fonksiyonlar.idElementDondur("LocationSearch_listbox", sure, driver)
                
                ilkSehir = element.find_elements_by_tag_name("button")[0]
                ilkSehir_text = ilkSehir.get_attribute("id").split("-")[1]
                if len(ilkSehir_text)>5: 
                    if sonSehirText !=ilkSehir_text:
                        sehirlerinSessionDegerleri[il] = ilkSehir_text
                        sonSehirText=ilkSehir_text
                        onay=False
                        
            except :
                onay=True  

        time.sleep(1)
    with open("weathercomIllerSessionCode.json", "w") as json_dosya:
        json.dump(sehirlerinSessionDegerleri, json_dosya)
    




with open("illerPlakaKodlari.json", "r", encoding="utf-8") as json_dosya:
    illerinPlakalari = json.load(json_dosya)


def veri_ekle(havaDurumuVerileri,plaka, sayac, yuksek_sicaklik, dusuk_sicaklik):
    if plaka not in havaDurumuVerileri:
        havaDurumuVerileri[plaka] = {}
    havaDurumuVerileri[plaka][sayac] = {"yuksek_sicaklik": yuksek_sicaklik, "dusuk_sicaklik": dusuk_sicaklik}




        
def yediGunlukVeriCek():
    with open("weathercomIllerSessionCode.json", "r") as json_dosya:
        okunan_sozluk = json.load(json_dosya)
    
    for il in okunan_sozluk:    
        
        print(okunan_sozluk[il])
        
        url="https://weather.com/tr-TR/weather/tenday/l/%s"%okunan_sozluk[il] 
        driver.get(url)
        
        
        fonksiyonlar.tiklaName("caret-up", 30, driver)
        
        #id 
        
        for plakaIcin in illerinPlakalari["iller"]:
            if plakaIcin["il"]==il:
                plaka=plakaIcin["plaka"]
    
        havaDurumuVerileri={}
        
        sayac=0
        
        for i in range(0,7):
            element=fonksiyonlar.idElementDondur("detailIndex"+str(i), 3, driver)
            yuksek=element.text.split("\n")[2].replace("°","")
            dusuk=element.text.split("\n")[3].replace("°","").replace("/","")
            
            veri_ekle(havaDurumuVerileri,plaka, sayac, yuksek, dusuk)

            sayac+=1
            
    return havaDurumuVerileri
            
        
        











