fh = open("pass.txt","w")

print "file mode : " + fh.mode

fh.write("Hello World")

fh.close()

fh = open("pass.txt","r")

for line in fh:
	print line

fh.close()

fh = open("pass.txt","a")

fh.write("\nNew Line?\n")

fh.close()


