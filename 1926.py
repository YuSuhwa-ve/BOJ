import sys
from collections import deque

N,M=map(int, sys.stdin.readline().strip().split())
paper=[]
result=[]
result_index=-1

dn =[-1,1,0,0]#상하좌우
dm =[0,0,-1,1]

for _ in range(N):
	paper.append(list(map(int,sys.stdin.readline().strip().split())))

def BFS(node_n,node_m, Graph, result_index):
	queue=deque([(node_n,node_m)])
	Graph[node_n][node_m]=2
	result[result_index]+=1
	while queue:
		now_node_n, now_node_m = queue.popleft()
		for d in range(4):
			next_node_n=now_node_n+dn[d]
			next_node_m=now_node_m+dm[d]
			if 0<=next_node_n<N and 0<=next_node_m<M and Graph[next_node_n][next_node_m]==1:
				Graph[next_node_n][next_node_m]=2
				result[result_index]+=1
				queue.append((next_node_n,next_node_m))

for n in range(N):
	for m in range(M):
		if paper[n][m]==1:
			result.append(0)
			result_index+=1
			BFS(n,m,paper,result_index)

print(len(result))
if len(result)==0:
	print(0)
else:
	print(max(result))