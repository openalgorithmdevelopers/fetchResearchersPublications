# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 11:11:50 2021

@author: bhupendra.singh bhupendra.bisht59@gmail.com
"""
# Description: Provide your scopus id in line number 22 and the script will generate all your articles
# available in SCOPUS database as of today. The final_report.csv will be generated in the same folder as this script


import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time  #replace with selenium wait

from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd
from tqdm.notebook import tqdm

os.chdir('C:/Users/bhupendra.singh/Documents/GitHub/fetchResearchersPublications')
authorId = 57197900632
#authorId = 57210953023  #bhupendra singh
#authorId = 57221459727 #D K Awasthi
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


dataRows = []
singleRow = []

articles = driver.find_elements(By.XPATH,  '//els-paginator[@totalamount]') 
a = articles[0].text
b = a.split()
c = b.index('Next')
numberOfNext = b[c-1]
numberOfNext = int(numberOfNext)
if(numberOfNext > 80):
    numberOfNext = 80

#for currentPage in range(numberOfNext):       #provide here the number of next clicks avaiable
for currentPage in tqdm(range(numberOfNext)):       #provide here the number of next clicks avaiable
    currentPage = currentPage + 1
    #print("current page = " + str(currentPage))
    articleAndJournalNameWebElementList = driver.find_elements(By.XPATH, '//a[@title="Show document details"]') #Article and journal name
    articleTypeWebElementList = driver.find_elements(By.XPATH,  '//div[@data-component="document-type"]') #article or + open, conference paper
    
    articleInformationWebElementList = driver.find_elements(By.XPATH,  '//span[@class="text-meta"]') #year, vol, issue, page nos, article no/
    citationsCountWebElementList = driver.find_elements(By.XPATH,  '//div[@class="sc-els-info-field"]') #Citations count
    
    #players = driver.find_elements(By.XPATH,  '//div[@data-component="document-authors"]') #article or + open, conference paper
    authorsWebElementList = driver.find_elements(By.XPATH,  '//div[@class="author-list"]') #Authors lists
    for i in range(len(articleTypeWebElementList)):
        singleRow = []
        articleType = articleTypeWebElementList[i].text
        articleType.replace("Open Access", "")
        singleRow.append(articleType)
        singleRow.append(articleAndJournalNameWebElementList[2*i].text)
        singleRow.append(articleAndJournalNameWebElementList[2*i + 1].text)
        
        #singleRow.append(articleInformationWebElementList[i].text)
        articleInformation = articleInformationWebElementList[i].text
        
        #separatedInfo = articleInformation.split()        #splits the information into year, vol, issue, page_nos
        # extract year, volume, issue, pages number
        yearInfo = articleInformation[0:4]
        if( len(articleInformation) > 4):
            volumeIssuePageNosInfo = articleInformation[5:len(articleInformation)]
        else:
            volumeIssuePageNosInfo = ""
        
        singleRow.append(yearInfo)
        singleRow.append(volumeIssuePageNosInfo)
        singleRow.append(citationsCountWebElementList[i].text)
        singleRow.append(authorsWebElementList[i].text)
        dataRows.append(singleRow)
        del singleRow
    #singleRow.clear()
    if numberOfNext > 1 and  currentPage < numberOfNext:
        a = driver.find_element_by_xpath("//span[contains(@class,'button__text sc-els-paginator') and contains(text(), 'Next')]").click()
        #print("reached")
        time.sleep(5)
#     
# =============================================================================
df = pd.DataFrame(dataRows)
df.columns=["Article Type", "Title", "Journal/Conference/Book chapter Name", "Year", "Vol/Issue/pages", "citations" , "Authors"]
df.to_csv("final_report.csv")

driver.quit()