# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 19:53:18 2023

@author: okmen
"""

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




import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox,QMessageBox
global suresayac
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal,Qt

from sistemBaslat_python import Ui_MainWindow


import metoOfficeScrubbing
import weathercomScrubbing
import havadurumuxScrubbing
import mongoDB

global hepsiniAyniAndaBaslat
hepsiniAyniAndaBaslat=False



class MainWindow(QMainWindow):
        def __init__(self):
            super(MainWindow, self).__init__()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            global hepsiniAyniAndaBaslat
        
            self.setWindowTitle("Flavves-Batuhan okmen Hava Durumu Scrubbing- Ozel Proje")
            
            ################
            self.ui.metoOfficeLinkleriAl.clicked.connect(self.metoOfficeScrubbingLinkleriAlButtonClicked)
            
            self.ui.metoOfficeBaslat.clicked.connect(self.metoOfficeBaslatButtonClicked)
            
            self.ui.metoOfficeDurdur.clicked.connect(self.metoOfficeDurdurButtonClicked)
            ################
            
            ################
            self.ui.weatherLinkleriAl.clicked.connect(self.weatherLinkleriAlButtonClicked)
            
            self.ui.weatherBaslat.clicked.connect(self.weatherBaslatButtonClicked)
            
            self.ui.weatherDurdur.clicked.connect(self.weatherDurdurButtonClicked)
            ################
            
            ################
            self.ui.HavadurumuxLinkleriAl.clicked.connect(self.havadurumuxLinkleriAlButtonClicked)
            
            self.ui.HavadurumuxBaslat.clicked.connect(self.havadurumuxBaslatButtonClicked)
            
            self.ui.HavadurumuxDurdur.clicked.connect(self.havadurumuxDurdurButtonClicked)
            
            ################
            self.ui.veriTabaninaYukle.clicked.connect(self.veriTabaninaYukleButtonClicked)
            self.ui.butunSistemleriBaslat.clicked.connect(self.butunSistemleriBaslatButtonClicked)
            self.ui.butunSistemleriDurdur.clicked.connect(self.butunSistemleriDurdurButtonClicked)
            #butunSistemleriBaslat
            
            
            global onay
            onay=0
            try:
                with open("havaDurumuxHavaDurumuVerileri.json", "r", encoding="utf-8") as json_dosya:
                    havaDurumuxHavaDurumuVerileri = json.load(json_dosya)
                    print(len(havaDurumuxHavaDurumuVerileri))
                    if len(havaDurumuxHavaDurumuVerileri)>2:
                        onay+=1
            except:
                pass
            
            try:
                with open("weatherComHavaDurumuVerileri.json", "r", encoding="utf-8") as json_dosya:
                    weatherComHavaDurumuVerileri = json.load(json_dosya)
                    if len(weatherComHavaDurumuVerileri)>2:
                        onay+=1

            except:
                pass
            
            try:
                with open("metofficeHavaDurumuVerileri.json", "r", encoding="utf-8") as json_dosya:
                    metofficeHavaDurumuVerileri = json.load(json_dosya)
                    if len(metofficeHavaDurumuVerileri)>2:
                        onay+=1

            except:
                pass
           
            
            if onay==3:
                self.ui.veriTabaninaYukle.setEnabled(True)
            
            """
            try:
                with open("havaDurumuxHavaDurumuVerileri.json", "r", encoding="utf-8") as json_dosya:
                    havaDurumuxHavaDurumuVerileri = json.load(json_dosya)
                    
                    gelentext=self.ui.havaDurumuxVeriler.text()
                    
                    linkler=gelentext.split("|")[0]
                    havaVerileri=gelentext.split("|")[1].replace("x",str(len(havaDurumuxHavaDurumuVerileri)))
                    self.ui.havaDurumuxVeriler.setText(linkler+havaVerileri)
            except:
                pass
            
            try:
                with open("weatherComHavaDurumuVerileri.json", "r", encoding="utf-8") as json_dosya:
                    weatherComHavaDurumuVerileri = json.load(json_dosya)
                    
                    gelentext=self.ui.weatherComVeriler.text()
                   
                    linkler=gelentext.split("|")[0]
                    havaVerileri=gelentext.split("|")[1].replace("x",str(len(weatherComHavaDurumuVerileri)))
                    self.ui.weatherComVeriler.setText(linkler+havaVerileri)
            except:
                pass
            
            try:
                with open("metofficeHavaDurumuVerileri.json", "r", encoding="utf-8") as json_dosya:
                    metofficeHavaDurumuVerileri = json.load(json_dosya)
                    
                    gelentext=self.ui.metOfficeVeriler.text()
                    
                    linkler=gelentext.split("|")[0]
                    havaVerileri=gelentext.split("|")[1].replace("x",str(len(metofficeHavaDurumuVerileri)))
                    self.ui.metOfficeVeriler.setText(linkler+havaVerileri)
            except:
                pass
            
        """
        
        #################################################    
        
        
        def butunSistemleriBaslatButtonClicked(self):
            global hepsiniAyniAndaBaslat
            LinklerAlinsin=self.ui.linkleriToplasinMiCheckBox.isChecked()
            if LinklerAlinsin:
                hepsiniAyniAndaBaslat=True
                self.ui.HavadurumuxLinkleriAl.click()
                self.ui.weatherLinkleriAl.click()
                self.ui.metoOfficeLinkleriAl.click()
            else:
                self.ui.HavadurumuxBaslat.click()
                self.ui.weatherBaslat.click()
                self.ui.metoOfficeBaslat.click()
            
        
        
        def butunSistemleriDurdurButtonClicked(self):
            self.ui.HavadurumuxDurdur.click()
            self.ui.weatherDurdur.click()
            self.ui.metoOfficeDurdur.click()
        
        
        
        def veriTabaninaYukleButtonClicked(self):
            mongoDBFunc=mongoDB.mongoDBConnect()
            sonuc=mongoDBFunc.mongoDBYukle()
            if sonuc==True:
                self.ui.veriTabaniSonuc.setText("Yükleme Başarıyla Tamamlandı")
            else:
                self.ui.veriTabaniSonuc.setText("Yükleme Başarısız")
                
        
        ##########################################################################
        def havadurumuxLinkleriAlButtonClicked(self):
            global myworkerhavadurumux
            self.myworkerhavadurumux = havadurumuxScrubbingThread() 
            self.myworkerhavadurumux.progress.connect(self.reportProgreshavadurumux)
            #self.myworker.songiris.connect(self.songirisProgress)
            #self.myworker.kazanilanItemler.connect(self.kazanilanItemlerProgress)
            self.myworkerhavadurumux.start()
        
        
        def havadurumuxDurdurButtonClicked(self):
            try:
                global myworkerhavadurumux
                self.myworkerhavadurumux.terminate()         
                self.myworkerhavadurumux = None   
            except:
                pass
            
            try:
                global myworkerhavadurumuxBaslat
                self.myworkerhavadurumuxBaslat.terminate()         
                self.myworkerhavadurumuxBaslat = None   
            except:
                pass
            
            self.ui.HavadurumuxSonucu.setText("Durduruldu")
            
        def reportProgreshavadurumux(self,n):
            global hepsiniAyniAndaBaslat
            self.ui.HavadurumuxSonucu.setText(str(n))
            if hepsiniAyniAndaBaslat:
                self.ui.HavadurumuxBaslat.click()

        def havadurumuxBaslatButtonClicked(self):
            global myworkerhavadurumuxBaslat
            self.myworkerhavadurumuxBaslat = havadurumuxBaslatScrubbingThread() 
            self.myworkerhavadurumuxBaslat.progress.connect(self.reportProgreshavadurumuxBaslat)
            #self.myworker.songiris.connect(self.songirisProgress)
            #self.myworker.kazanilanItemler.connect(self.kazanilanItemlerProgress)
            self.myworkerhavadurumuxBaslat.start()
        
        def reportProgreshavadurumuxBaslat(self,n):
            self.ui.HavadurumuxSonucu.setText(str(n))
            
            if n=="Başarılı":
                self.ui.havadurumuxCheckBox.setChecked(True)
                with open("havaDurumuxHavaDurumuVerileri.json", "r", encoding="utf-8") as json_dosya:
                    havadurumuVerileri = json.load(json_dosya)
                print(havadurumuVerileri)
                
                
                if self.ui.havadurumuxCheckBox.isChecked() and self.ui.metoCheckBox.isChecked() and self.ui.weatherCheckBox.isChecked():
                    print("hepsi tamam")
                    self.ui.veriTabaninaYukle.setEnabled(True)
                    
        ##########################################################################  
        
        ##########################################################################
        def weatherLinkleriAlButtonClicked(self):
            global myworkerWeather
            self.myworkerWeather = weatherComScrubbingThread() 
            self.myworkerWeather.progress.connect(self.reportProgresWeather)
            #self.myworker.songiris.connect(self.songirisProgress)
            #self.myworker.kazanilanItemler.connect(self.kazanilanItemlerProgress)
            self.myworkerWeather.start()
        
        
        def weatherDurdurButtonClicked(self):
            try:
                global myworkerWeather
                self.myworkerWeather.terminate()         
                self.myworkerWeather = None   
            except:
                pass
            
            try:
                global myworkerWeatherBaslat
                self.myworkerWeatherBaslat.terminate()         
                self.myworkerWeatherBaslat = None   
            except:
                pass
            
            self.ui.weatherSonucu.setText("Durduruldu")
            
        def reportProgresWeather(self,n):
            global hepsiniAyniAndaBaslat
            self.ui.weatherSonucu.setText(str(n))
            if hepsiniAyniAndaBaslat:
                self.ui.weatherBaslat.click()

        

        def weatherBaslatButtonClicked(self):
            global myworkerWeatherBaslat
            self.myworkerWeatherBaslat = weatherComBaslatScrubbingThread() 
            self.myworkerWeatherBaslat.progress.connect(self.reportProgresWeatherBaslat)
            #self.myworker.songiris.connect(self.songirisProgress)
            #self.myworker.kazanilanItemler.connect(self.kazanilanItemlerProgress)
            self.myworkerWeatherBaslat.start()
        
        def reportProgresWeatherBaslat(self,n):
            self.ui.weatherSonucu.setText(str(n))
            
            if n=="Başarılı":
                self.ui.weatherCheckBox.setChecked(True)
                with open("weatherComHavaDurumuVerileri.json", "r", encoding="utf-8") as json_dosya:
                    havadurumuVerileri = json.load(json_dosya)
                print(havadurumuVerileri)
                
                if self.ui.havadurumuxCheckBox.isChecked() and self.ui.metoCheckBox.isChecked() and self.ui.weatherCheckBox.isChecked():
                    print("hepsi tamam")
                    self.ui.veriTabaninaYukle.setEnabled(True)
            
        ##########################################################################    
        
        
        
        
        ##########################################################################
        def metoOfficeScrubbingLinkleriAlButtonClicked(self):
            global myworker
            self.myworker = metoOfficeScrubbingThread() 
            self.myworker.progress.connect(self.reportProgressmeto)
            #self.myworker.songiris.connect(self.songirisProgress)
            #self.myworker.kazanilanItemler.connect(self.kazanilanItemlerProgress)
            self.myworker.start()
        
        
        def metoOfficeDurdurButtonClicked(self):
            try:
                global myworker
                self.myworker.terminate()         
                self.myworker = None   
            except:
                pass
            
            try:
                global myworkerBaslat
                self.myworkerBaslat.terminate()         
                self.myworkerBaslat = None   
            except:
                pass
            self.ui.metoOfficeSonucu.setText("Durduruldu")
            
        def reportProgressmeto(self,n):
            global hepsiniAyniAndaBaslat
            self.ui.metoOfficeSonucu.setText(str(n))
            if hepsiniAyniAndaBaslat:
                self.ui.metoOfficeLinkleriAl.click()
      

        def metoOfficeBaslatButtonClicked(self):
            global myworkerBaslat
            self.myworkerBaslat = metoOfficeBaslatScrubbingThread() 
            self.myworkerBaslat.progress.connect(self.reportProgressmetoBaslat)
            #self.myworker.songiris.connect(self.songirisProgress)
            #self.myworker.kazanilanItemler.connect(self.kazanilanItemlerProgress)
            self.myworkerBaslat.start()
        
        def reportProgressmetoBaslat(self,n):
            self.ui.metoOfficeSonucu.setText(str(n))
            
            if n=="Başarılı":
                self.ui.metoCheckBox.setChecked(True)
                with open("metofficeHavaDurumuVerileri.json", "r", encoding="utf-8") as json_dosya:
                    havadurumuVerileri = json.load(json_dosya)
                print(havadurumuVerileri)
                
                if self.ui.havadurumuxCheckBox.isChecked() and self.ui.metoCheckBox.isChecked() and self.ui.weatherCheckBox.isChecked():
                    print("hepsi tamam")
                    self.ui.veriTabaninaYukle.setEnabled(True)
            
        ##########################################################################    


class havadurumuxScrubbingThread(QThread):
    progress = pyqtSignal(str)
    #songiris = pyqtSignal(str)
    #kazanilanItemler = pyqtSignal(int,str,str,str)
 
    def __init__(self):
        super().__init__()

    def run(self):
        
        sonuc="Başlıyor"
        self.progress.emit(sonuc)
        
        chrome_options = Options()
        #chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(executable_path=r'chromedriver.exe',chrome_options=chrome_options)

        headers = {
            "User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        }
        driver.get("https://www.havadurumux.net")

        
        havadurumuxScrubbingFunc=havadurumuxScrubbing.havadurumuxScrubbing()
        sonuc="Devam Ediyor"
        self.progress.emit(sonuc)
        
        sonuc=havadurumuxScrubbingFunc.illeriCek(driver)
        
        if sonuc==True:
            sonuc="Başarılı"            
        else:
            sonuc="Başarısız"
            
        self.progress.emit(sonuc)
        driver.close()
        
        

class havadurumuxBaslatScrubbingThread(QThread):
    progress = pyqtSignal(str)
    #songiris = pyqtSignal(str)
    #kazanilanItemler = pyqtSignal(int,str,str,str)
    
    def __init__(self):
        super().__init__()

    def run(self):
        sonuc="Başlıyor"
        self.progress.emit(sonuc)
        
        chrome_options = Options()
        #chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(executable_path=r'chromedriver.exe',chrome_options=chrome_options)

        headers = {
            "User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        }
        driver.get("https://www.havadurumux.net")

        havadurumuxScrubbingFunc=havadurumuxScrubbing.havadurumuxScrubbing()
        sonuc="Devam Ediyor"
        self.progress.emit(sonuc)
        
        sonuc=havadurumuxScrubbingFunc.sicakliklariCek(driver)
        
        if sonuc!=False:
            sonuc="Başarılı"
        elif sonuc==False:
            sonuc="Başarısız"
            
        self.progress.emit(sonuc)
        driver.close()    












###############################################################################
class weatherComScrubbingThread(QThread):
    progress = pyqtSignal(str)
    #songiris = pyqtSignal(str)
    #kazanilanItemler = pyqtSignal(int,str,str,str)
    
    def __init__(self):
        super().__init__()

    def run(self):
        sonuc="Başlıyor"
        self.progress.emit(sonuc)
        
        chrome_options = Options()
        #chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(executable_path=r'chromedriver.exe',chrome_options=chrome_options)

        headers = {
            "User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        }
        driver.get("https://weather.com/tr-TR")
        
        fonksiyonlar=seleniumFonksiyonlari.seleniumFonksiyonlari()
        
        #cookie kabul et
        
        fonksiyonlar.tiklaId("truste-consent-button", 30, driver)
        
        weatherComScrubbing=weathercomScrubbing.weatherComScrubbing()
        sonuc="Devam Ediyor"
        self.progress.emit(sonuc)
        
        sonuc=weatherComScrubbing.illerinSessionCodeDegerleriniCek(driver)
        if sonuc==True:
            sonuc="Başarılı"            
        else:
            sonuc="Başarısız"
            
        self.progress.emit(sonuc)
        driver.close()
        
        

class weatherComBaslatScrubbingThread(QThread):
    progress = pyqtSignal(str)
    #songiris = pyqtSignal(str)
    #kazanilanItemler = pyqtSignal(int,str,str,str)
    
    def __init__(self):
        super().__init__()

    def run(self):
        sonuc="Başlıyor"
        self.progress.emit(sonuc)
        
        chrome_options = Options()
        #chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(executable_path=r'chromedriver.exe',chrome_options=chrome_options)

        headers = {
            "User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        }
        driver.get("https://weather.com/tr-TR")
        
        fonksiyonlar=seleniumFonksiyonlari.seleniumFonksiyonlari()
        
        #cookie kabul et
        
        fonksiyonlar.tiklaId("truste-consent-button", 30, driver)
        
        weatherComScrubbing=weathercomScrubbing.weatherComScrubbing()
        sonuc="Devam Ediyor"
        self.progress.emit(sonuc)
        
        sonuc=weatherComScrubbing.yediGunlukVeriCek(driver)
        
        if sonuc!=False:
            sonuc="Başarılı"
        elif sonuc==False:
            sonuc="Başarısız"
            
        self.progress.emit(sonuc)
        driver.close()    



###############################################################################

class metoOfficeScrubbingThread(QThread):
    progress = pyqtSignal(str)
    #songiris = pyqtSignal(str)
    #kazanilanItemler = pyqtSignal(int,str,str,str)
    
    def __init__(self):
        super().__init__()

    def run(self):
        sonuc="Başlıyor"
        self.progress.emit(sonuc)
        
        chrome_options = Options()
        #chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(executable_path=r'chromedriver.exe',chrome_options=chrome_options)

        headers = {
            "User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        }
        driver.get("https://www.metoffice.gov.uk/weather/world/turkey/list")
        
        fonksiyonlar=seleniumFonksiyonlari.seleniumFonksiyonlari()
        
        #cookie kabul et
        fonksiyonlar.tiklaId("ccc-recommended-settings", 30, driver)
        
        metoOfficeScrubbingFunc=metoOfficeScrubbing.metoOfficeScrubbing()
        sonuc="Devam Ediyor"
        self.progress.emit(sonuc)
        
        sonuc=metoOfficeScrubbingFunc.illerinSessionCodeDegerleriniCek(driver)
        if sonuc==True:
            sonuc="Başarılı"
            
            
        else:
            sonuc="Başarısız"
            
        self.progress.emit(sonuc)
        driver.close()
        
        


class metoOfficeBaslatScrubbingThread(QThread):
    progress = pyqtSignal(str)
    #songiris = pyqtSignal(str)
    #kazanilanItemler = pyqtSignal(int,str,str,str)
    
    def __init__(self):
        super().__init__()

    def run(self):
        sonuc="Başlıyor"
        self.progress.emit(sonuc)
        
        chrome_options = Options()
        #chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(executable_path=r'chromedriver.exe',chrome_options=chrome_options)

        headers = {
            "User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        }
        driver.get("https://www.metoffice.gov.uk/weather/world/turkey/list")
        
        fonksiyonlar=seleniumFonksiyonlari.seleniumFonksiyonlari()
        
        #cookie kabul et
        fonksiyonlar.tiklaId("ccc-recommended-settings", 30, driver)
        
        metoOfficeScrubbingFunc=metoOfficeScrubbing.metoOfficeScrubbing()
        sonuc="Devam Ediyor"
        self.progress.emit(sonuc)
        
        sonuc=metoOfficeScrubbingFunc.yediGunlukVeriCek(driver)
        
        if sonuc!=False:
            sonuc="Başarılı"
        elif sonuc==False:
            sonuc="Başarısız"
            
        self.progress.emit(sonuc)
        driver.close()    
        

###############################################################################



if __name__ == "__main__":
            app = QApplication(sys.argv)
    
            window = MainWindow()
            #window.setWindowTitle("batuhan okmen")
            window.show()
    
            sys.exit(app.exec_())
            
    
    
    
    
    
    















