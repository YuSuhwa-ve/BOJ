import sys

K ,N = map(int, sys.stdin.readline().split())

LanLines=[]
for _ in range(K):
	LanLines.append(int(sys.stdin.readline()))

def howManyLanLines(LanLines, unit):
	if unit==0:
		return -1
	sumLine=0
	for line in LanLines:
		sumLine+=line//unit
	return sumLine

start=0
end=max(LanLines)
mid=0
numOfLine=0
length=0

while start<=end:
	mid = int((start+end)/2)
	if mid==0:

	numOfLine = howManyLanLines(LanLines, mid)
	#print("mid :",mid, ",numOfLine :",numOfLine)
	if numOfLine >= N:
		start=mid+1
		if length<mid :
			length=mid
	elif numOfLine < N:
		end=mid-1

#print(mid-1)
print(length)
