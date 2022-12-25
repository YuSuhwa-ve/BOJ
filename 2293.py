import sys

N, K = map(int,sys.stdin.readline().split())

V=[] #동전의 가치 저장
for i in range(N):
	V.append(int(sys.stdin.readline()))

dp=[0]*(K+1)
dp[0]=1

for i in range(N) : #동전하나씩 생각
	if V[i]<=K: # 찾고자하는 금액이 동전보다 커야함.
		for j in range(V[i],K+1): 
# 이 for문이 끝나면, v[i] 동전으로 만들수있는 경우의 수를 다 더한것임
			dp[j]=dp[j]+dp[j-V[i]];

print(dp[K])
	

