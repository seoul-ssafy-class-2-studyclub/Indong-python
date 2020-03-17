from pprint import pprint
matrix = [[[[[[] for j in range(21)] 
for k in range(21)]
for l in range(21)]
for m in range(21)]
for i in range(2)]

matrix[0][1][0][0][0].append('00')
matrix[1][0][1][0][0].append('01')
matrix[0][0][0][1][0].append('10')
matrix[1][0][0][0][1].append('11')

queue = [[0, 1, 0, 0, 0], [1, 0, 1, 0, 0], [0, 0, 0, 1, 0], [1, 0, 0, 0, 1]]
def bfs(queue):
    global matrix
    length = len(queue)
    for i in range(length):
        node = queue.pop(0)
        if node[0] == 0:
            next = node[:]
            next[1] += 1
            nxt_num = matrix[next[0]][next[1]][next[2]][next[3]][next[4]]
            if not nxt_num:
                nxt_num.append(1)
            if next not in queue:
                queue.append(next)
            next = node[:]
            next[2] += 1
            next[0] = 1
            nxt_num = matrix[next[0]][next[1]][next[2]][next[3]][next[4]]
            if not nxt_num:
                nxt_num.append(2)
            if next not in queue:
                queue.append(next)
        elif node[0] == 1:
            next = node[:]
            next[3] += 1
            next[0] = 0
            nxt_num = matrix[next[0]][next[1]][next[2]][next[3]][next[4]]
            if not nxt_num:
                nxt_num.append(3)
            if next not in queue:
                queue.append(next)
            next = node[:]
            next[4] += 1
            nxt_num = matrix[next[0]][next[1]][next[2]][next[3]][next[4]]
            if not nxt_num:
                nxt_num.append(4)
            if next not in queue:
                queue.append(next)
    return queue

for i in range(1, 20):
    queue = bfs(queue)

# pprint(matrix)
print(matrix[1][1][1][1][1])


for case in range(1, int(input()) + 1):
    A, B, C, D = map(int, input().split())
    if abs(B - C) > 1 or (B ==0 and C == 0 and A != 0 and D != 0):
        print(f'#{case} impossible')
        continue
    result = ''
    num = matrix[0][A][B][C][D]
    if num:
        if num[0] == 1:
            num = matrix