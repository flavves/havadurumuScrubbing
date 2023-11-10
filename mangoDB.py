# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 15:09:11 2023

@author: okmen
"""

from pymongo import MongoClient


# MongoDB'ye bağlan
client = MongoClient('mongodb://localhost:27017/')

# Veritabanı seç
db = client['batuhan_okmen']

# Bir koleksiyon oluştur
collection = db['havaDurumu']

# Veri ekle
data = {'name': 'John', 'age': 30, 'city': 'New York'}
collection.insert_one(data)

# Veri sorgula
result = collection.find_one({'name': 'John'})
print(result)



from datetime import datetime, timezone, timedelta

# Şu anki tarihi ve saat dilimini al
belirli_tarih = datetime(2023, 11, 7, 0, 0, 0, tzinfo=timezone.utc)

# Tarihi belirli bir formatta ekrana yazdır
formatli_tarih = belirli_tarih.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "+00:00"
print("Şu anki tarih:", formatli_tarih)
