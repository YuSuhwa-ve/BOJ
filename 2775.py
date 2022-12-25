import sys

T=int(sys.stdin.readline())

d=[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]]


for _ in range(T):
	K=int(sys.stdin.readline())
	N=int(sys.stdin.readline())
	
	if(N==0):
		print(0)
	elif(N==1):
		print(1) 
	elif K<=len(d)-1:
		print(d[K][N])
	else:
		for k in range(len(d),K+1):
			d.append([0,1])
			for n in range(2,15):
				d[k].append(d[k][n-1]+d[k-1][n])
		print(d[K][N])