#top-down
import sys
sys.setrecursionlimit(10**6)

N=int(sys.stdin.readline())
memo={1:0,2:1,3:1}

def Make1(n):
	if n==1:
		return memo[1]
	elif n in memo:
		return memo[n]
	else:
		memo[n]=1+Make1(n-1)
		if n%3==0:
			memo[n]=min(memo[n],1+Make1(n//3))
		if n%2==0:
			memo[n]=min(memo[n],1+Make1(n//2))
		
		return memo[n]

print(Make1(N))
