'''
P=[]
setR=set(list(range(1,10001)))
i=0
for n in range(1,10000):
    P.append(n+(n//1000)+(n//100)+(n//10)+(n%10))
    while True:
        i+=1
        if P[i-1]>10000:
            break
        P.append(P[i-1]+(P[i-1]//1000)+(P[i-1]//100)+(P[i-1]//10)+(P[i-1]%10))

print(P)
setP=set(P)
R=list(setR-setP)
R.sort()
print(R)
'''
'''
R=list(range(1,10001))

for n in range(0,len(R)):
    P=[]
    i=0
    print("n : ",n)
    print("R[n] : ",R[n])
    P.append(R[n]+(R[n]//1000)+(R[n]//100)+(R[n]//10)+(R[n]%10))
    while True:
        p=P[i]+(P[i]//1000)+(P[i]//100)+(P[i]//10)+(P[i]%10)
        if p>=10000 :
            break
        else :
            P.append(p)
        i+=1
    #print(P)
    R=list(set(R)-set(P))
    print("len(R) :",len(R))

print(R)
'''
'''
P=[]
R=list(range(1,10001))

for n in range(1,10000):
    p=n+(n//1000)+(n//100)+(n//10)+(n%10)
    if p>10000 :
        break
    else :
        P.append(p)

setP=set(P)
setR=set(R)
setA=setR-setP
A=list(setA)
A.sort()
print(A)
'''


R = list(range(1, 10001))
P = []
for n in R :
    for p in str(n):
        n+=int(p)
    if n <= 10000:   
        P.append(n)  


setP=set(P)
setR=set(R)
setA=setR-setP
A=list(setA)
A.sort()

for a in A:
    print(a)


'''
numbers = list(range(1, 10_001))
remove_list = []  # 이후에 삭제할 숫자 list
for num in numbers :
    for n in str(num):
        num += int(n)  # 생성자가 있는 숫자
    if num > 10_000:
        break
    else :
        remove_list.append(num)  # append: 리스트에 요소를 추가할 때

for remove_num in set(remove_list) :  # set 으로 중복값 제거
    numbers.remove(remove_num)

for self_num in numbers :  # 생성자가 있는 숫자를 삭제한 리스트
    print(self_num)





P=[]
R=list(range(1,10001))

for n in range(1,10000):
    p=n+(n//10000)+(n//1000)+(n//100)+(n//10)+(n%10)
    if p>10000 :
        break
    else :
        P.append(p)

setP=set(P)
setR=set(R)
setA=setR-setP
A=list(setA)
A.sort()
for a in A:
    print(a)
    '''
