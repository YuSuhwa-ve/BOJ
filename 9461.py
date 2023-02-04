import sys
sys.setrecursionlimit(10**6)

P=[0,1,1,1,2,2] #P(1)~P(5)

def PadoP(n):
	if len(P)-1 >= n:
		return P[n]
	else :
		P.append(PadoP(n-1)+PadoP(n-5))
		return P[n]
		

T = int(sys.stdin.readline())

for _ in range(T):
	N = int(sys.stdin.readline())
	print(PadoP(N))
