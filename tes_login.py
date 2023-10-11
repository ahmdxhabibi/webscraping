from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.service import Service

input_user = "user"
input_password = "password"
servis = Service('chromedriver.exe')
driver = webdriver.Chrome(service=servis)
driver.get('https://shopee.co.id/buyer/login')
element = WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.NAME,"loginKey")))
driver.find_element(By.NAME,"loginKey").send_keys(input_user)
driver.find_element(By.NAME,"password").send_keys(input_password)
driver.find_element(By.XPATH, "//button[@class='wyhvVD _1EApiB hq6WM5 L-VL8Q cepDQ1 _7w24N1']").click()
