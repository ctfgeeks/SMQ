with open("chall.txt","r") as f:
	s = f.readlines();
	msg = "".join(s);
	answer = []
	for i in msg:
		if(i == '\u200b'):
			answer.append('1');
		elif(i == '\u200d'):
			answer.append('0');
		elif(i == '\u200c'):
			answer.append(' ');

	binary = ("".join(answer)).split(" ");
	flag = "".join( chr(int(i,2)) for i in binary)
	print(flag);