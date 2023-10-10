from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pandas
import time

opsi = webdriver.ChromeOptions()
opsi.add_argument('--headless')
servis = Service('chromedriver.exe')
driver = webdriver.Chrome(service=servis, options=opsi)
# link = "https://shopee.co.id/search?keyword=headset"
link = "https://shopee.co.id/Kaos-Polos-col.3971528"
driver.set_window_size(1300,800)
driver.get(link)

##selenium auto scroll
scroll_ms = 500
for i in range(1,7):
    last = scroll_ms * i
    to_do = "window.scrollTo(0, " + str(last)+")"
    driver.execute_async_script(to_do)
    print("Loading " + str(i))
    time.sleep(1)

time.sleep(5)

driver.save_screenshot("home.png")
content = driver.page_source

driver.quit()

data = BeautifulSoup(content, "html.parser")
i = 1
# print(data.encode("utf-8"))
base_link = "https://shopee.co.id/" 
for area in data.find_all("div", class_="col-xs-2-4 shopee-search-item-result__item"):
    print(i)
    i+=1
    nama = area.find("div", class_="Af+5o- JKW-T3 U28b4N").get_text()
    gambar = area.find("img")["src"]
    harga = area.find("span", class_="wbhegq").get_text()
    link = base_link + area.find("a")["href"]
    terjual = area.find("div", class_="_24y9A4 -TRbsk")
    if terjual != None:
        terjual = terjual.get_text()
    lokasi = area.find("div", class_="rkY3va").get_text()
    print(nama)
    print(gambar)
    print(harga)
    print(terjual)
    print(lokasi)
    print(link)
    print("--------------------------------")
    print("")