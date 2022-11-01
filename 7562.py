import sys
from collections import deque

T= int(sys.stdin.readline())

#탐색방향 : (x-2,y-1 ), (x-2,y+1 ), (x-1, y-2), (x-1, y+2), (x+1, y-2), (x+1,y+2 ), (x+2, y-1), (x+2,y+1 )
dx=[-2,-2,-1,-1, 1,1, 2,2]
dy=[-1, 1,-2, 2,-2,2,-1,1]

def BFS(x,y,g_x,g_y,check,l):
	#방문 후 큐에 넣기
	check[x][y]+=1
	queue=deque([(x,y)])
	while queue: #큐가 빌때까지 탐색
		now_x, now_y = queue.popleft() #현재노드(이미방문됨)
		if now_x == g_x and now_y == g_y: #목표도달
			print(check[now_x][now_y])
			return
		#탐색(방문후 큐에넣기)
		for d in range(8):
			next_x=now_x+dx[d]
			next_y=now_y+dy[d]
			if 0<=next_x<l and 0<=next_y<l and check[next_x][next_y]==-1:
				check[next_x][next_y]=check[now_x][now_y]+1
				queue.append((next_x, next_y))

for _ in range(T):
	L=int(sys.stdin.readline())
	NOW_x, NOW_y = map(int, sys.stdin.readline().strip().split())
	GOAL_x, GOAL_y = map(int, sys.stdin.readline().strip().split())
	Check=[[-1]*L for _ in range(L)]

	BFS(NOW_x, NOW_y,GOAL_x,GOAL_y,Check, L)