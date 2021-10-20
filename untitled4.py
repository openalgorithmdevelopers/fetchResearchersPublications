# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 13:12:45 2021

@author: bhupendra.singh
"""


import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time  #replace with selenium wait

from webdriver_manager.chrome import ChromeDriverManager



os.chdir('C:/Users/bhupendra.singh/Documents/GitHub/fetchResearchersPublications')
authorId = 41461482100
url = "https://www.scopus.com/authid/detail.uri?authorId=" + str(authorId)


options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(ChromeDriverManager().install() , options=options)
driver.get(url)

driver.refresh()
time.sleep(10)
print("title = " + driver.title)

count = 0
a = driver.find_element_by_xpath("//span[contains(@class,'button__text sc-els-paginator') and contains(text(), 'Next')]")
# Automating button click
#driver.find_elements(By.XPATH,  '//button[@class="button--link-black sc-els-paginator"]') #Authors lists
for i in range(5):
    #driver.find_elements(By.XPATH, "//span[contains(@class,'button__text sc-els-paginator') and contains(text(), 'Next')]")
    #driver.find_element_by_xpath("//span[contains(@class,'button__text sc-els-paginator') and contains(text(), 'Next')]").click();
    print(i)
    buttonStatus = a.
    print("button status " + str(buttonStatus))
    if(buttonStatus):
        count = count + 1
        print("Count = " + str(count))
        a.click()
        a = driver.find_element_by_xpath("//span[contains(@class,'button__text sc-els-paginator') and contains(text(), 'Next')]")
    if(buttonStatus == False): 
        driver.quit()
        break
    
    #a = driver.find_element_by_xpath("//span[contains(@class,'button__text sc-els-paginator') and contains(text(), 'Next')]")
    #print(a[0].text)
    #print("cliekd = " + str(a.is_enabled()))
    #a.click()
    time.sleep(3)
    
print("Count = " + str(count))



driver.quit()