import numpy as np


def Eculidean_distance(A,B):
	return np.sqrt(np.sum((A-B)**2))

def Manhathon_distance(A,B):
	return np.sum(np.abs(A-B))

def cosine_sim(A,B):
	pass

def pearson():
	pass

def Jaccard_sim():
	pass


A = np.array([[0,0],[5,0],[5,1],[0,1],[0,0.5]])
for e in Eculidean_distance(A[i,:],A):
	print(e)
