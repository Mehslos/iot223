from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import tkinter as tk
import names
import secrets
import random
import string
import os
from selenium.webdriver.common.by import By


chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

chrome_options = Options()
options = [
    "--headless",
    "--disable-gpu",
    "--window-size=1920,1200",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage"
]
for option in options:
    chrome_options.add_argument(option)

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)


rand_name = names.get_first_name(gender='male')
S = random.randint(4,8)
N = random.randint(8,12)
rn = ''.join(random.choices(string.ascii_lowercase + string.digits, k = S))    
names=(rand_name+rn)
main2 = ''.join((secrets.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(random.randint(8,12))))

driver.get('https://ex.rex24.store/ref288819')
time.sleep(15)
driver.find_element(by=By.XPATH, value='//*[@id="ProfileBlock"]/div[1]/div/div[1]/div/div[3]/div').click()
time.sleep(10)
driver.find_element(by=By.XPATH, value='//*[@id="login"]').send_keys(names)
time.sleep(4)
driver.find_element(by=By.XPATH, value='//*[@id="password_1"]').send_keys(main2)
time.sleep(5)
driver.find_element(by=By.XPATH, value='//*[@id="password_2"]').send_keys(main2)
time.sleep(6)
driver.find_element(by=By.XPATH, value='//*[@id="FormRegister"]/div[8]/div').click()
time.sleep(6)
