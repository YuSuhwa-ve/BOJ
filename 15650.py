import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().split())

allP=list(permutations(range(1,N+1),M))

resultP=[]

for p in allP:
	isAsOrder=True
	for m in range(M-1):
		if p[m]>p[m+1]:
			isAsOrder=False
			break
	if isAsOrder:
		resultP.append(p)

for result in resultP:
	print(*result)