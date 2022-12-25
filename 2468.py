import sys
from collections import deque

def BFS(m,cm,x,y,w):
	dx=[0,0,-1,1]#상하좌우
	dy=[-1,1,0,0]
	#첫번째 노드 큐에 넣기
	Queue=deque()
	Queue.append([x,y])
	cm[y][x]=1
	while Queue:
		#큐에서 다음에 방문할 노드를 꺼내 방문
		a,b =Queue.popleft()
		#cm[b][a]=1
		#현재 노드에 상하좌우로 인접하고 방문안했고 수면위(1이상)인 노드들 큐에 넣기
		for d in range(4):
			nextA=a+dx[d]
			nextB=b+dy[d]
			if 0<=nextA<N and 0<=nextB<N and m[nextB][nextA]>w and not cm[nextB][nextA]:
				Queue.append([nextA,nextB])
				cm[nextB][nextA]=1

N=int(sys.stdin.readline())
MAP=[]
for _ in range(N):
	m=list(map(int,sys.stdin.readline().split()))
	MAP.append(m)

'''
#현재 맵의 최소 높이와 최대높이
min_water=min(map(min,MAP))
max_water=max(map(max,MAP))
'''
min_water=101
max_water=0
for i in MAP:
	for j in i:
		if max_water<j:
			max_water=j
		if min_water>j:
			min_water=j
result=[]




for water in range(min_water,max_water+1):
	count=0
	CheckMAP=[[0]*N for _ in range(N)]
	for i in range(N):
		for j in range(N):
			if MAP[i][j]>water and not CheckMAP[i][j]:
				count+=1
				BFS(MAP,CheckMAP,j,i,water)
	result.append(count)

print(max(result))
