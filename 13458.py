import sys

N= int(sys.stdin.readline())
classroom=list(map(int, sys.stdin.readline().strip().split()))
B, C =map(int, sys.stdin.readline().split())
result=N

for n in range(N):
	now_student=classroom[n]-B
	if now_student%C==0:
			result+=now_student/C
	else : 
			result+=now_student//C+1

print(int(result))
