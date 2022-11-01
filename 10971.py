import sys

N=int(sys.stdin.readline())
W=[]
result=[]
for _ in range(N):
    W.append(list(map(int,sys.stdin.readline().strip().split())))

def DFS(node,check,graph,count,start):
    global mincount
    if node in check : #이미 방문한 노드일때 
        return
    else : #처음방문한 노드일때
        check.append(node) # 방문표시
        
        if len(check)==N: #현재노드까지 해서 전부 방문
            nowcount=count+graph[node][start] #마지막노드->시작노드
            if mincount>nowcount:
                mincount=nowcount
        
        for i in range(len(graph[node])):
            if graph[node][i] != 0 and not(i in check):
                DFS(i,check,graph,count+graph[node][i],start)

for i in range(N):
    Check=[]
    mincount=10**6
    DFS(i,Check,W,0,i)
    result.append(mincount)

print(min(result))

