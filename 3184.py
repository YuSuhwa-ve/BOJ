import sys
from collections import deque

def BFS(MAP,CHECK,NODE_R,NODE_C,SHEEP,WOLF,I,R,C):
	queue=deque([(NODE_R,NODE_C)])
	CHECK[NODE_R][NODE_C]=True
	dr=[-1,1,0,0]#상하좌우
	dc=[0,0,-1,1]
	while queue:
		now_r, now_c =queue.popleft()
		if MAP[now_r][now_c]=='o':
			SHEEP[I]+=1
		if MAP[now_r][now_c]=='v':
			WOLF[I]+=1
		for d in range(4):
			next_r=now_r+dr[d]
			next_c=now_c+dc[d]
			if 0<=next_r<R and 0<=next_c<C and not CHECK[next_r][next_c] and MAP[next_r][next_c]!='#':
				CHECK[next_r][next_c]=True
				queue.append((next_r,next_c))

R, C = map(int, sys.stdin.readline().split())
yard =[]

for _ in range(R):
	yard.append(list(sys.stdin.readline().strip()))

check=[[False]*C for _ in range(R)]
count_sheep=[]#각 영역에 양이 얼마나 남았는지 저장
count_wolf=[]#각 영역에 늑대가 얼마나 남았는지 저장
index=-1#영역의 인덱스

for r in range(R):
	for c in range(C):
		if not check[r][c] and yard[r][c]!='#':
			count_sheep.append(0)
			count_wolf.append(0)
			index+=1
			BFS(yard,check,r,c,count_sheep,count_wolf,index,R,C)
for i in range(index+1):
	if count_sheep[i]>count_wolf[i]:
		count_wolf[i]=0
	else:
		count_sheep[i]=0

print(sum(count_sheep),sum(count_wolf))
			