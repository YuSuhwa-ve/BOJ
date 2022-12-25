N=int(input())
Person=[]
result=[1]*N
for _ in range(N):
	p=list(map(int,input().split()))
	Person.append(p)

for i in range(0,N):
	for j in range(i+1,N):
		if Person[i][0]<Person[j][0] and Person[i][1]<Person[j][1]:
			result[i]+=1
		if Person[j][0]<Person[i][0] and Person[j][1]<Person[i][1]:
			result[j]+=1

print(*result)
