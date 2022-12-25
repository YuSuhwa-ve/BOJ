import sys

N = int(sys.stdin.readline())

dp=[-1,1,3] #0번째는 쓰레기 값, 1,3은 초기값

for i in range(3,N+1):
	dp.append(dp[i-1]+2*dp[i-2])

print(dp[N])