import sys

N,K=map(int,sys.stdin.readline().strip().split())

result=0

for h in range(N+1):
	for m in range(60):
		for s in range(60):
			if K==0:
				if len(str(h))==1 or (str(K) in str(h)):
					result+=1
				elif len(str(m))==1 or (str(K) in str(m)):
					result+=1
				elif len(str(s))==1 or (str(K) in str(s)):
					result+=1
			else:
				if str(K) in str(h):
					result+=1
				elif str(K) in str(m):
					result+=1
				elif str(K) in str(s):
					result+=1
		
print(result)
	