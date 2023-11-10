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
from unidecode import unidecode
import json





class havadurumuxScrubbing():
    

    
    
    #illeri çekme işlemi
    def illeriCek(self,driver):
        try:
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
        except:
            return False
        return True
        
        
        
        
    
   
    def sicakliklariCek(self,driver):
        
        with open("iller.txt", "r", encoding="utf-8") as dosya:
            gelendeneme=dosya.readline()
        
        def turkish_to_english(text):
            return unidecode(text)
        
        
        illerListesi=gelendeneme.split(";")
        illerListesi.pop()
        
        with open("illerPlakaKodlari.json", "r", encoding="utf-8") as json_dosya:
            illerinPlakalari = json.load(json_dosya)
        
        
        def veri_ekle(havaDurumuVerileri,plaka, sayac, yuksek_sicaklik, dusuk_sicaklik):
            if plaka not in havaDurumuVerileri:
                havaDurumuVerileri[plaka] = {}
            havaDurumuVerileri[plaka][sayac] = {"yuksek_sicaklik": yuksek_sicaklik, "dusuk_sicaklik": dusuk_sicaklik}
        
        
        
        havaDurumuVerileri={}
        for ilCek in illerListesi:
            try:
                il=ilCek
                ilCek=turkish_to_english(ilCek)
              
                driver.get('https://www.havadurumux.net/%s-hava-durumu/'%ilCek)
                #htmlKodu=driver.page_source
                havaVerileri=driver.find_element_by_id("hor-minimalist-a").text.split("\n")
                havaVerileri.pop(0)
                havaVerileri=havaVerileri[0:14]
                
                
                plaka=""
                
                for plakaIcin in illerinPlakalari["iller"]:
                    if plakaIcin["il"]==il:
                        plaka=plakaIcin["plaka"]
                        break
                    
                if plaka=="":
                    print("plaka bulunamadı")
                    continue
            
                print("plaka %s il %s"%(plaka,ilCek))
                
                sayac=0
                for dereceler in havaVerileri:
                    if "°" in dereceler:
                        yuksek=dereceler.split(" ")[0].replace("°","")
                        dusuk=dereceler.split(" ")[1].replace("°","")
                        veri_ekle(havaDurumuVerileri,plaka, sayac, yuksek, dusuk)
                        
                        #print(havaDurumuVerileri)
            
                        sayac+=1
                time.sleep(2)
            except:
                return False
        
        
        with open("havaDurumuxHavaDurumuVerileri.json", "w") as json_dosya:
            json.dump(havaDurumuVerileri, json_dosya)
            
        return True
        
        return havaDurumuVerileri
                
    
