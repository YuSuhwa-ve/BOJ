import sys
from collections import deque

F, S, G, U, D = map(int, sys.stdin.readline().strip().split())


#무조건 use the stairs
if (S>G and D==0) or (S<G and U==0):
	print("use the stairs")
else:
	#BFS
	check=[-1]*1000001 # -1이면 방문 안함
	check[S]=0 #현재위치 우선방문
	queue=deque([S]) #방문한 노드 큐에 넣음
	while queue : #큐가 빌때까지 탐색
		now=queue.popleft()
		if now==G:
			print(check[G])
			break
		#갈 수 있는 인접노드 탐색
		if 0<now+U<=F and check[now+U]==-1:
			check[now+U]=check[now]+1
			queue.append(now+U)
		if 0<now-D<=F and check[now-D]==-1:
			check[now-D]=check[now]+1
			queue.append(now-D)
	if check[G]==-1:
		print("use the stairs")