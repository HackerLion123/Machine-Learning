import sys

print("Hello",end=' ')
if len(sys.argv) >= 2:
	print(sys.argv[1])
else:
	print("world")
