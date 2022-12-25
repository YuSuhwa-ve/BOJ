import sys

N, K=map(int, sys.stdin.readline().strip().split())
k=list(map(int,sys.stdin.readline().strip().split()))
k.sort(reverse=True)

'''for n in str(N):
	for kk in k:
		if n==kk:
			두번째로 큰 자릿수 검사
				두번째 큰 자릿수=kk
					세번째로 큰 자릿숫 검사
		elif n<kk:
			result+='kk'+str(max(k))+...
'''


def MakeBigN(depth,result,flag):
	if depth==len(str(N)):
		return result

	if flag:
		MakeBigN(depth+1,result+str(max(k)),True)

	n=int(str(N)[depth]) #현재 n은 N의 depth만큼의 큰 자릿수이다.
	for kk in k:
		if n==kk:
			return MakeBigN(depth+1,result+str(kk),False)
			
		elif n>kk:
			return MakeBigN(depth+1,result+str(kk),True)
			

result=MakeBigN(0,'',False)
print(result)


			