import sys

sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
MAP = []
result = [0]

for _ in range(N):
	MAP.append(list(map(int, sys.stdin.readline().strip().split())))


def DFS(h,w):
	if MAP[h][w]==0:
		result[0]+=1
	else:
		for dh, dw in [(0,1),(1,0)]:
			nh = h+dh*MAP[h][w]
			nw = w+dw*MAP[h][w]
			if nh<N and nw<N:
				DFS(nh,nw)

DFS(0,0)

print(result[0])