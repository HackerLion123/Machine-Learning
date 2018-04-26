value = input()
value = int(value)
array = []
for j in range(0,value):
    non_con = 0
    size = input()
    size = int(size)
    array =  [int(x) for x in input().split()]
    for i in range(0,size):
        #a = input()
        #array += a
        if(array[i]>0):
            #print (array[i])
            non_con += array[i]
            #print (non_con)
    max_ending = max_ending_here = 0
    for i in range(0,size):
        max_ending = max_ending+array[i]
        if(max_ending > max_ending_here):
            max_ending_here = max_ending
        if(max_ending < max_ending_here):
            max_ending = 0
    print (str(non_con)+" " + str(max_ending_here)) 

