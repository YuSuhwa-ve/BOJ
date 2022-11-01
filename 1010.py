import sys

T= int(sys.stdin.readline())
fac=[1,1] #팩토리얼의 계산값을 저장하는 배열

def Fac(num):
	if num<=len(fac)-1:
		return fac[num]
	else:
		fac.append(Fac(num-1)*num)
		return fac[num]

def num_com(n,m):
	return int(Fac(m)/(Fac(n)*Fac(m-n)))

for _ in range(T):
	N,M=map(int,sys.stdin.readline().split())
	print(num_com(N,M))