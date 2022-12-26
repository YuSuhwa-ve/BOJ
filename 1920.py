import sys

N = int(sys.stdin.readline())
A= list(map(int,sys.stdin.readline().strip().split()))
A.sort()

def binarySearch(List, start, end, value):
	if start > end:
		return -1
	mid = int((start+end)/2) #int는 무조건 내림
	if List[mid]==value:
		return mid
	elif List[mid]<value:
		return binarySearch(List,mid+1,end,value)
	elif List[mid]>value:
		return binarySearch(List, start,mid-1,value)

M = int(sys.stdin.readline())
B= list(map(int,sys.stdin.readline().strip().split()))
for b in B:
	if binarySearch(A,0,N-1,b)==-1:
		print(0)
	else:
		print(1)
