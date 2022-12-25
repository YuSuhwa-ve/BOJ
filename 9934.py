import sys

K=int(sys.stdin.readline())
VisitRoutine=list(map(int,sys.stdin.readline().strip().split()))

#각 레벨당 노드의 개수
NLN=[0] #index 1=level 1 = root node의 개수
for k in range(K):
	NLN.append(2**k)

Tree=[0]*(len(VisitRoutine)+1)
matchList=[] #상근이가 도시를 방문한 순서의 Tree 인덱스들

def It(startnode):
	if startnode > len(VisitRoutine):
		return
	L = int(startnode*2)
	R= int(startnode*2+1)
	It(L)
	matchList.append(startnode)
	It(R)

It(1)

for i in range(len(VisitRoutine)):
	Tree[matchList[i]]=VisitRoutine[i]

start=1
for p in range(1,K+1):
	print(*Tree[start:start+NLN[p]])
	start+=NLN[p]
