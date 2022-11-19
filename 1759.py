import sys

L, C = map(int, sys.stdin.readline().split())

CT= sys.stdin.readline().strip().split()

result = []

CT.sort() #알파벳 순서로 정렬

vowel=['a','e','i','o','u']
temp=[]

def codeVowelCondition(code) :
	howMany=0
	for c in code:
		if c in vowel:
			howMany+=1
	if howMany==0 or howMany>L-2:
		return False
	else:
		return True
	

def makeSecretCode(start):
	for nextC in range(start,C) : #현재 수열의 현재 자리에서 가능한 항
		temp.append(CT[nextC])
		if len(temp)==L and codeVowelCondition(temp):
			print("".join(temp))
		makeSecretCode(nextC+1)
		temp.pop()

makeSecretCode(0)