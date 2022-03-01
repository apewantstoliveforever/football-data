from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import csv

#url = 'https://tiki.vn/search?q=phone'
s = Service(r"C:\Users\11131\OneDrive\Desktop\chromedriver_win32\chromedriver.exe")
browser = webdriver.Chrome(service= s)
browser.maximize_window()

field = ["name", "price"]
filename ="a.csv"
csvfile = open(filename, "w", encoding='utf-8')
csvwriter = csv.writer(csvfile)
csvwriter.writerow(field)


number = 0
def getiteminpage(page):
     # check if con san pham de scrape
        # check if con san pham de scrape trong page
    global number
    url = 'https://tiki.vn/search?q=phone&page=' + str(page)
    browser.get(url)
    time.sleep(1)
    content = browser.page_source
    print(page)
    if "Rất tiếc, không tìm thấy sản phẩm phù hợp với lựa chọn của bạn" in content:
        print("End")
        return
    else:
        items = browser.find_elements(by=By.CLASS_NAME, value="product-item")
        for item in items:
            #name = item.find_element(by = By.CLASS_NAME, value= '//*[@id="__next"]/div[1]/main/div[2]/div/div[2]/div[1]/div[2]/div[1]/a/span/div/div[2]/div[3]/div[1]')
            #value = item.find_elements_by_xpath('//*[@id="__next"]/div[1]/main/div[2]/div/div[2]/div[1]/div[2]/div[1]/a/span/div/div[3]/div[3]/div')

            name = item.find_element(by=By.CLASS_NAME, value='name')    #element khong co s
            value = item.find_element(by=By.CLASS_NAME, value='price-discount__price')  #element khong co s
            time.sleep(3)
            number += 1
            s = [str(name.text), str(value.text)]
            print(number, s)
            csvwriter.writerow(s)
            time.sleep(2)
        return getiteminpage(page+1)
getiteminpage(1)