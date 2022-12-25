import sys

P = 1000-int(input())
result =0
d=[500,100,50,10,5,1]
for n in d:
	count=P//n
	P-=count*n
	result+=count
print(result)