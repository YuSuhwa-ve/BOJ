import sys

T=int(sys.stdin.readline())
#print(T)
for _ in range(T):
	N=int(sys.stdin.readline())
	#print(N)
	sticker=[]
	for _ in range(2):
		sticker.append(list(map(int,sys.stdin.readline().strip().split())))
	#print(sticker)
	for i in range(1,N):
		sticker[0][i]=max(sticker[1][i-1]+sticker[0][i],sticker[0][i-1])
		sticker[1][i]=max(sticker[0][i-1]+sticker[1][i],sticker[1][i-1])
	print(max(sticker[0][N-1],sticker[1][N-1]))
