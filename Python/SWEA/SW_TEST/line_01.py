from collections import deque

a, b = map(int, input().strip().split(' '))
mes = deque([int(input()) for _ in range(a)])
con = [0] * b

for i in range(b):
    con[i] = mes.popleft()

while mes:
    cur = mes.popleft()
    idx = 0
    val = 9999
    for i in range(b):
        if con[i] < val:
            val = con[i]
            idx = i
    con[idx] += cur

print(max(con))
