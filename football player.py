from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from player import Player
from selenium.common.exceptions import NoSuchElementException

club = 'Real Madrid'
s = Service(r"C:\Users\11131\OneDrive\Desktop\chromedriver_win32\chromedriver.exe")
browser = webdriver.Chrome(service = s)
browser.maximize_window()
browser.get('https://www.google.com/')
search = browser.find_element(by= By.NAME, value= 'q')
search.send_keys(club)
searchbutton = browser.find_element(by= By.NAME, value= 'btnK')
time.sleep(1)
searchbutton.click()
tabplayer = browser.find_element(by= By.XPATH, value= '//*[@id="sports-app"]/div/div[2]/div/div/div/ol/li[4]')
tabplayer.click()
time.sleep(1)
players = browser.find_elements(by = By.CSS_SELECTOR, value= "div[jsname='jXK9ad']")
print(len(players))
allplayer = {}

for player in players:
    playername = player.find_element(by = By.CLASS_NAME, value= 'JjtOHd')
    playerposition = player.find_element(by = By.CSS_SELECTOR, value= "div[class= 'ellip yF4Rkc AqEFvb']")
    allplayer[str(playername.text)] = [str(playerposition.text)]

# name, position, birthday, place, height
for name, j in allplayer.items():
    browser.get('https://www.google.com/search?q=' + name +" "+club)
    try:
        birth = browser.find_element(by = By.CSS_SELECTOR, value= 'div[data-attrid="kc:/people/person:born"]')
        birth1 = birth.find_element(by = By.CSS_SELECTOR, value= "span[class= 'LrzXr kno-fv wHYlTd z8gr9e']")
        birthday = str(birth1.text)
        #split birthday and place
        if birthday.find(')') == (len(birthday)-1):
            b1 = birthday
            b2 = ''
        else:
            b2 = birthday[(birthday.find(')')+3):]
            b1 = birthday[:birthday.find(')') + 1]
        temp = b1.find('(')
        b1 = b1[:(temp -1)]
        allplayer[name].append(b1)
        allplayer[name].append(b2)
    except NoSuchElementException:
        pass

    try:
        height = browser.find_element(by = By.XPATH, value= '//*[@id="kp-wp-tab-overview"]/div[1]/div/div/div/div/div/div[3]/div/div/div/span[2]')
        h = str(height.text)
        allplayer[name].append(h)
    except NoSuchElementException:
        allplayer[name].append('')
        pass
    #height = browser.find_element(by = By.CSS_SELECTOR, value= 'div[data-attrid="ss:/webfacts:height"]')
    #height1 = height.find_element(by = B nny.CSS_SELECTOR, value= "span[class= 'LrzXr kno-fv wHYlTd z8gr9e']")
    #mylist = [j]
    #mylist.append(str(birth1.text))
    #mylist.append(str(height1.text))


for name, j in allplayer.items():
    print(name, j)


