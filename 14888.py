'''
import sys
import math
from itertools import permutations

N =int(sys.stdin.readline())
NUM=list(map(int,sys.stdin.readline().strip().split()))
OP=list(map(int,sys.stdin.readline().strip().split()))


#연산자들을 하나의 배열로 변형
op=['+','-','*','/']
NEW_OP=[]

for i in range(4):
	if OP[i]!=0:
		for _ in range(OP[i]):
		    NEW_OP.append(op[i])

#연산자들을 순열로 돌림
OP_PER=list(permutations(NEW_OP,len(NEW_OP)))
OP_PER=list(set(OP_PER))

result=[0]*len(OP_PER)

for i in range(len(OP_PER)):
	TEM_EX=[str(NUM[0])]
	
	for j in range(len(NEW_OP)):
		TEM_EX.append(OP_PER[i][j])
		TEM_EX.append(str(NUM[1+j]))
	
	result[i]=TEM_EX[0]
	for k in range(1,len(TEM_EX),2):
		result[i]=math.trunc(eval(str(result[i])+TEM_EX[k]+TEM_EX[k+1]))
    


print(max(result))
print(min(result))
'''
import sys
import math
from itertools import permutations

N =int(sys.stdin.readline())
NUM=list(map(int,sys.stdin.readline().strip().split()))
OP=list(map(int,sys.stdin.readline().strip().split()))


#연산자들을 하나의 배열로 변형
op=['+','-','*','/']
NEW_OP=[]

for i in range(4):
	if OP[i]!=0:
		for _ in range(OP[i]):
		    NEW_OP.append(op[i])

#연산자들을 순열로 돌림
OP_PER=list(permutations(NEW_OP,len(NEW_OP)))
OP_PER=list(set(OP_PER))

result=[0]*len(OP_PER)

for i in range(len(OP_PER)):
	TEM_EX=NUM[0]
	
	for j in range(len(NEW_OP)):
		TEM_EX=math.trunc(eval(str(TEM_EX)+OP_PER[i][j]+str(NUM[1+j])))
	
	result[i]=TEM_EX

    


print(max(result))
print(min(result))

print(round(3.1415))