import sys
from collections import deque

R, C = map(int, sys.stdin.readline().strip().split())
Farm=[]
Check=[]
for _ in range(R):
	Farm.append(list(sys.stdin.readline().strip()))
	Check.append([False]*C)
dr=[1,-1,0,0] #상하좌우
dc=[0,0,-1,1]


def set_fense(s_r,s_c,MAP): #양의 위치를 입력받아 양의 상하좌우에 울타리를 친다.
	for d in range(4):
		a_r=s_r+dr[d]
		a_c=s_c+dc[d]
		if 0<=a_r<R and 0<=a_c<C:
			if MAP[a_r][a_c]=='S' or MAP[a_r][a_c]=='D':#어차피 여기 방향으로는 양이 있기에 늑대가 못들어옴
				continue
			elif MAP[a_r][a_c]=='W':#양의 상하좌우에 늑대있는것
				print(0)
				sys.exit(0)
			else : #빈경우'
				MAP[a_r][a_c]='D'

def BFS(w_r,w_c,check,MAP):
	#현재 노드 방문
	Check[w_r][w_c]=True
	queue=deque([(w_r,w_c)])
	while queue:
		now_r, now_c = queue.popleft()
		if MAP[now_r][now_c]=='S':
			print(0)
			sys.exit(0)
		for d in range(4):
			next_r=now_r+dr[d]
			next_c=now_c+dc[d]
			if 0<=next_r<R and 0<=next_c<C and MAP[next_r][next_c]=='.' and not Check[next_r][next_c]:
				Check[next_r][next_c]=True
				queue.append((next_r,next_c))

#일단 양 주위에 울타리를 다 치기
for r in range(R):
	for c in range(C):
		if Farm[r][c]=='S':
			set_fense(r,c,Farm)

#다 울타리를 쳤는데도 늑대가 양을 보면 그냥 막을수없는거다.
for r in range(R):
	for c in range(C):
		if Farm[r][c]=='W':
			BFS(r,c,Check,Farm)

#모든 늑대가 양을 못만남
print(1)

for r in range(R):
	for c in range(C):
		print(Farm[r][c],end='')
	print()
	