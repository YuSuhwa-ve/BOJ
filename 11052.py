import sys
import math

N= int(sys.stdin.readline())

P = [-1]+ list(map(int,sys.stdin.readline().strip().split()))

dp=[-1, P[1]] #각 인덱스개수의 카드를 구매가능한 가장 비싼값 저장

for i in range(2,N+1):
	dpI=P[i]
	for j in range(1,math.floor(i/2)+1):
		comI=dp[j]+dp[i-j]
		if dpI<comI:
			dpI=comI
	dp.append(dpI)

print(dp[N])