from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

s = Service(r"C:\Users\11131\OneDrive\Desktop\chromedriver_win32\chromedriver.exe")
browser = webdriver.Chrome(service = s)
browser.maximize_window()
browser.get("https://www.linkedin.com/login")
content = browser.page_source
signupid = browser.find_element(by = By.ID, value = "username")
signuppass = browser.find_element(by= By.ID, value = "password")
signupid.send_keys('foreveralone16082003@gmail.com')
signuppass.send_keys('Ilove1993')
loginbutton = browser.find_element(by =By.XPATH, value= '//*[@id="organic-div"]/form/div[3]/button')
loginbutton.click()