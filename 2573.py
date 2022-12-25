import sys
from collections import deque
import copy

N, M = map(int, sys.stdin.readline().strip().split())
original_map=[]
time=0 #현재 빙산부터 탐색
count=0 #우선초기화

for _ in range(N):
	original_map.append(list(map(int, sys.stdin.readline().strip().split())))

next_map=copy.deepcopy(original_map)

dn =[-1,1,0,0]#상하좌우
dm =[0,0,-1,1]

def update_map(B_MAP,A_MAP):
#B_MAP 을 참고하여 A_MAP을 update
	for i in range(N):
		for j in range(M):
			if B_MAP[i][j]!=0: #육지일때
				sea=0 
				for d in range(4):#바다 개수세기
					next_i=i+dn[d]
					next_j=j+dm[d]
					if 0<=next_i<N and 0<=next_j<M and B_MAP[next_i][next_j]==0:
							sea+=1
				A_MAP[i][j]=0 if (A_MAP[i][j]-sea)<0 else (A_MAP[i][j]-sea)				
	# A_MAP을 B_MAP에 덮어씌우기
	for i in range(N):
		for j in range(M):
			B_MAP[i][j]=A_MAP[i][j]
				




def BFS(node_n,node_m,MAP,Check):
	queue=deque([(node_n,node_m)])
	Check[node_n][node_m]=True
	while queue:
		now_node_n, now_node_m=queue.popleft()
		for d in range(4):
			next_node_n=now_node_n+dn[d]
			next_node_m=now_node_m+dm[d]
			if 0<=next_node_n<N and 0<=next_node_m<M and MAP[next_node_n][next_node_m]!=0 and not Check[next_node_n][next_node_m]:
				Check[next_node_n][next_node_m]=True
				queue.append((next_node_n,next_node_m))
		

while count<2:
	check_map=[[False]*M for _ in range(N)] #메모리할당계속되나?
	count=0
	time+=1
	update_map(original_map,next_map)

	#빙산이 다 녹을때까지 분리되지 않을때 0 출력
	melt=True
	for n in range(N):
		if any(original_map[n]) : #0이 아닌 노드가 있으면 True
			melt=False
	if melt:
		time=0
		break

	for n in range(N):
		for m in range(M):
			if original_map[n][m]!=0 and not check_map[n][m]:
				count+=1
				BFS(n,m,original_map,check_map)


print(time)