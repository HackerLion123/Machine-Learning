import mechanicalsoup
from bs4 import BeautifulSoup as bs

url = "https://www.google.com/"

browser = mechanicalsoup.StatefulBrowser()

try:
	browser.open(url)
except Exception as e:
	print("{} cannot open url".format(e))
else:
	#print(browser.get_current_page())
	browser.select_form()
	#print(browser.get_current_form().print_summary())

	browser["q"] = "Dogs"

	response = browser.submit_selected()

	print(response.text)