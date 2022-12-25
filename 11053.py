import sys

N=int(sys.stdin.readline())
dp=[1]*N

A=list(map(int,sys.stdin.readline().split()))

for i in range(N):
	for j in range(i):
		if A[j]<A[i]:
			dp[i]=max(dp[i],dp[j]+1)
print(dp)
print(max(dp))
