import sys

N = int(sys.stdin.readline())

words = []

for _ in range(N):
	words.append(sys.stdin.readline().strip())

# 단어의 길이순으로 words 정렬
words.sort(key=len)

result = 0

for n in range(N):
    prefixFlag=False
    for i in range(n+1,N):
        if words[i].find(words[n])==0 : #접두사
            prefixFlag=True
            break
    if not prefixFlag :
        result += 1

print(result)