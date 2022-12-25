import sys
sys.setrecursionlimit(10**6)

N=int(sys.stdin.readline())
M=int(sys.stdin.readline())
Graph=[[] for _ in range(N+1)]
CheckGraph=[False]*(N+1)
count=0

for _ in range(M):
	V1, V2= map(int,sys.stdin.readline().split())
	Graph[V1].append(V2)
	Graph[V2].append(V1)


def DFS(Graph,Check,count,v):
	#현재 노드 v를 방문
	Check[v]=True
	count+=1

	print(Check)
	print(count)

	#현재 노드 v에 연결된 방문 안한 노드들 방문
	for i in Graph[v]:
		if not Check[i]:
			count=DFS(Graph,Check,count,i)	
	return count
	
print(DFS(Graph,CheckGraph,count,1))
