
T=int(input()) #테스트 케이스 개수
for _ in range(T):
	N=int(input()) #통나무 개수
	list = list(map(int, input().split())) #통나무 배열
	result=0 #통나무 배열의 최종 난이도
	Rlist=[]
	for i in range(N):
		Rlist.append(0) # 통나무 최종 배열
	list.sort() #1. 리스트 정렬
	Rlist[0]=list[N-1]# 2. 가운데에 가장 큰 원소 넣기
	Rlist[N-1]=list[N-2]
	Rlist[1]=list[N-3]
	ri=1
	li=1
	for i in range(N-4,-1,-1):
		if abs(Rlist[ri]-list[i])>=abs(Rlist[N-li]-list[i]):
			Rlist[ri+1]=list[i]
			if abs(Rlist[ri]-list[i])>result:
				result=abs(Rlist[ri]-list[i])
			ri+=1
		else:
			Rlist[N-li-1]=list[i]
			if abs(Rlist[N-li]-list[i])>result:
				result=abs(Rlist[N-li]-list[i])
			li+=1
	print(result)
	