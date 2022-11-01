import sys

def addVertax(newNode):
	nextNode=Tree[0][0]
	while True:
		if not Tree[nextNode]:#해당 트리에 자식노드가 없으면
			Tree[nextNode].append(newNode)
			break
		else:
			nextNode=Tree[nextNode][0]


N, M =map(int, sys.stdin.readline().split())

Tree=[[] for _ in range(N)]

for m in range(1,M+1):
	Tree[0].append(m)

for n in range(M+1,N) : 
	addVertax(n)

for i in range(N):
	for j in range(len(Tree[i])):
		print(i,Tree[i][j])
			
	
	