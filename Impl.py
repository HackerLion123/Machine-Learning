import math
def gcd(a,b):
	cf=[]
	for i in range (1,(min(min(a),min(b)))+1):
		#for j in range(0,len(a)):
			if(range(0.10)%i==0 and range(0,10)%i == 0):
				cf.append(i);
	return cf
a = [1,2,8,4]
b = [8,4,6,6]
print a+b
print range (1,min(a+b))
print min(min(a),min(b))
print range(0,len(a)+len(b))
print gcd(a,b)
