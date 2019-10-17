import string as str;
import random as rnd;

file1 = open("brocode1.txt","w");
file2 = open("brocode2.txt","w");

s = str.ascii_letters + str.digits;

arr1 = [];
arr2 = [];

cnt = 0;
line = 0;
while(True):
	c = rnd.choice(s);
	d = rnd.choice(s);
	if(c != d):
		arr1.append(c);
		arr2.append(d);
		cnt += 1;
		line += 1;
	if(line == 50):
		arr1.append("\n");
		arr2.append("\n");
		line = 0;
	if(cnt >= 500):
		break;

idx = [];
n = 31;
set = set();
while len(set) < n:
	x = rnd.randint(0,470);
	while (arr1[x] == '\n'):
		x = rnd.randint(0,470);
	set.add(x);

for i in set:
	idx.append(i);
idx.sort();

secret = "L00king past th3 diff3renc3s!!!";
for i in range(n):
	arr1[idx[i]] = secret[i];
	arr2[idx[i]] = secret[i];

file1.write("".join(arr1));
file2.write("".join(arr2));

file1.close();
file2.close();



