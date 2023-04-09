import sys

alpabet="abcdefghijklmnopqrstuvwxyz"
S = input()
index=[]
count=1
for n in S:
	index.append(alpabet.find(n))
for i in len(index)-1:
	if index[i]>index[i+1]:
		count+=1

print(count)