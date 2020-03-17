from sys import stdin

input = stdin.readline
N = int(input())
seats = list(map(int, input().split()))
vacant = []
people = []

for i in range(N):
    if seats[i]:
        people.append(i)
    else:
        vacant.append(i)

res = 0
for seat in vacant:
    min_dis = 987654321
    for p in people:
        dis = abs(seat - p)
        if dis < min_dis:
            min_dis = dis
    if res < min_dis:
        res = min_dis

print(res)
