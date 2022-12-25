import sys
sys.setrecursionlimit(10**6)

T=int(sys.stdin.readline())

dx=[0,0,-1,1] #상하좌우
dy=[-1,1,0,0]


def DFS(Graph,x,y,M,N):
	#현재 노드 방문 : 그래프의 값을 -1로 변경
	Graph[y][x]=-1
	#현재 노드 주변(상하좌우)의 노드중 1이고 방문 안핞노드 탐색
	for d in range(4):
		if 0<=x+dx[d]<M and 0<=y+dy[d]<N and Graph[y+dy[d]][x+dx[d]]==1:
			DFS(Graph,x+dx[d],y+dy[d],M,N)


for _ in range(T):
	M,N,K=map(int, sys.stdin.readline().split())
	#일단 모두 0인 맵
	MAP=[[0]*M for _ in range(N)]
	for _ in range(K):
		X, Y=map(int,sys.stdin.readline().split())
		MAP[Y][X]=1
	
	count=0
	for i in range(N):
		for j in range(M):
			if MAP[i][j]==1:
				count+=1
				DFS(MAP,j,i,M,N)
	print(count)
