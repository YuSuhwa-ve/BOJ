alphabet = 'abcdefghijklmnopqrstuvwxyz'
words = input()

L = len(words)
result = 1

for i in range(L-1):
     
    if alphabet.index(words[i]) < alphabet.index(words[i+1]):
        continue
    else:
        result +=1

print(result)