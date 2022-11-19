import sys

N, M = map(int, sys.stdin.readline().split())

base = range(1,N+1)
temp=[]
def makeSequence():
	for i in range(1,N+1):
		temp.append(i)
		if len(temp)==M:
			print(*temp)
		else:
			makeSequence()
		temp.pop()

makeSequence()