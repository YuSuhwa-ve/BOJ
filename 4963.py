import sys
sys.setrecursionlimit(10**6)

def CountIL(MAP,CheckMAP,nowHindex,nowWindex):
	if CheckMAP[nowHindex][nowWindex]:#이미 방문한 경로 방문 안하기위해
		return
	else : 
		CheckMAP[nowHindex][nowWindex]=True
		if MAP[nowHindex][nowWindex]==0:
			return
		else:
			for i in range(8):
				if 0<=(nowWindex+dx[i]) and (nowWindex+dx[i])<W and 0<=(nowHindex+dy[i]) and (nowHindex+dy[i])<H :
					CountIL(MAP,CheckMAP,nowHindex+dy[i],nowWindex+dx[i])




result=[]
dx=[1,1,0,-1,-1,-1,0,1] #동,동남, 남, 남서, 서,북서, 북, 북동 의 방향
dy=[0,1,1,1,0,-1,-1,-1]

while True:
	count=0
	MAP=[]
	W,H = map(int, sys.stdin.readline().split())
	if W==0 and H==0:
		break
	for _ in range(H):
		m=list(map(int, sys.stdin.readline().split()))
		MAP.append(m)
	CheckMAP=[[False]*W for _ in range(H)]

	for i in range(H):
		for j in range(W):
			if CheckMAP[i][j]: #이미방문한(이미 센 섬)을 피하기위해
				continue
			if MAP[i][j]==1:
				count+=1
			CountIL(MAP,CheckMAP,i,j)
	result.append(count)

for r in result:
	print(r)		
