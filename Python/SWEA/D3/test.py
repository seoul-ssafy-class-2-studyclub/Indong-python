import sys
from collections import deque
sys.setrecursionlimit(10**7)

def bfs(cur):
    pacific[r][c] = num
    queue = deque()
    queue.append((r, c))
    while queue:
        y, x = queue.popleft()
        for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            yi = y + dy
            xi = x + dx
            if 0 <= yi < N and 0 <= xi < M:
                nxt = pacific[yi][xi]
                if pacific[yi][xi] == cur:
                    queue.append((yi, xi))
                    pacific[yi][xi] = num
                elif nxt != '#' and nxt != '.' and nxt != num:
                    if con.get(nxt) == num:
                        continue
                    adj[num] += [nxt]
                    adj[nxt] += [num]
                    con[num] = num
                    con[nxt] = num


def init():
    for i in range(num):
        con[i] = 0


def findCurVertex(now):
    global order
    discovered[now] = order
    order += 1
    stack.append(now)
    ret = discovered[now]
    for nxt in adj[now]:
        if not discovered[nxt]:
            subtree = findCurVertex(nxt)
            if is_island[now] and subtree >= discovered[now]:
                ap[now] = True
                while stack and stack[-1] != now:
                    con[stack.pop()] = 1
            stack.append(now)
            ret = min(ret, subtree)
        else:
            ret = min(ret, discovered[nxt])
        
    return ret

input = sys.stdin.readline
N, M = map(int, input().split())
pacific = [list(input().strip()) for _ in range(N)]
adj = [[]]
con = {}
num = 1
is_island = [False]
for r in range(N):
    for c in range(M):
        if pacific[r][c] == '#' or pacific[r][c] == '.':
            if pacific[r][c] == '#':
                is_island += [True]
            else:
                is_island += [False]
            adj += [[]]
            bfs(pacific[r][c])
            num += 1

is_sum = [0] * num
discovered = [False] * num
ap = [False] * num
stack = deque()
order = 1

init()
findCurVertex(1)

for r in range(N):
    for c in range(M):
        num = pacific[r][c]
        if not is_island[num]:
            pacific[r][c] = '.'
        elif con[num] and discovered[num] != 1:
            pacific[r][c] = 'X'
        else:
            pacific[r][c] = 'O'
    print(''.join(pacific[r]))
