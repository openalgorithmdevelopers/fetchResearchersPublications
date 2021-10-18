# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 11:11:50 2021

@author: bhupendra.singh
"""
import urllib.request
from bs4 import BeautifulSoup;
from nltk import *
from nltk import word_tokenize


#url = "https://scholar.google.com/citations?user=-KXu-KwAAAAJ&hl=en"
url = "https://www.scopus.com/authid/detail.uri?authorId=7405638726"
#url = "https://orcid.org/my-orcid?orcid=0000-0002-4490-1164"

with urllib.request.urlopen(url) as url:
    soup = BeautifulSoup(url)
    
    # kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out
text = soup.get_text()
print(text)