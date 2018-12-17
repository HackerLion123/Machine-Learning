import requests
from bs4 import BeautifulSoup

BASE_URL = "https://pokemondb.net/pokedex/"

def get_names(content):
	website = BeautifulSoup(content,'html.parser')
	spans = website.find_all('span',{'class':'infocard-lg-img'})
	pokemons = []
	for span in spans:
		pokemon = span.find('a').get('href')
		pokemon = pokemon.split('/')[2]
		pokemons.append(pokemon)
	return pokemons

def save_names(file_name,names,details):
	with open(file_name,'w') as fp:
		for i in range(len(names)):
			print(names[i])
			print(details[i])

def get_details(names):
	details = []
	for name in names:
		content = requests.get(BASE_URL+name,verify=True).content
		web = BeautifulSoup(content,'html.parser')
		type = web.find('table',{'class':'vitals-table'}).find('tbody')
		#print(type)
		type = type.find_all('tr')[1].find('td').find('a').get('href')
		#print(type)
		type = type.split('/')[2]
		des = web.find('td',{'class':'cell-med-text'})
		# print(type)
		# print(des.text)
		details.append(type+":"+des.text)
	return details

def main():
	# All gens are loaded every time so one is enough
	pokemon_gens =  ["national#gen-1"]
	for gen in pokemon_gens:
		web = requests.get(BASE_URL+gen,verify=True).content
		#print(web)
		names = get_names(web)
		print(len(names))
		details = get_details(names)
		#save_names("",names,details)

if __name__ == '__main__':
	main()