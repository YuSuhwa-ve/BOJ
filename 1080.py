import sys

N, M = map(int,sys.stdin.readline().split())
A=[]
B=[]
result=0

def flip(a,I,J):
	for i in range(I,I+3):
		for j in range(J,J+3):
			if a[i][j]==0:
				a[i][j]=1
			else:
				a[i][j]=0


for _ in range(N):
	A.append(list(map(int,sys.stdin.readline().strip())))
for _ in range(N):
    B.append(list(map(int,sys.stdin.readline().strip())))
for n in range(N-2):
	for m in range(M-2):
		if A[n][m]!=B[n][m]:
			flip(A,n,m)
			result+=1
		if A==B:
			break
	if A==B:
		break

if A!=B:
	print(-1)
else:
	print(result)