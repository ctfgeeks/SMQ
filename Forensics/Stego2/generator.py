msg = "Hello there, Can you read what is required?"
flag = "z3r0_wid7h_ch4r4ct3rs_4r3_aw3s0m3"

binary = " ".join(format(ord(i), "b") for i in flag)

secret = [];
for c in binary:
	if(c == '1'):
		secret.append('\u200b');
	elif(c == '0'):
		secret.append('\u200d');
	else:
		secret.append('\u200c');


msg = msg + "".join(secret);

with open("chall.txt","w") as f:
	print(msg, file = f)


