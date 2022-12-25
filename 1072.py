import sys

X, Y = map(int, sys.stdin.readline().split())

minPlusGame=1000000000*10000
start=1
end = 1000000000*10000 #일단 end를 엄청 큰수로 두자
def winningRate(x,y):
    return int(100*y/x)

originWinningRate=winningRate(X,Y)
#print(originWinningRate)
if originWinningRate>=99:
        print(-1)
        exit()

        
while start<=end:
    mid=int((start+end)/2)
    #print("start : ",start, ", end : ", end, ", mid :", mid,",승률:",winningRate(X+mid,Y+mid),",최소게임 :",minPlusGame)
    if winningRate(X+mid,Y+mid)-originWinningRate>0:
        if minPlusGame>mid:
            minPlusGame=mid
        end=mid-1
    else:
        start=mid+1
        
    
print(minPlusGame)
