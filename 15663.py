import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().split())

NList = list(map(int, sys.stdin.readline().strip().split()))

allP=list(permutations(NList,M))
#중복제거
setP=set(allP)

resultP=list(setP)

resultP.sort(key=lambda x:tuple(x[m] for m in range(M)))

for r in resultP:
	print(*r)