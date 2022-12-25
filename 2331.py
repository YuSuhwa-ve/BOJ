import sys

A, N=map(int, sys.stdin.readline().split())
D=[A]
i=0
while True:
	d=0
	for p in str(D[i]):
		d+=int(p)**N
	if d in D:
		i=D.index(d)
		break
	D.append(d)	
	i+=1

print(i)
		