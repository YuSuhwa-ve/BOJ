M=int(input())
N=int(input())
S=[]
result=[]
i=1
maxI=0
while True:
	if i*i>=N:
		maxI=i
	if maxI!=0:
		break;
	i+=5

for i in range(1,maxI+1):
	S.append(i*i)

print(S)

for s in S:
	if s>N :
		break
	elif s>=M:
		result.append(s)

print(result)

if result:
	print(sum(result))
	print(result[0])
else :
	print(-1)
	
