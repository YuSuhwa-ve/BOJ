import sys

N, K = map(int,sys.stdin.readline().split())
coins=[]
result=0
for _ in range(N):
	coin=int(sys.stdin.readline())
	coins.append(coin)

for i in range(N-1,-1,-1):
	if coins[i]>K:
		continue
	result+=K//coins[i]
	K=K%coins[i]

print(result)
	
