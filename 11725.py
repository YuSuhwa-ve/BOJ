import sys
sys.setrecursionlimit(10**6)

N=int(sys.stdin.readline())

Tree=[[] for _ in range(N+1)]
for _ in range(N-1):
	V1, V2 = map(int, sys.stdin.readline().split())
	Tree[V1].append(V2)
	Tree[V2].append(V1)
Parents=[-1]*(N+1)
CheckTree=[False]*(N+1)

def DFS(Graph, Check, Node, Parents) :
	if not Check[Node] :
		Check[Node]=True
		for i in Graph[Node]:
			if not Check[i]:
				Parents[i]=Node
				DFS(Graph,Check,i,Parents)

DFS(Tree,CheckTree,1,Parents)
for i in range(2,N+1):
	print(Parents[i])
