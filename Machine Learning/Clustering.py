from math import sqrt

def readfile(filename):
	lines = [line for line in file(filename)]

	# First line is the column titles
	colnames = lines[0].strip().split('\t')[1:]
	rownames = []
	data = []
	for line in lines[1:]:
		p = line.strip().split('\t')
		
		# First column in each row is the rowname
		rownames.append(p[0])
		# other data
		data.append([float(x) for x in p[1:]])
	return rownames,colnames,data

#it takes a list of numbers and return pearson value
def pearson(n1,n2):
	sum1 = sum(n1)
	sum2 = sum(n2)

	sumSq1 = sum([pow(v,2) for v in n1])
	sumSq2 = sum([pow(v,2) for v in n2])

	#sum of products	
	pSum = 	sum([n1[i]*n2[i] for i in range(len(n1))])

	#calculate pearson score
	num = pSum - sum1*sum2/len(n1)
	den = sqrt(sumSq1 - pow(sum1,2)/len(n1) * sumSq2 - pow(sum2,2)/len(n2))
	if den == 0: return 0
	
	#it is to create smaller distance between close items
	return 1.0 - num/den

class bicluster:
	def __init__(self,vec,left=None,right=None,distance = 0.0,id=None ):
		self.vec = vec
		self.left = left
		self.right = right
		self.id = id
		self.distance = distance

def hcluster(rows):
	distances = {}
	currentclusterid = -1

	#Clusters are intially just the rows
	clust = [bicluster(rows[i],id=i) for i in range(len(rows))]

	while len(clust)>1:
		lowestpair = (0,1)
		closest = pearson(clust[0].vec,clust[1].vec)

		




