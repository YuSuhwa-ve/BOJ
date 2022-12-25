import sys


INPUT = list(map(str,sys.stdin.readline().strip().split()))


H=int(INPUT[0])

maxNodeNum=0 #전체노드(1~전체노드개수)의 개수 -> 일반완전이진트리는 0~전체노드개수-1
for h in range(H+1): #루트= 2**0, level1=2**1, ....
	maxNodeNum+=2**h

nowNode=0 #일단 루트노드부터 시작(일반완전이진트리기준)
if len(INPUT)<2:
	Path=[]
else:
	Path=list(INPUT[1])
	
for p in Path :
	if p=='L':
		nowNode=int(nowNode*2)+1
	if p=='R':
		nowNode=int(nowNode*2)+2

print(maxNodeNum-nowNode)