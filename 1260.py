import sys
from collections import deque
sys.setrecursionlimit(10**6)

N, M, Start = map(int, sys.stdin.readline().split())
result_B=[]
result_D=[]

Graph={}

for _ in range(M):
	V1, V2 = map(int, sys.stdin.readline().split())
	if V1 not in Graph:
		Graph[V1]=[]
	if V2 not in Graph:
		Graph[V2]=[]
	Graph[V1].append(V2)
	Graph[V2].append(V1)
for i in Graph.keys():
	if len(Graph[i])>1:
		Graph[i].sort()

def BFS(now_Node,Graph,result,queue):
	#현재 정점에 인접한 각 정점 방문(정점 번호가 작은거먼저방문)
	for i in Graph[now_Node]:
		if i not in result :
			queue.append(i)
			result.append(i)
	if queue: #큐에 정점이 남아있을 때만 탐색 계속
		BFS(queue.popleft(), Graph, result,queue) 
	

def DFS(now_Node,Graph,result):
	if now_Node not in result:
		result.append(now_Node)
		for i in Graph[now_Node]:
			DFS(i,Graph,result)


if Start in Graph:
	#시작정점 방문->큐에 넣음
	queue=deque([Start])
	result_B.append(Start)
	BFS(queue.popleft(),Graph,result_B,queue)
	DFS(Start,Graph,result_D)

	print(*result_D)
	print(*result_B)
else : 
	print(Start)
	print(Start)
