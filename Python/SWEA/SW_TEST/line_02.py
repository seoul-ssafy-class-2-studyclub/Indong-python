from itertools import permutations
from sys import stdin

input = stdin.readline
num = list(map(int, input().split()))
k = int(input()) - 1

per = list(permutations(num, len(num)))
per.sort()

res = 0
for i in range(len(per[k])):
    res += (10 ** i) * per[k][-1-i]

print(res)
