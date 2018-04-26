#Dictonary for a list of movies and it's critics

critics = {'Me':{'Dark Knight':4.5,'Mean Girls':4.0,'Grown Up':5.0,'Justice League':4.8,'Adult world':3.5,'Midnight in Paris':4.5},'Bruce':{'Dark Knight':5,'Mean Girls':3.5,'Grown Up':4.0,'Justice League':4.0,'Adult world':3.6,'Midnight in Paris':3.0},'Wolverine':{'X-men':4.5,'Mean Girls':3.5,'Grown Up':5.0,'Jaws':4.6,'Terminator 2':4.5,'Midnight in Paris':4.5},'Charles':{'X-men':4.5,'Twilight':4.5,'Rick and Morty':5,'Powerpuff Girls':4},'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},'Peter':{'Spider man':4.9,'Mean Girls':4.0,'Midnight in Paris':4.2,'Pirates of caribean':4.6,'Wonder woman':4.6},'Adam':{'Spider man':4.2,'Mean Girls':3.1,'Midnight in Paris':4.0,'Pirates of caribean':5,'Wonder woman':4.4,'connan:the barbarian':4.0},'Jack':{'Titanic':4.8,'Adult world':3.0,'Snakes on a Plane':4.3,'Grown Up':5.0},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}

from math import sqrt;

def Euclian_distance(prefs,person1,person2):
	#list of shared item
	si = {}

	for movie in prefs[person1]:
		if movie in prefs[person2]:
			si[movie] = 1

	#if no rating in common 
	if(len(si) == 0): return 0
	
	sq = sum([pow(prefs[person1][movie] - prefs[person2][movie],2)
	for movie in prefs[person1] 
		if movie in prefs[person2]])          #a list is created using for loop
	return 1/(1+sq)

#pearson corelation coefficent
def sim_pearson(prefs,p1,p2):
	#list of shared item
	si = {}

	for movie in prefs[p1]:
		if movie in prefs[p2]:
			si[movie] = 1

	n = len(si)

	#if no rating in common 
	if(n == 0): return 0
	
	# sum up all preferences
	sum1 = sum([prefs[p1][item] for item in si])    
	sum2 = sum([prefs[p2][item] for item in si])

	# sum up squares
	sum1Sq = sum([pow(prefs[p1][item],2) for item in si])
	sum2Sq = sum([pow(prefs[p2][item],2) for item in si])

	#sum up products
	psum = sum([prefs[p1][item]*prefs[p2][item] for item in si])

	#calculate person correlation coffeicent
	num = psum - ((sum1*sum2)/n)
	den = sqrt((sum1Sq - pow(sum1,2)/n)*(sum2Sq - pow(sum2,2)/n))

	if den == 0: return 0
	
	return num/den

#critics that matches my taste
def topMatches(prefs,person,n = 3,similarity = sim_pearson):
	scores = [(similarity(prefs,person,other),other) for other in prefs if other != person]

	#sort the list in descending order
	scores.sort()
	scores.reverse()
	return scores[0:n]

#get Recommendations
def getRecommendations(prefs,person):
	totals = {}
	simSums = {}
	for other in prefs:
		#don't compare myself with me again
		if other == person: continue
		sim = sim_pearson(prefs,person,other)

		#ignore critics who are zero or lower
		if sim <= 0: continue
		for item in prefs[other]:
			
			if item not in prefs[person]:
				#Similarity * Score
				totals.setdefault(item,0)
				totals[item] += prefs[other][item]*sim;

				#sum of sims
				simSums.setdefault(item,0)
				simSums[item] += sim

		rankings = [(total/simSums[item],item) for item,total in totals.items()]
		
		rankings.sort()
		rankings.reverse()

	return rankings[0:3]

#Function to flip the dictionary 
#This is used to get people also see tab
def transformPrefs(prefs):
	result = {}
	for person in prefs:
		for item in prefs[person]:
			result.setdefault(item,{})
			
			result[item][person] = prefs[person][item]
	return result

#movies = transformPrefs(critics)

def calculateSimilarItems(prefs,n = 10):
	# Create a dictionary of items showing which other items they
	# are most related to.
	result = {}

	#reverse the dataset
	itemsPrefs = transformPrefs(critics)
	c = 0
	for item in itemsPrefs:
		#status update for large dataset this is cool
		c += 1
		if c%100 == 0: print "%d/%d"%(c,len(itemsPrefs))
		
		#Find most similar items
		scores = topMatches(itemsPrefs,item,3,Euclian_distance)
		#print scores
		result[item] = scores
	return result

print calculateSimilarItems(critics)

