from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pandas
import time

opsi = webdriver.ChromeOptions()
opsi.add_argument('--headless')
servis = Service('chromedriver.exe')
driver = webdriver.Chrome(service=servis, options=opsi)
link = "https://shopee.co.id/Kaos-Polos-col.3971528"
driver.set_window_size(1300,800)
driver.get(link)

##selenium auto scroll
scroll_ms = 500
for i in range(1,10):
    last = scroll_ms * i
    to_do = "window.scrollTo(0,"+str(last)+")"
    driver.execute_script(to_do)
    print("Loading " + str(i))
    time.sleep(1)

time.sleep(5)

driver.save_screenshot("home.png")
content = driver.page_source

driver.quit() 

data = BeautifulSoup(content, "html.parser") ## Parsing data / Memisahkan data
i = 1
base_link = "https://shopee.co.id/" 
## Inisialisasi sebagai list sebelum dimasukkan ke data excel
# list_nama, list_gambar, list_harga, list_link, list_terjual, list_lokasi = [], [], [], [], [], []
list_nama, list_harga, list_link, list_terjual, list_lokasi = [], [], [], [], []

for area in data.find_all("div", class_="col-xs-2-4 shopee-search-item-result__item"):
    print(i)
    i+=1
    ## Sesuaikan dengan tag HTML pada web yang di scraping
    nama = area.find("div", class_="Af+5o- JKW-T3 U28b4N").get_text()
    # gambar = str(area.find("img")["src"])
    harga = area.find("span", class_="wbhegq").get_text()
    link = base_link + area.find("a")["href"]
    terjual = area.find("div", class_="_24y9A4 -TRbsk")
    if terjual != None:
        terjual = terjual.get_text()
    lokasi = area.find("div", class_="rkY3va").get_text()
    ## Pengecekkan apakah data sudah masuk
    print(nama)
    # print(gambar)
    print(harga)
    print(terjual)
    print(lokasi)
    print(link)
    print("--------------------------------")
    print("")
    ## Memasukkan data
    list_nama.append(nama)
    # list_gambar.append(gambar)
    list_harga.append(harga)
    list_terjual.append(terjual)
    list_lokasi.append(lokasi)
    list_link.append(link)

## Input data ke excel
# df = pandas.DataFrame({'Nama':list_nama, 'Gambar':list_gambar, 'Harga':list_harga, 'Terjual':list_terjual, 'Lokasi':list_lokasi, 'Link':list_link})
df = pandas.DataFrame({'Nama':list_nama, 'Harga':list_harga, 'Terjual':list_terjual, 'Lokasi':list_lokasi, 'Link':list_link})
writer = pandas.ExcelWriter('kaos.xlsx')
df.to_excel(writer, 'Sheet1', index=False)
writer.save()

import mysql.connector
from sqlalchemy import create_engine

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="tes_scraping"
)

cursor = conn.cursor()

buat_table = """
CREATE TABLE IF NOT EXISTS data_tes (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Nama TEXT NOT NULL,
    Harga INT NOT NULL,
    Terjual INT NULL,
    Lokasi TEXT NOT NULL,
    Link TEXT NOT NULL
);
"""
cursor.execute(buat_table)

for index, row in df.iterrows():
    insert_query = "INSERT INTO data_tes (Nama, Harga, Terjual, Lokasi, Link) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(insert_query, (row.Nama, row.Harga, row.Terjual, row.Lokasi, row.Link))

# Commit perubahan pada tabel dan tutup kursor
conn.commit()
cursor.close()

# tabel_mysql = "data_tes"

# engine = create_engine('mysql+pymysql://root:@localhost/tes_scraping', echo=False)
# tabel_mysql = "data_tes"
# df.to_sql(name=tabel_mysql, con=engine, if_exists='replace', index=False)

# # Commit perubahan dan tutup koneksi
# conn.commit()
conn.close()
