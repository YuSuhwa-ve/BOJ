'''
import sys

N = int(sys.stdin.readline())

Path = list(map(int, sys.stdin.readline().strip().split()))
parents=[-1]*(N+1) #일단 전부 루트로 초기화
stack=[]

for p in Path:
	if p in stack: #이전에 있는지검사
		data = stack.pop()#data는 p의 자식
		parents[data]=p
		while data!=p:
			data=stack.pop()
	stack.append(p) #일단 스택에 넣기

K=0
for n in range(1,N+1):
	if parents[n]==-1:
		K=n
		break

print(K)
print(*parents[:K])
'''
import sys

N = int(sys.stdin.readline())

Path = list(map(int, sys.stdin.readline().strip().split()))
parents=[-10]*(N+1) #일단 전부 초기화
stack=[]

parents[Path[0]]=-1 #첫번째는 루트
stack.append(Path[0]) #일단 스택에 넣기

for n in range(1,N):
	if Path[n] in stack: #이전에 있는지검사
		data = stack.pop()#data는 p의 자식
		parents[data]=Path[n]
		while data!=Path[n] :
			data=stack.pop()
	stack.append(Path[n]) #일단 스택에 넣기

K=0
for n in range(1,N+1):
	if parents[n]==-10:
		K=n
		break

print(K)
print(*parents[:K])