import sys

N,M=map(int,input().split())
Cards=list(map(int, input().split()))
result=0

#카드들을 내림차순으로 정렬한후, M이상인 카드값을 제거
Cards.sort(reverse=True)
RM=[]
for i in range(0,N):
	if Cards[i]>=M :
		RM.append(i)
	else :
		break
if RM:
	Cards=Cards[RM.pop():]
N=len(Cards)

#가장 큰값 + 가장 작은값+ 그다음으로 작은 값 조합이 M보다 큰지 검사
for p in range(0,N) :
	for i in range(-1,p-N+1,-1):
		for j in range(i-1,p-N,-1):
			s=Cards[p]+Cards[i]+Cards[j]
			if s>M:
				break
			elif s==M:
				result=s
				break
			else :
				if s>result :
					result=s
		if s>=M:
			break
	if s==M:
		break
				
print(result)
