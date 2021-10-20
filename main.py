# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 11:11:50 2021

@author: bhupendra.singh
"""

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time  #replace with selenium wait

from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd


os.chdir('C:/Users/bhupendra.singh/Documents/GitHub/fetchResearchersPublications')
authorId = 57221459727
#authorId = 57210953023  #bhupendra singh
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

for numberOfNext in range(2):       #provide here the number of next clicks avaiable
    print("i = " + str(numberOfNext))
    articleAndJournalNameWebElementList = driver.find_elements(By.XPATH, '//a[@title="Show document details"]') #Article and journal name
    articleTypeWebElementList = driver.find_elements(By.XPATH,  '//div[@data-component="document-type"]') #article or + open, conference paper
    
    articleInformationWebElementList = driver.find_elements(By.XPATH,  '//span[@class="text-meta"]') #year, vol, issue, page nos, article no/
    citationsCountWebElementList = driver.find_elements(By.XPATH,  '//div[@class="sc-els-info-field"]') #Citations count
    
    #players = driver.find_elements(By.XPATH,  '//div[@data-component="document-authors"]') #article or + open, conference paper
    authorsWebElementList = driver.find_elements(By.XPATH,  '//div[@class="author-list"]') #Authors lists
    for i in range(len(articleTypeWebElementList)):
        print(articleTypeWebElementList[i].text)
        singleRow = []
        singleRow.append(articleTypeWebElementList[i].text)
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
    a = driver.find_element_by_xpath("//span[contains(@class,'button__text sc-els-paginator') and contains(text(), 'Next')]").click()
    time.sleep(5)
#     
# =============================================================================
df = pd.DataFrame(dataRows)
df.columns=["Article/Conference/Book Chapter", "Title", "Journal/Conference/Book chapter Name", "Year", "Vol/Issue/pages", "citations" , "Authors"]
df.to_csv("final_report.csv")
print(articleInformation)

driver.quit()