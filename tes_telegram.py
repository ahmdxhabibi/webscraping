from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import telepot

def send_image(img):
    token = "6645683879:AAGpZ7C3IhyjS4iKhr4wOFODcBRul2N30EQ"
    chat_id = "687165125"
    bot = telepot.Bot(token)
    bot.sendPhoto(chat_id, photo=open(img, 'rb'))

input_user = "user"
input_password = "password"
link = "https://ecourt.mahkamahagung.go.id/Login/index/CAPTCHA"
captcha_ = "captcha1.png"

servis = Service('chromedriver.exe')
driver = webdriver.Chrome(service=servis)

driver.get(link)

captcha_img = driver.find_element(By.XPATH, '//*[@id="captchaimage"]')
captcha_img.screenshot(captcha_)
send_image(captcha_)

element = WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, '//*[@id="login_frm"]/div[1]/input')))
driver.find_element(By.XPATH, '//*[@id="login_frm"]/div[1]/input').send_keys(input_user)
driver.find_element(By.XPATH, '//*[@id="login_frm"]/div[2]/input').send_keys(input_password)
driver.find_element(By.XPATH, '//*[@id="login_frm"]/div[4]/input').click()


