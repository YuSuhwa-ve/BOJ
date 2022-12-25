import sys
sys.setrecursionlimit(10**6)

N,M=map(int, sys.stdin.readline().split())
board=0
CheckMAP=[[False]*M for _ in range(N)]
MAP=[]
dxy=[1,-1]
for _ in range(N):
	m=list(sys.stdin.readline().strip())
	MAP.append(m)

def DFS(MAP,Check,x,y):
	Check[x][y]=True
	if MAP[x][y]=='-':
		for d in dxy:
			if 0<=y+d<M and not Check[x][y+d] and MAP[x][y+d]=='-':
				DFS(MAP,Check,x,y+d)
	elif MAP[x][y]=='|':
		for d in dxy:
			if 0<=x+d<N and not Check[x+d][y] and MAP[x+d][y]=='|':
				DFS(MAP,Check,x+d,y)




for i in range(N):
	for j in range(M):
		if not CheckMAP[i][j]:
			board+=1
			DFS(MAP,CheckMAP,i,j)

print(board)
