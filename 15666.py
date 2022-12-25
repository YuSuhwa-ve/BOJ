'''
import sys
from itertools import product

N, M = map(int, sys.stdin.readline().split())

NList = list(map(int, sys.stdin.readline().strip().split()))
#print(NList)

allP=list(product(NList,repeat=M))

#중복제거
allP=list(set(allP))

allP.sort(key=lambda x:tuple(x[m] for m in range(M)))

resultP=[]

for o in allP:
	isAsOrder=True
	for m in range(M-1):
		if o[m]>o[m+1]:
			isAsOrder=False
			break
	if isAsOrder:
		resultP.append(o)


for r in resultP:
	print(*r)
    '''

import sys
from itertools import product

N, M = map(int, sys.stdin.readline().split())

NList = list(map(int, sys.stdin.readline().strip().split()))

allP=list(product(NList,repeat=M))

#중복제거
allP=list(set(allP))

#비 내림차순제거
resultP=[]

for o in allP:
	isAsOrder=True
	for m in range(M-1):
		if o[m]>o[m+1]:
			isAsOrder=False
			break
	if isAsOrder:
		resultP.append(o)

#사전순정렬
resultP.sort(key=lambda x:tuple(x[m] for m in range(M)))


for r in resultP:
	print(*r)