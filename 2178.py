import sys
from collections import deque
sys.setrecursionlimit(10**6)

N,M=map(int, sys.stdin.readline().split())
MAP=[]
for _ in range(N):
	m=list(map(int, (sys.stdin.readline()).strip("\n")))
	MAP.append(m)
CheckMAP=[[0]*M for _ in range(N)]

dr=[1,0,-1,0]
dc=[0,1,0,-1] #하->우->상->좌

def BFS(now_Node, Check):
	if now_Node[0]==N-1 and now_Node[1]==M-1 :
		print(Check[N-1][M-1])
		return
	for i in range(4) : #하->우->상->좌
		r=now_Node[0]+dr[i]
		c=now_Node[1]+dc[i]
		if 0<=r<N and 0<=c<M and MAP[r][c]==1:
			if not Check[r][c] :
					Check[r][c]=Check[now_Node[0]][now_Node[1]]+1
					queue.append([r,c])
				
	#탐색!
	if queue :
		next_Node=queue.popleft()
		BFS(next_Node,Check)


queue=deque([[0,0]]) # [행좌표, 열좌표], 루트

CheckMAP[0][0]=1
BFS(queue.popleft(),CheckMAP)
