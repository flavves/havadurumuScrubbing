# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 15:05:51 2023

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
from unidecode import unidecode


class metoOfficeScrubbing():

  
    
    def illerinSessionCodeDegerleriniCek(self,driver):
        
        def illeriCek():
            with open("iller.txt", "r", encoding="utf-8") as dosya:
                iller=dosya.readline()
            return iller
        
        
        iller=illeriCek()
        illerListesi=iller.split(";")
        illerListesi.pop()
        
        def turkish_to_english(text):
            return unidecode(text)
        
        sehirlerinSessionDegerleri={}
        #LocationSearch_input
        degisken="location-search-input"
        sure=30
        driver.get("https://www.metoffice.gov.uk/weather/world/turkey/list")
        sonSehirText=""
        print("json yazılıyor")
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
                    #print(il)
                    
                    href_value = link.find_element_by_tag_name('a').get_attribute('href').split("/")[-1]
                    #print(href_value)
                    sehirlerinSessionDegerleri[il] = href_value
           
        with open("metofficeIllerSessionCode.json", "w") as json_dosya:
            json.dump(sehirlerinSessionDegerleri, json_dosya)
        
        print("json yazıldı")
            
        return True
                
    
    
    
    def yediGunlukVeriCek(self,driver):
        
        def turkish_to_english(text):
            return unidecode(text)
        
        def veri_ekle(havaDurumuVerileri,plaka, sayac, yuksek_sicaklik, dusuk_sicaklik):
            if plaka not in havaDurumuVerileri:
                havaDurumuVerileri[plaka] = {}
            havaDurumuVerileri[plaka][sayac] = {"yuksek_sicaklik": yuksek_sicaklik, "dusuk_sicaklik": dusuk_sicaklik}
        
        with open("illerPlakaKodlari.json", "r", encoding="utf-8") as json_dosya:
            illerinPlakalari = json.load(json_dosya)
        
        with open("metofficeIllerSessionCode.json", "r") as json_dosya:
            okunan_sozluk = json.load(json_dosya)
        
        havaDurumuVerileri={}
        
        for ilCek in okunan_sozluk:    
            
            try:
                url="https://www.metoffice.gov.uk/weather/forecast/%s"%okunan_sozluk[ilCek] 
                driver.get(url)
                source=driver.page_source
                veriler=source.split("dayNav")[1].split("tabDay7")[0].split('class="tab-inner">')
                veriler.pop(0)
                
                il=ilCek
                plaka=""
                for plakaIcin in illerinPlakalari["iller"]:
                    if turkish_to_english(plakaIcin["il"])==il:
                        plaka=plakaIcin["plaka"]
                        break
                    
                if plaka=="":
                    print("plaka bulunamadı")
                    continue
                
                sayac=0
                
                print("plaka %s il %s"%(plaka,ilCek))
                
                
                for veri in veriler:
                    dereceler=veri.split('<span data-value=')
                    yuksek=dereceler[1].split('"')[1]
                    dusuk=dereceler[2].split('"')[1]
                    
                    veri_ekle(havaDurumuVerileri,plaka, sayac, yuksek, dusuk)
        
                    sayac+=1
            except:
                return False
            
        with open("metofficeHavaDurumuVerileri.json", "w") as json_dosya:
            json.dump(havaDurumuVerileri, json_dosya)
            
        return True
    
    
