from sys import stdin

input = stdin.readline
N = int(input())
toilet = [0] * 151
for _ in range(N):
    go, back = map(int, input().split())
    for i in range(go, back):
        toilet[i] += 1

print(max(toilet))
