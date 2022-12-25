import sys
sys.setrecursionlimit(10**6)

T=int(sys.stdin.readline())

def DFS(node,Check,Graph):
	if Check[node]: #방문한 노드 재방문시
		return
	else : 
		Check[node]=True #현재노드 방문표시
		DFS(Graph[node],Check,Graph)
	

for _ in range(T):
	N=int(sys.stdin.readline())
	INPUT=list(map(int,sys.stdin.readline().strip().split()))
	P=[0]+INPUT

	Check=[False]*(N+1)
	Check[0]=True
	cycle=0
	for i in range(1,N+1):
		if Check[i]:
			continue
		cycle+=1
		DFS(i,Check,P)
	print(cycle)