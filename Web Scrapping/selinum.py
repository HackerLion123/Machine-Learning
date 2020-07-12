from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

terms = ['flowers','ooty','water','fire']

driver.get("http://www.google.com/q="+terms[0])


"""for each in terms:
	print(each)
	ele = driver.find_element_by_id('lst-ib')
	ele.send_keys(each)
	ele.send_keys(Keys.RETURN)
"""
