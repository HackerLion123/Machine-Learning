n = input()

# _ is don't care symbol
d = dict(raw_input().split() for _ in  range(0,n))
for i in range(0,n):
    key = raw_input()
    if key in d:
        print(key+"="+d[key])
    else:
        print("Not found")
    
