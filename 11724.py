import sys

N, M=map(int,sys.stdin.readline().split())
G=[[] for _ in range(N+1)]
Check=[False]*(N+1)
result=0

for _ in range(M):
	V1, V2=map(int,sys.stdin.readline().split())
	G[V1].append(V2)
	G[V2].append(V1)

print(G)
print(Check)

def DFS(Node, Graph, Check):
	if Check[Node]:
		return
	else:
		Check[Node]=True
		for i in range(len(Graph[Node])):
			DFS(Graph[Node][i],Graph,Check)

for i in range(1,N+1):
	if Check[i]:
		continue
	else :
		DFS(i,G,Check)
		result+=1

print(result)
	
	