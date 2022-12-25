import sys

T= int(sys.stdin.readline())

for _ in range(T):
	A, B = map(int, sys.stdin.readline().split())
	if A>B:
		temp = B
		B=A
		A=temp
	parentA=[A]
	while True:
		if A==1 : 
			break
		if A%2==0 : #짝수 즉 왼쪽자식
			A=A//2
			parentA.append(A)
		else: #홀수 즉 오른쪽 자식
			A=(A-1)//2
			parentA.append(A)
	
	while True:
		if B in parentA:
			print(10*B)
			break
		if B%2==0:
			B=B//2
		else : 
			B=(B-1)//2