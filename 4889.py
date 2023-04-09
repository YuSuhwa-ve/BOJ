i=0
while True:
	result=0
	C=input()
	if '-' in C:
		break
	count=0
	for c in C:
		if c=='{':
			count+=1
		elif c=='}':
			count-=1
	i+=1
	result=count/2
	print(i,".",result)
	
