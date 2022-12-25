import sys
sys.setrecursionlimit(10**6)

def CountA(MAP,CheckMAP,nowYindex,nowXindex):
	if CheckMAP[nowYindex][nowXindex] : 
		return
	else : 
		CheckMAP[nowYindex][nowXindex]=True
		if MAP[nowYindex][nowXindex]==0:
			return
		else : 
			global count
			result[count]+=1

			#print(count, "result in CountA :",result)

			for i in range(4):
				if 0<=(nowYindex+dy[i]) and (nowYindex+dy[i]<N) and (0<=nowXindex+dx[i]) and (nowXindex+dx[i]<N) : 
					CountA(MAP,CheckMAP,nowYindex+dy[i],nowXindex+dx[i])

N=int(input())
#print(N)
result=[] #각 단지들의 아파트 개수를 저장하는 배열
count =-1  #result 배열의 index
dx=[1,-1,0,0]
dy=[0,0,1,-1]
MAP=[]
CheckMAP=[[False]*N for _ in range(N)]
for _ in range(N):
	m=list(map(int, input()))
	MAP.append(m)
#print(MAP)
#print(CheckMAP)
for i in range(N):
	for j in range(N):
		if CheckMAP[i][j]:
			continue
		if MAP[i][j]==1:
			count+=1
			result.append(0)

			#print("result" ,result)

		CountA(MAP,CheckMAP,i,j)

result.sort()
print(len(result))
for r in result:
	print(r)
