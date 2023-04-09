
'''
F=[0,1]
N=int(input())
i=1
while F[i]<=N:
    F.append(F[i]+F[i-1])
    i+=1
print(F)
'''


T=int(input())
for _ in range(T):
	N=int(input())
	F=[0,1]
	result=[]
	i=1
	while F[i]<=N:
		F.append(F[i]+F[i-1])
		i+=1
	print(F)
	print("i :",i)
	while N>0:
		if F[i]<=N:
			result.append(F[i])
			N-=F[i]
		i-=1
	result.reverse()
	for a in result:
		print(a)


'''

F=[0,1]
T=int(input())
for _ in range(T):
	N=int(input())
	result=[]
	i=1
	while F[i]<=N:
		F.append(F[i]+F[i-1])
		i+=1
	for n in range(i,0,-1):
		if F[n]<=N:
			result.append(F[n])
			N-=F[n]
		if N==0:
			break
	print(result)
'''
