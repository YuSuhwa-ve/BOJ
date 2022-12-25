import sys

N=int(sys.stdin.readline())
coins=[]
for _ in range(N):
	coins.append(list(sys.stdin.readline().strip()))
result=[0]*(1<<N)

#해당 열을 뒤집는 함수
def flip(Coin,C):
	for i in range(N):
		if Coin[i][C]=='H':
			Coin[i][C]='T'
		else:
			Coin[i][C]='H'

#2**n 경우의 수 만큼 for문 
for bit in range(1<<N):
	new_coins=[coins[i][:] for i in range(N)]
	#해당 경우의 수에 해당되도록 열 뒤집기
	for i in range(N):
		if bit & (1<<i):
			flip(new_coins,i)
	#해당 경우의 수에서 각 행을 검사하여 이득인 경우 행 뒤집기
	for i in range(N):
		ct=new_coins[i].count('T')
		if ct>2//N:
			result[bit]+=(N-ct)
		else :
			result[bit]+=ct

print(min(result))
	