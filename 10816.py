import sys
import math


n = int(sys.stdin.readline())

N = list(map(int,sys.stdin.readline().strip().split()))
m= int(sys.stdin.readline())
M = list(map(int,sys.stdin.readline().strip().split()))
result = []

N.sort()

NN=[[N[0],1]]
flag = 1
for i in range(1,n) :
    if N[i-1]==N[i]:
        flag+=1
    else:
        NN[len(NN)-1][1]=flag
        NN.append([N[i],1])
        flag=1

if flag!=1:
     NN[len(NN)-1][1]=flag

def binarySearch(value,array,arrayLen):
    start=0
    end=arrayLen-1
    while(start<=end):
        mid = math.floor((start+end)/2)
        if array[mid][0] == value:
            return mid
        elif  array[mid][0] > value:
            end=mid-1
        elif array[mid][0] < value:
            start=mid+1
    return -1





for mm in M:
    NNi = binarySearch(mm,NN,len(NN))
    if NNi == -1:
        result.append(0)
    else:
        result.append(NN[NNi][1])

print(*result)