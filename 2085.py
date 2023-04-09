import sys
import math

N, M = map(int,sys.stdin.readline().split())

tree = list(map(int,sys.stdin.readline().strip().split()))

tree.sort()

start = 0
end = max(tree)
maxTreeH = 0

def totalTree(treelist,h):
    sum=0
    for tree in treelist:
        if tree>h:
            sum+=tree-h
    return sum


while(start<=end):
    mid = math.floor((start+end)/2)
    tempTreeSum = totalTree(tree,mid)
    if tempTreeSum==M:
        print(mid)
        exit()
    elif tempTreeSum>M:
        start=mid+1
        if mid>maxTreeH:
            maxTreeH=mid
    elif tempTreeSum<M:
        end=mid-1

print(maxTreeH)
