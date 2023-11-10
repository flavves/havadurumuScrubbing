# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 15:09:11 2023

@author: okmen
"""

import json
from datetime import datetime, timezone, timedelta

from pymongo import MongoClient

class mongoDBConnect():
    
    def mongoDBYukle(self):
        # MongoDB'ye bağlan
        client = MongoClient('mongodb://localhost:27017/')
        
        # Veritabanı seç
        db = client['batuhan_okmen']
        
        # Bir koleksiyon oluştur
        collection = db['havaDurumu']
        
        #burada işleme yapacağız
        
        
        with open("havaDurumuxHavaDurumuVerileri.json", "r", encoding="utf-8") as json_dosya:
            havaDurumuxHavaDurumuVerileri = json.load(json_dosya)
        
        with open("weatherComHavaDurumuVerileri.json", "r", encoding="utf-8") as json_dosya:
            weatherComHavaDurumuVerileri = json.load(json_dosya)
        
        with open("metofficeHavaDurumuVerileri.json", "r", encoding="utf-8") as json_dosya:
            metofficeHavaDurumuVerileri = json.load(json_dosya)
        
        
        
        yedi_gun_tarih=[]
        bugun = datetime.now(timezone.utc)
        
        # Bugünden başlayarak 7 gün sonrasına kadar olan tarihleri oluştur
        for gun in range(8):
            belirli_tarih = bugun + timedelta(days=gun)
            formatli_tarih = belirli_tarih.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "+00:00"
            yedi_gun_tarih.append(formatli_tarih)
        
        
        for plakaNo in range(1,82):
            try:
                yuklenecekJson={}
                
                
                try:
                    havaDurumux=havaDurumuxHavaDurumuVerileri[str(plakaNo)] 
                except:
                    havaDurumux={}
                    pass
                
                try:
                    weatherCom=weatherComHavaDurumuVerileri[str(plakaNo)]
                except:
                    weatherCom={}
                    pass
                try:
                    metoffice=metofficeHavaDurumuVerileri[str(plakaNo)]
                except:
                    metoffice={}
                    pass
                
                
                for sirasi in range(0,7):
            
                    
                    try:
                        try:
                            havaDurumux_yuksek=float(havaDurumux[str(sirasi)]["yuksek_sicaklik"])    
                        except:
                            havaDurumux_yuksek=-99.99
                        try:
                            havaDurumux_dusuk=float(havaDurumux[str(sirasi)]["dusuk_sicaklik"])
                        except:
                            havaDurumux_dusuk=-99.99
                    except:
                        havaDurumux_yuksek=-99.99
                        havaDurumux_dusuk=-99.99
                        
                        
                    try:
                        try:
                            weatherCom_yuksek=float(weatherCom[str(sirasi)]["yuksek_sicaklik"]  )      
                        except:
                            weatherCom_yuksek=-99.99
                        try:
                            weatherCom_dusuk=float(weatherCom[str(sirasi)]["dusuk_sicaklik"])
                        except:
                            weatherCom_dusuk=-99.99
                    except:
                        weatherCom_yuksek=-99.99
                        weatherCom_dusuk=-99.99
                        
                        
                        
                    
                    try:
                        try:
                            metoffice_yuksek=float(metoffice[str(sirasi)]["yuksek_sicaklik"])        
                        except:
                            metoffice_yuksek=-99.99
            
                        try:
                            metoffice_dusuk=float(metoffice[str(sirasi)]["dusuk_sicaklik"])
                        except:
                            metoffice_dusuk=-99.99
                    except:
                        metoffice_yuksek=-99.99
                        metoffice_dusuk=-99.99
                        
                        
                        
               
                    
                    data = {'provincial_plate': plakaNo, 'date': yedi_gun_tarih[sirasi],
                            'weather':
                                {"metoffice":
                                 {"up":metoffice_yuksek,"low":metoffice_dusuk},
                                 "weather_com":{"up":weatherCom_yuksek,"low":weatherCom_dusuk},
                                 "havadurumux":{"up":havaDurumux_yuksek,"low":havaDurumux_dusuk}}}
                    
                    
                    collection.insert_one(data)
            except:
                return False
        return True    
        
        
            
    
    
    
    




















