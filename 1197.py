import sys

V, E = map(int, sys.stdin.readline().split())

Graph = [] #(정점1, 정점2, 가중치)
MST=[] #가중치만 추가
parent=[] #최소스패닝트리 기록


for v in range(V+1):
	parent.append(v) #각 인덱스(각 노드)별로 부모노드를 저장
#초기에는 전부 자기자신을 부모노드로 두고있음

def findRoot(node) :
	if parent[node]==node:
		return node
	else:
		return findRoot(parent[node])

def isCycle(V1, V2): #현재간선을 추가했을때 사이클이 생기는지아닌지
	V1Root=findRoot(V1)
	V2Root=findRoot(V2)
	if V1Root == V2Root:
		return True #사이클이 생긴다.
	else : #임의로 더 수가작은 노드를 부모노드로 둔다
		if V1Root < V2Root:
			parent[V2Root]=V1Root
		else :
			parent[V1Root]=V2Root
		return False


for _ in range(E):
	A, B, C = map(int, sys.stdin.readline().split())
	Graph.append((A,B,C))

#1. 간선들 정렬
Graph.sort(key=lambda x:x[2])


#2. 간선들로 사이클이 만들어지지 않게 최소신장트리만들기
for g in Graph:
	v1, v2, w = g
	if isCycle(v1,v2):
		continue
	else:
		MST.append(w)



print(sum(MST))