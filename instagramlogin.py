import time
from csv import writer

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome()

driver.get("https://instagram.com")
time.sleep(5)
username = driver.find_element(By.NAME,"username")
password = driver.find_element(By.NAME,"password")

username.send_keys("amezireli")
password.send_keys("Alp117077124*")
time.sleep(5)
click_button = driver.find_element("xpath", '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button')
click_button.click()



