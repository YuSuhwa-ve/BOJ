import sys
from collections import deque 
sys.setrecursionlimit(10**6)

N, K=map(int, sys.stdin.readline().split())

def BFS(now_Node,Queue,count):
	if now_Node==K:
		print(count[now_Node])
		return
	for x in (now_Node-1,now_Node+1,now_Node*2):
		if 0<=x<=100000 and not count[x]:
			count[x]=count[now_Node]+1
			Queue.append(x)
	if Queue:
		BFS(Queue.popleft(), Queue,count)

count=[0]*100001
queue=deque([N])
BFS(queue.popleft(),queue,count)
