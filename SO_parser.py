'''
This code opens Stackoverflow in a browser (either in Firefox or Chrome)

Features:
- Search entries in Stackoverflow for specific keywords

'''

from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Stack Overflow results for questions tagged with [python]
# We can later ad more keywords to the searchbar and make more precise searches
SO_pythonPage = 'https://stackoverflow.com/questions/tagged/python?tab=votes&page={}&pagesize=15%27.format(page))'

driver = webdriver.Firefox(executable_path="drivers\geckodriver.exe")       # This driver is needed to run the URL in firefox
#driver = webdriver.Chrome(executable_path="drivers\chromedriver.exe")      # This driver is needed to run the URL in Chrome

driver.get(SO_pythonPage)                                       # Open the given URL
#driver.refresh()                                               # Refresh the page


searchText = 'test'
driver.find_element_by_name("q").clear()                            # Clear the searchbar text (q is the element name of the searchbar in browser)
driver.find_element_by_name("q").send_keys(searchText + Keys.ENTER)     # Append new keyword(s) to search bar


