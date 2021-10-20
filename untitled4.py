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
authorId = 57221459727
url = "https://www.scopus.com/authid/detail.uri?authorId=" + str(authorId)


options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(ChromeDriverManager().install() , options=options)
driver.get(url)

driver.refresh()
time.sleep(10)

articles = driver.find_elements(By.XPATH,  '//els-paginator[@totalamount]') #Authors lists
a = articles[0].text
b = a.split()
c = b.index('Next')
print("Count = " + b[c-1])



driver.quit()