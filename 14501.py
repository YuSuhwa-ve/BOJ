N=int(input())
Schedule=[]
result=0 #최대수익값

# Schedule=[[Ti,Pi],[...]...],index+1=날짜
for i in range(0,N):
	s=list(map(int,input().split()))
	Schedule.append(s)


def find_maxP(now_P,now_index):
	global result,N
	#print("now_날짜",now_index+1,"||now_P",now_P)
	if now_index==N:
		if now_P>result:
			print("끝조합",now_index,'||',now_P)
			result=now_P
	for i in range(now_index,N):
		if i+Schedule[i][0]>N:
			if now_P>result:
				print("끝조합",now_index,'||',now_P)
				result=now_P
			continue
		else:

			#now_P+=Schedule[i][1]
			#print("날짜",i+1,"||더해지는일정", Schedule[i],"||now_P",now_P)
			find_maxP(now_P+Schedule[i][1],i+Schedule[i][0])

find_maxP(0,0)
print(result)
