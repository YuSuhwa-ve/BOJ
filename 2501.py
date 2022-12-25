I=list(map(int,input().split()))
N=I[0]
K=I[1]
Q=list(range(1,N+1))
P=[] #약수리스트
count=0
for q in Q:
	if N%q==0:
		P.append(q)
		count+=1
	if count==K :
		break

print(P[K-1])
