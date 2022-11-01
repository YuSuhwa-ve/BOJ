import sys
sys.setrecursionlimit(10**6)

N= int(sys.stdin.readline())

Tree=[[] for _ in range(N+1)]
Tree[0]=-1 #index 0은 쓰지 않고, 1 부터 루트

for _ in range(N-1):
	A, B = map(int,sys.stdin.readline().split())
	Tree[A].append(B)
	Tree[B].append(A)

Check=[] #방문여부판단
result=[0]*(N+1) #각 리프노드마다 루트~리프노드 까지의 최단 간선개수

def findLeaf(node,count):
	if isLeaf(node):#잎노드일때=연결된노드가 전부 방문상태일때
		Check.append(node)
		result[node]=count # 루트~잎까지의 간선수
	else : #잎노드가 아닐때
		Check.append(node)
		for n in Tree[node]:
			if not n in Check:
				findLeaf(n,count+1) #연결된노드중방문하지않은노드 탐색(이때count++)
		
def isLeaf(node):
	signal = True
	for v in Tree[node]:
		if v in Check:
			signal= signal and True
		else:
			signal=False
	return signal

findLeaf(1,0)

if sum(result) %2==0:
	print("No")
else:
	print("Yes")