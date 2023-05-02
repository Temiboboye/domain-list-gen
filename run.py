#import requests
#from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
#Import Ex[ected conditionss as EC]
from selenium.webdriver.support import expected_conditions as EC
import time
from netaddr import *

browser = webdriver.Firefox()
browser.get('https://ipinfo.io/AS55293#block-ranges')

#WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.XPATH,
#    '/html/body/div/div/section[2]/div/div[2]/div[2]/div/div[2]/div[1]/div/a'))).click()

browser.execute_script("arguments[0].click()",browser.find_element(By.XPATH,
    '/html/body/div/div/section[2]/div/div[2]/div[2]/div/div[2]/div[1]/div/a'))

table_list = browser.find_element(By.TAG_NAME, 'table')
ranges = table_list.find_elements(By.XPATH, "//tr/td/a")
#print(table_list)
range_list = []

slash = '/'
for iprange in ranges :
    #print(iprange.text)
    if (slash in iprange.text):
        range_list.append(iprange.text)

print(range_list)
browser.close()

    
    

