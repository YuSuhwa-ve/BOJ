'''#top-down
import sys
sys.setrecursionlimit(10**6)

N=int(sys.stdin.readline())
memo=[0]*91 #input 조건중 n의 최대가 90
memo[0]=0 #F0=0
memo[1]=1 #F1=1

def Fibo(n):
	if n==0 :
		return memo[0]
	elif memo[n]!=0:
		return memo[n]
	else:
		memo[n]=Fibo(n-1)+Fibo(n-2)
		return memo[n]

print(Fibo(N))
'''

#bottom-up
import sys

N=int(sys.stdin.readline())

dp=[0]*91  #input 조건중 n의 최대가 90
dp[0]=0   #F0=0
dp[1]=1   #F1=1

for i in range(2,N+1):
	dp[i]=dp[i-1]+dp[i-2]

print(dp[N])

