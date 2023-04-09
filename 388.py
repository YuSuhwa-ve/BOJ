N,M=map(int,input().split())
board=[]

for _ in range(N):
	board.append(list(input()))
count=0

for i in range(N):
	pre="/"
	for j in range(M):
		if board[i][j]== '-':
			if board[i][j]!=pre :
				count+=1
		pre=board[i][j]

for j in range(M):
	pre="/"
	for i in range(N):
		if board[i][j]=='|':
			if board[i][j]!=pre:
				count+=1
		pre=board[i][j]

print(count)
