    # -*- coding: utf-8 -*-
"""
    Created on Tue Oct 31 00:28:37 2023
    
    @author: okmen
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options

    
class seleniumFonksiyonlari():
    
    def nelerVar(self):
        print("""
              elementlerin hepsinde degisken
              sure keys ve driver degerleri istenir
              istenilen kodların islemleri dogru olursa
              True aksi durumda False donusu olur
              Batuhan ökemen tarafından yapılmıştır. Flavves
              
              
              
              """)
    def deneme(self):
        print("Selenium foksyionları icin gelistirdigim sistem v4.2")
        
    def tiklaIdKeys(self,degisken,sure,keys,driver):
        try:
            WebDriverWait(driver, sure).until(
                EC.element_to_be_clickable((By.ID, degisken))
            )
        except:
            return False
            
        element=driver.find_element(By.ID,degisken)
        element.click()
        
        try:
             element.send_keys(keys)
        except:
             pass
         
        return True
    
    def tiklaId(self,degisken,sure,driver):
        try:
            WebDriverWait(driver, sure).until(
                EC.visibility_of_element_located((By.ID, degisken))
            )
        except:
            return False
            
        element=driver.find_element(By.ID,degisken)
        try:
            element.click()
        except:
            return False
        return True
    
    def idElementDondur(self,degisken,sure,driver):
        try:
            WebDriverWait(driver, sure).until(
                EC.visibility_of_element_located((By.ID, degisken))
            )
        except:
            return False
            
        element=driver.find_element(By.ID,degisken)
        
        return element
    
    def idElementlerDondur(self,degisken,sure,driver):
        try:
            WebDriverWait(driver, sure).until(
                EC.visibility_of_element_located((By.ID, degisken))
            )
        except:
            return False
            
        element=driver.find_elements(By.ID,degisken)
        
        return element
    
    def tiklaClassKeys(self,degisken,sure,keys,driver):
        try:
            WebDriverWait(driver, sure).until(
                EC.visibility_of_element_located((By.CLASS_NAME, degisken))
            )
        except:
            return False
            
        element=driver.find_element(By.CLASS_NAME,degisken)
        element.click()
        try:
            element.send_keys(keys)
        except:
            pass
        
        return True
    
    
    
    def tiklaClass(self,degisken,sure,driver):
        try:
            WebDriverWait(driver, sure).until(
                EC.visibility_of_element_located((By.CLASS_NAME, degisken))
            )
        except:
            return False
            
        element=driver.find_element(By.CLASS_NAME,degisken)
        try:
            element.click()
        except:
            return False
        
        return True
    
    
    
    def tiklaName(self,degisken,sure,driver):
        try:
            WebDriverWait(driver, sure).until(
                EC.visibility_of_element_located((By.NAME, degisken))
            )
        except:
            return False
            
        element=driver.find_element(By.NAME,degisken)
        try:
            element.click()
        except:
            return False
        
        return True
    
    
    def tiklaNameKeys(self,degisken,sure,keys,driver):
        try:
            WebDriverWait(driver, sure).until(
                EC.visibility_of_element_located((By.NAME, degisken))
            )
        except:
            return False
            
        element=driver.find_element(By.NAME,degisken)
        element.click()
        try:
            element.send_keys(keys)
        except:
            return False
        
        return True
    

    
    def tiklaLink(self,degisken,sure,driver):
        try:
            WebDriverWait(driver, sure).until(
                EC.visibility_of_element_located((By.LINK_TEXT, degisken))
            )
        except:
            return False
            
        element=driver.find_element(By.LINK_TEXT,degisken)
        try:
            element.click()
        except:
            return False
        
        return True
    
  
        
