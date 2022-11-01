
'''import sys

E=sys.stdin.readline().strip()

LE=list(E)
for i in range(1,len(LE)):
    if LE[i]=='0' and LE[i-1]!='0' and LE[i-1]!='+' and LE[i-1]!='-':
        LE[i]='*'
    elif LE[i]=='0' and LE[i-1]=='*':
        LE[i]='*'
    
RE="".join(LE)
RE=RE.replace('0','')
RE=RE.replace('*','0')

print(RE)
Pflag=False
I=0
newE=RE
for i in range(len(RE)):
    newi=i+I
    #rint('newE길이 : ',len(newE))
    #print('newi :',newi)
    if newE[newi]=='-' and Pflag==False:
        newE=RE[:newi+1]+'('+RE[newi+1:]
        Pflag=True
        I+=1
        print(newE)
    elif newE[newi]=='-' and Pflag==True:
        newE=newE[:newi]+')'+newE[newi]+'('+newE[newi+1]
        I+=2
        print(newE)
    if i==len(RE)-1 and Pflag==True:
        newE=newE+')'
        print(newE)

print(eval(newE))

'''

import sys
import re

E=sys.stdin.readline().strip()

#print('E :',E)

num=[int(s) for s in re.split('[+-]',E) if s.isdigit()]
#print(num)
i=0
RE=str(num[i])
for e in E:
    if e=='+' or e=='-':
        i+=1
        RE+=e+str(num[i])
        #print(RE)

Pflag=False
I=0
newE=RE
for i in range(len(RE)):
    newi=i+I
    #rint('newE길이 : ',len(newE))
    #print('newi :',newi)
    if newE[newi]=='-' and Pflag==False:
        newE=RE[:newi+1]+'('+RE[newi+1:]
        Pflag=True
        I+=1
        print(newE)
    elif newE[newi]=='-' and Pflag==True:
        newE=newE[:newi]+')'+newE[newi]+'('+newE[newi+1:]
        I+=2
        print(newE)
    if i==len(RE)-1 and Pflag==True:
        newE=newE+')'
        print(newE)

print(eval(newE))

