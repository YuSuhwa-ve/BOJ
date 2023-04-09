import sys

N=int(sys.stdin.readline())
meetings=[]

for _ in range(N):
	meeting_start, meeting_end = map(int, sys.stdin.readline().split())
	meetings.append((meeting_start,meeting_end))
meetings.sort(key=lambda x: (x[1],x[0]))

#print(meetings)

result =1
#print(meetings[0])
now_endtime=meetings[0][1]
for i in range(1,N):
	if now_endtime>meetings[i][0]:
		continue
	result+=1
	#print(meetings[i])
	now_endtime=meetings[i][1]

print(result)
