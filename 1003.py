import sys
sys.setrecursionlimit(10**6)

T=int(sys.stdin.readline())
#튜플의 첫번째는 0의 개수, 두번째는 1의 개수이다)
d=[(1,0),(0,1)]

def how_many_0_and_1(num):
	if num<=len(d)-1: #이미 값이 있는 경우
		return d[num]
	else: #값이 없는 경우
		n1_0,n1_1 = how_many_0_and_1(num-1)
		n2_0, n2_1=how_many_0_and_1(num-2)
		d.append((n1_0+n2_0,n1_1+n2_1))
		return (n1_0+n2_0,n1_1+n2_1)
		

for _ in range(T):
	N=int(sys.stdin.readline())
	print(*how_many_0_and_1(N))
	