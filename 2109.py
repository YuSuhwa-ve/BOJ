import sys

N=int(sys.stdin.readline())
lectures=[]
max_d=0


for _ in range(N):
	p, d=map(int, sys.stdin.readline().split())
	lectures.append((p,d))
	if max_d<d:
		max_d=d
# p 내림차순, d 오름차순으로 정렬
lectures.sort(key= lambda x: (-x[0],x[1]))

# 답 배열을 가장큰 d 만큼의 크기로 설정
result=[0]*(max_d+1)
#print(max_d)
#print(lectures)

for i in range(N):
	d=lectures[i][1]
	if result[d] ==0 :
		result[d]=lectures[i][0]
	else:
		for j in range(d-1,0,-1):
			if result[j]==0:
				result[j]=lectures[i][0]
				break
		
#print(result)
print(sum(result))
