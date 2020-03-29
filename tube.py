import time
import threading
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/results?search_query=%EB%8B%A4%ED%81%90%EB%A9%98%ED%84%B0%EB%A6%AC&sp=EgIQAQ%253D%253D")

links = []

def calpagelength():
    user_data = driver.find_elements_by_xpath('//*[@id="video-title"]')
    for j in user_data:
        if j.get_attribute('href') not in links:
            links.append(j.get_attribute('href'))
    print(len(links))
    print(links)

count = 0

def starttimer():
    global count
    timer = threading.Timer(2.5, starttimer)
    timer.start()
    print(count)
    driver.find_element_by_tag_name('html').send_keys(Keys.END)
    count += 1
    if count > 50:
        timer.cancel()
        calpagelength()

starttimer()



