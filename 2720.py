for _ in range(int(input())):
    C = int(input())
    d = [25, 10, 5, 1]
    result = []
    for n in d:
        result.append(C//n)
        C = C%n
    print(*result)