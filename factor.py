def factor(n):
	flist=[]
	for i in range(1,n+1):
		if(n%i == 0):
			"""flist = flist + [i] also can be used"""
			flist.append(i)
	return(flist)

if __name__ == '__main__': 
	n =input("Enter a value ")
	print factor(n)
