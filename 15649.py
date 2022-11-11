import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().split())

P= permutations(range(1,N+1),M)
for p in P:
    print(*p)

