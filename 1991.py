import sys

N= int(sys.stdin.readline())
resultPreT=[] #각각 전위,중위, 후위 순회시 저장되는 배열
resultIT=[]
resultPostT=[]
Tree= {}

def addParentNode(parent, child):
	if child != '.':
		Tree[child]=[parent]

for _ in range(N):
	node, leftC, rightC = map(str, sys.stdin.readline().strip().split())
	if node in Tree :
		Tree[node].append(leftC)
		addParentNode(node,leftC)
		Tree[node].append(rightC)
		addParentNode(node,rightC)
	else : #루트노드의 경우
		Tree[node]=[0,leftC,rightC]
		addParentNode(node,leftC)
		addParentNode(node,rightC)


def PreT(Tree, startNode):
	if startNode=='.':
		return
	resultPreT.append(startNode)
	L,R = Tree.get(startNode)[1:]
	PreT(Tree, L)
	PreT(Tree, R)

def IT(Tree, startNode):
	if startNode=='.':
		return
	L,R = Tree.get(startNode)[1:]
	IT(Tree,L)
	resultIT.append(startNode)
	IT(Tree,R)

def PostT(Tree,startNode):
	if startNode=='.':
		return
	L,R = Tree.get(startNode)[1:]
	PostT(Tree,L)
	PostT(Tree,R)
	resultPostT.append(startNode)


PreT(Tree, 'A')
IT(Tree,'A')
PostT(Tree,'A')

print(''.join(resultPreT))
print(''.join(resultIT))
print(''.join(resultPostT))

