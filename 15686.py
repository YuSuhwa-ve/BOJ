import sys

N, M = map(int, sys.stdin.readline().split())

City=[]

for _ in range(N):
	City.append(list(map(int, sys.stdin.readline().strip().split())))

print(City)
House=[]
Restaurant=[]
result = []

for y in range(N):
	for x in range(N):
		if City[y][x]==1:
			House.append((y,x))
		if City[y][x]==2:
			Restaurant.append((y,x))

def circulateChickenDistance(House, y, x):
	minChickenDistance = 100
	for h in range(len(House)):
		hy, hx = House[h]
		nowChickenDistance=abs(hy-y)+abs(hx-x)
		if minChickenDistance > nowChickenDistance:
			minChickenDistance=nowChickenDistance
	return minChickenDistance


for r in Restaurant:
	ry, rx = r
	result.append(circulateChickenDistance(House, ry, rx))

result.sort()
print(sum(result[:M]))