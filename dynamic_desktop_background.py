import os
import random
from bs4 import BeautifulSoup
import shutil
import ctypes
import requests
import mechanicalsoup

"""
	A python program to scrap wallpapers from internet and change it daily

"""
URL = "https://www.pexels.com/"
LOC = "/root/mywallpaper"

def get_links(url):
	links = []
	browser = mechanicalsoup.StatefulBrowser()
	try:
		#web = requests.get(url,verify=False)
		#print(web.content)
		website = browser.open(url).text
		print(website)
		soup = BeautifulSoup(website,'html.parser')
		#print(soup)
		div = soup.find("div",{"class":"photos"})
		for atag in div.find_all('a'):
			links.append(atag.get('href'))
			print(atag.get('href'))
	except Exception as e:
		print("Get Links "+str(e))
	return links

def get_image(url):
	response = requests.get(url,stream=True,verify=False)
	print(response)
	with open(LOC+'.jpg','wb') as fp:
		shutil.copyfileobj(response.raw, fp)

def set_background(img_path):
	if os.uname().sysname == "Windows":
		SPI_SETDESKWALLPAPER = 20
		try:
			ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0 ,img_path, 0)
		except Exception as e:
			print("Error! can't set background " + e)

	if os.uname().sysname == "Linux":
		try:
			os.system("gsettings set org.gnome.desktop.background picture-uri "+img_path)
		except Exception as e:
			print("Error! can't set background " + e)

def main():
	links = get_links(URL)
	#print(len(links))
	index = random.randint(0,len(links))
	
	get_image("https://images.pexels.com/photos/1076805/pexels-photo-1076805.jpeg?cs=srgb&amp;dl=colorful-colourful-confetti-1076805.jpg&amp;fm=jpg")
	set_background(LOC+'.jpg')

if __name__ == '__main__':
	main()