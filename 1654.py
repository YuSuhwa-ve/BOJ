import sys

K ,N = map(int, sys.stdin.readline().split())

LanLines=[]
for _ in range(K):
	LanLines.append(int(sys.stdin.readline()))

def howManyLanLines(LanLines, unit):
	sumLine=0
	for line in LanLines:
		sumLine+=line//unit
	return sumLine

start=0
end=max(LanLines)

while start<=end:
	mid = int((start+end)/2)
	numOfLine = howManyLanLines(LanLines, mid)
	if numOfLine == N+1:
		print(mid-1)
		break
	elif numOfLine > N+1:
		start=mid+1
	elif numOfLine < N+1:
		end=mid-1





		ㅇㄹㅇㄹㅇㄹ

print("?")	
	