file1 = open("brocode1.txt","r").read();
file2 = open("brocode2.txt","r").read();


for x,y in zip(file1,file2):
	if (x == y and x != "\n"):
		print(x,end="");