import sys
from itertools import combinations

N=int(sys.stdin.readline())
DATA=[]

for _ in range(N):
	DATA.append(list(map(int,sys.stdin.readline().strip().split())))

#일단 가능한 조합을 뽑는다. 이때 팀은 0~N-1개인 걸로
com=list(combinations(range(0,N),int(N/2)))

#각 팀 조합일때 능력차를 저장할 배열
result=[100]*int(len(com)/2)

#각 팀 조합일때 능력차 계산
for n in range(int(len(com)/2)):
	sum_start=0
	sum_link=0
	team_start=list(combinations(com[n],2))
	team_link=list(combinations(com[len(com)-1-n],2))
	for i in range(len(team_start)):
		start_c, start_r=team_start[i]
		sum_start+=DATA[start_c][start_r] + DATA[start_r][start_c]
		link_c, link_r=team_link[i]
		sum_link+=DATA[link_c][link_r] + DATA[link_r][link_c]
	result[n]=abs(sum_start-sum_link)	

print(min(result))