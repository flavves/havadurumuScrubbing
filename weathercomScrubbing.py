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


class weatherComScrubbing:
    
    
    def illerinSessionCodeDegerleriniCek(self,driver):
        fonksiyonlar=seleniumFonksiyonlari.seleniumFonksiyonlari()
        
        def illeriCek():
            with open("iller.txt", "r", encoding="utf-8") as dosya:
                iller=dosya.readline()
            return iller
        
        
        iller=illeriCek()
        illerListesi=iller.split(";")
        illerListesi.pop()
        
        sehirlerinSessionDegerleri={}
        #LocationSearch_input
        degisken="LocationSearch_input"
        sure=30
        driver.get("https://weather.com/tr-TR/")
        sonSehirText=""
        for il in illerListesi:  
            try:
                keys=il
                element=fonksiyonlar.idElementDondur(degisken, sure, driver)
                driver.execute_script("arguments[0].value = '';", element)
                driver.execute_script("arguments[0].value = '';", element)
                time.sleep(0.5)
                fonksiyonlar.tiklaIdKeys(degisken, sure, keys, driver)
                time.sleep(0.5)
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
                print("---------------------------")
                #print(sehirlerinSessionDegerleri)   
                time.sleep(1)
            except:
                return False
        with open("weathercomIllerSessionCode.json", "w") as json_dosya:
            json.dump(sehirlerinSessionDegerleri, json_dosya)
            
        return True
    
    
 
    
    
    
    
            
    def yediGunlukVeriCek(self,driver):
        
        fonksiyonlar=seleniumFonksiyonlari.seleniumFonksiyonlari()
        
        with open("illerPlakaKodlari.json", "r", encoding="utf-8") as json_dosya:
            illerinPlakalari = json.load(json_dosya)
        
        
        def veri_ekle(havaDurumuVerileri,plaka, sayac, yuksek_sicaklik, dusuk_sicaklik):
            if plaka not in havaDurumuVerileri:
                havaDurumuVerileri[plaka] = {}
            havaDurumuVerileri[plaka][sayac] = {"yuksek_sicaklik": yuksek_sicaklik, "dusuk_sicaklik": dusuk_sicaklik}
        
        
        
        
        with open("weathercomIllerSessionCode.json", "r") as json_dosya:
            okunan_sozluk = json.load(json_dosya)
        havaDurumuVerileri={}
      
        for ilCek in okunan_sozluk:   
       
            try:
                
                #print(okunan_sozluk[ilCek])
                time.sleep(1)
                
               
                url="https://weather.com/tr-TR/weather/tenday/l/%s"%okunan_sozluk[ilCek] 
                driver.get(url)
                
               
                fonksiyonlar.tiklaName("caret-up", 30, driver)
                
                #id 
                il=ilCek
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
               
                fonksiyonlar.bekleName("twc-logo", 30, driver)
                
                for i in range(0,7):
                    while 1:
                        time.sleep(0.5)
                        try:
                            element=fonksiyonlar.idElementDondur("detailIndex"+str(i), 3, driver)
                            
                            yuksek=element.text.split("\n")[2].replace("°","")
                            dusuk=element.text.split("\n")[3].replace("°","").replace("/","")
                            
                            try:
                                if "%" in yuksek:
                                    fonksiyonlar.tiklaName("caret-up", 3, driver)
                                    yuksek=element.text.split("\n")[2].replace("°","")
                                    dusuk=element.text.split("\n")[3].replace("°","").replace("/","")
                                
                            except:
                                pass
                            
                            break
                        except:
                            pass
                       
                    veri_ekle(havaDurumuVerileri,plaka, sayac, yuksek, dusuk)
        
                    sayac+=1
                    #print(havaDurumuVerileri)
                
            except:
                pass
                return False
                
        with open("weatherComHavaDurumuVerileri.json", "w") as json_dosya:
            json.dump(havaDurumuVerileri, json_dosya)
            
        return True
  
    
    
    
    
    
