import sys
import math

N = int(sys.stdin.readline())
budgetRequest = list(map(int,sys.stdin.readline().strip().split()))
totalBudget = int(sys.stdin.readline())

if sum(budgetRequest)<=totalBudget:
    print(max(budgetRequest))
    exit()

maxTotalBuget = 0
start = 0
end = max(budgetRequest)

def expectedBudget(bugetList,upperBuget,limit):
    result=0
    for b in bugetList:
        if b<=upperBuget:
            result+=b
        else :
            result+=upperBuget
    return result
    

while(start<=end):
    mid=math.floor((start+end)/2)
    tempTotalBuget=expectedBudget(budgetRequest,mid,totalBudget)
    if tempTotalBuget==totalBudget:
        print(mid)
        exit()
    elif tempTotalBuget>totalBudget:
        end=mid-1
    elif tempTotalBuget < totalBudget:
        if tempTotalBuget>maxTotalBuget:
            maxTotalBuget=mid
        start=mid+1

print(maxTotalBuget)