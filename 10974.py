n=int(input()) #입력받은 n
N0=list(range(1,n+1)) #1부터 n까지의 수가 담긴 배열
R0=[]

def pm(N,R):
	if len(N)==0:
		print(*R)
	else:
		for p in N:
			R1=R.copy()
			R1.append(p)
			N1=N.copy()
			N1.remove(p)
			pm(N1,R1)

pm(N0,R0)
		


'''
#for문으로 작성
n=int(input()) #입력받은 n
N=list(range(1,n+1)) #1부터 n까지의 수가 담긴 배열

for i in N: #첫번째 원소
	R=[]
	R.append(i) #R=[1]
	if n==1:
		print(*R)
		continue
	N1=N.copy() 
	N1.remove(i) #N1=[2345]
	for p in N1 : #두번째 원소
		R1=R.copy()
		R1.append(p) #R1=[12]
		if n==2:
			print(*R1)
			continue
		N2=N1.copy()
		N2.remove(p) #N2=[345]
		for s in N2: #3번째 원소
			R2=R1.copy()
			R2.append(s) #R2=[123]    #❤️R2=[124]
			if n==3:
				print(*R2)
				continue
			N3=N2.copy()
			N3.remove(s) #N3=[45]    #❤️N3=[35]
			for q in N3: #4번째 원소
				R3=R2.copy()
				R3.append(q) #R3=[1234] #⭐R3=[1235]
				if n==4:
					print(*R3)
					continue
				N4=N3.copy()
				N4.remove(q) #N4=[5]    #⭐N4=[4]
				for o in N4: #5번째 원소
					R4=R3.copy()
					R4.append(o) #R5[12345] #⭐R5=[12354]
					if n==5:
						print(*R4) #[12345]->⭐   [12354]->❤️
						continue
					N5=N4.copy()
					N5.remove(o)
					for w in N5: #6번째 원소
						R5=R4.copy()
						R5.append(o) 
						if n==6:
							print(*R5)
							continue
						N6=N5.copy()
						N6.remove(w)
						for x in N6: #7번째 원소
							R6=R5.copy()
							R6.append(o) 
							if n==7:
								print(*R6) 
								continue
							N7=N6.copy()
							N7.remove(o)
							for y in N7: #8번째 원소
								R7=R6.copy()
								R7.append(o) 
								if n==8:
									print(*R7) 


'''
