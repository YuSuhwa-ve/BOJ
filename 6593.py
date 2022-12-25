from pickle import NEXT_BUFFER
import sys
from collections import deque

dl=[0,0,0,0,1,-1]#동서남북상하
dr=[0,0,1,-1,0,0]
dc=[1,-1,0,0,0,0]

def BFS(MAP,CHECK, NODE_L, NODE_R, NODE_C,L,R,C,GOAL):
    queue=deque([(NODE_L,NODE_R,NODE_C)])
    CHECK[NODE_L][NODE_R][NODE_C]+=1
    while queue:
        now_l, now_r, now_c=queue.popleft()
        for d in range(6):
            next_l=now_l+dl[d]
            next_r=now_r+dr[d]
            next_c=now_c+dc[d]
            if 0<=next_l<L and 0<=next_r<R and 0<=next_c<C:
                if CHECK[next_l][next_r][next_c]==-1 and MAP[next_l][next_r][next_c]!='#':
                    CHECK[next_l][next_r][next_c]=CHECK[now_l][now_r][now_c]+1
                    queue.append((next_l,next_r,next_c))
                    if next_l==GOAL[0] and next_r==GOAL[1] and next_c==GOAL[2]:
                        return 0
while True:
    L, R, C = map(int, sys.stdin.readline().split()) #층, 행, 열
    if L==0 and R==0 and C==0:
        break
    building=[]
    start=[] #순서대로 시작지점의 층,행,열
    end=[] # 끝지점의 층,행,열
    for l in range(L):
        floor=[]
        for r in range(R):
            floor.append(list(sys.stdin.readline().strip()))
            if 'S' in floor[r]:
                start.append(l)
                start.append(r)
                start.append(floor[r].index('S'))
            if 'E' in floor[r]:
                end.append(l)
                end.append(r)
                end.append(floor[r].index('E'))
        sys.stdin.readline()
        building.append(floor)
    
    check_building=[[[-1]*C for _ in range(R)] for _ in range(L)]

    BFS(building,check_building,start[0],start[1],start[2],L,R,C,end)

    if check_building[end[0]][end[1]][end[2]]!=-1:
        print("Escaped in",check_building[end[0]][end[1]][end[2]],"minute(s).")
    else:
        print("Trapped!")
    
