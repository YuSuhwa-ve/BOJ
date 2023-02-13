import sys

n = int(sys.stdin.readline())

bsize = list(map(int,sys.stdin.readline().strip().split()))
bmax = [1]
box = [(1,bsize[0])]

def BMAX(i):
	for j in range(i-1,-1,-1):
		if bsize[j]<bsize[i]:
			if box[j][1]<bsize[i]:
				return box[j][0]+1
			else : 
				return bmax[j]+1
	return 1


for i in range(1,n):
	if bsize[i]>box[i-1][1]:
		bmax.append(box[i-1][0]+1)
		box.append((bmax[i],bsize[i]))
	else:
		bmax.append(BMAX(i))
		if box[i-1][0] > bmax[i]:
			box.append(box[i-1])
		elif box[i-1][0] == bmax[i]:
			if box[i-1][1] <= bsize[i]:
				box.append(box[i-1])
			else:
				box.append((bmax[i],bsize[i]))
		else:
			box.append((bmax[i],bsize[i]))
	

print(box[n-1][0])