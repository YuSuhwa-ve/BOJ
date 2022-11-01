import sys
from collections import deque

N, K =map(int, sys.stdin.readline().strip().split())
check=[-1]*100001

#bfs로 탐색
check[N]=0
queue=deque([N]) #방문처리후 큐에 넣기
while queue:
	now_node= queue.popleft() #탐색할 노드(이미방문됨) 큐에서 꺼내기
	if 0<=now_node*2<=100000:
		if check[now_node*2]==-1: # 인접노드 탐색가능한지
			check[now_node*2]=check[now_node]
			queue.append(now_node*2)
		else: #이미 탐색한 경우
			if check[now_node*2]>check[now_node]: # update
				check[now_node*2]=check[now_node]
	if 0<=now_node+1<=100000 :
		if check[now_node+1]==-1: # 인접노드 탐색가능한지
			check[now_node+1]=check[now_node]+1
			queue.append(now_node+1)
		else:
			if check[now_node+1]>check[now_node]+1:
				check[now_node+1]=check[now_node]+1
	if 0<=now_node-1<=100000:
		if check[now_node-1]==-1: # 인접노드 탐색가능한지
			check[now_node-1]=check[now_node]+1
			queue.append(now_node-1)
		else:
			if check[now_node-1]>check[now_node]+1:
				check[now_node-1]=check[now_node]+1


print(check[K])