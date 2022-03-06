a = 1000 - int(input())
b = [500, 100, 50, 10, 5, 1]
result = 0
for i in b:
    result += a // i
    a %= i
print(result)