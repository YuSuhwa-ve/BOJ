import sys

N, S = map(int, sys.stdin.readline().split())

sequence = list(map(int, sys.stdin.readline().strip().split()))

temp=[]
result=[]

def makeSubSequence(first):
	for nextH in range(first,N): #각 부분 수열에서 가능한 다음항
		temp.append(sequence[nextH])
		if sum(temp)==S:
			result.append(temp)
		makeSubSequence(nextH+1)
		temp.pop()

makeSubSequence(0)	
		
#print(result)
print(len(result))