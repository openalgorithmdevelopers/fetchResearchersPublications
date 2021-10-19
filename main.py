# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 11:11:50 2021

@author: bhupendra.singh
"""
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

import pandas as pd


os.chdir('C:/Users/bhupendra.singh/Documents/GitHub/fetchResearchersPublications')
authorId = 57202256028
url = "https://www.scopus.com/authid/detail.uri?authorId=" + str(authorId)


options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(ChromeDriverManager().install() , options=options)
driver.get(url)

driver.refresh()
time.sleep(15)
print("title = " + driver.title)

articleAndJournalNameWebElementList = driver.find_elements(By.XPATH, '//a[@title="Show document details"]') #Article and journal name
articleTypeWebElementList = driver.find_elements(By.XPATH,  '//div[@data-component="document-type"]') #article or + open, conference paper

articleInformationWebElementList = driver.find_elements(By.XPATH,  '//span[@class="text-meta"]') #year, vol, issue, page nos, article no/
citationsCountWebElementList = driver.find_elements(By.XPATH,  '//div[@class="sc-els-info-field"]') #Citations count

#players = driver.find_elements(By.XPATH,  '//div[@data-component="document-authors"]') #article or + open, conference paper
authorsWebElementList = driver.find_elements(By.XPATH,  '//div[@class="author-list"]') #Authors lists


print(len(articleTypeWebElementList))


dataRows = []
singleRow = []

for i in range(len(articleTypeWebElementList)):
    print(articleTypeWebElementList[i].text)
    singleRow = []
    singleRow.append(articleTypeWebElementList[i].text)
    singleRow.append(articleAndJournalNameWebElementList[2*i].text)
    singleRow.append(articleAndJournalNameWebElementList[2*i + 1].text)
    singleRow.append(articleInformationWebElementList[i].text)
    singleRow.append(citationsCountWebElementList[i].text)
    singleRow.append(authorsWebElementList[i].text)
    dataRows.append(singleRow)
    del singleRow
    #singleRow.clear()
#     
# =============================================================================
df = pd.DataFrame(dataRows)
df.to_csv("final_report.csv")

driver.quit()