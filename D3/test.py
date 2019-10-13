import sys
import collections
input = sys.stdin.readline
# https://www.crocus.co.kr/1164
def find(y, x, named):
    global earth
    q = collections.deque([])
    q.append((y, x))
    earth[y][x] = named
    while q:
        y, x = q.popleft()
        for dy, dx in [(0,1), (0,-1), (1, 0), (-1, 0)]:
            iy = dy + y
            ix = dx + x
            if 0 <= iy < N and 0 <= ix < M and earth[iy][ix] == '#':
                q.append((iy, ix))
                earth[iy][ix] = named


def secondfind(y, x, stop):
    global earth
    tempvisit = [ [False]*M for _ in range(N) ]
    q = collections.deque([])
    q.append((y, x))
    forreturn = []
    while q:
        y, x = q.popleft()
        for dy, dx in [(0,1), (0,-1), (1, 0), (-1, 0)]:
            iy = dy + y
            ix = dx + x
            if 0 <= iy < N and 0 <= ix < M and tempvisit[iy][ix] == False:
                if earth[iy][ix] == '.':
                    tempvisit[iy][ix] = True
                    q.append((iy, ix))
                if earth[iy][ix] != stop and earth[iy][ix] != '.':
                    forreturn.append(earth[iy][ix])
    return forreturn


def getinfo(start):
    global earth
    mychildren = set()
    used = [ [False]*M for _ in range(N) ]
    for i in range(N):
        for j in range(M):
            if earth[i][j] == start and used[i][j] == False:
                used[i][j] = True
                info = secondfind(i, j, start)
                mychildren.update(info)
    return list(mychildren)


N, M = map(int, input().split())
# 최외곽을 0로 바꾼다. -> 우리들의 도착점이다.
earth = [ list(input().strip()) for _ in range(N) ]
landname = [0]
name = 0
for i in range(N):
    for j in range(M):
        if i == 0 or j == 0 or i == N-1 or j == M-1:
            earth[i][j] = 0
        if earth[i][j] == '#':
            name += 1
            landname.append(name)
            find(i, j, name)
adj_list = [ [] for i in range(name+1)]
for one in landname:
    children = getinfo(one)
    adj_list[one].extend(children)
safe = [False] * (name+1)
def solve(i):
    global safe, myparent
    vis = [False] * (name + 1)
    q = collections.deque([])
    q.append(i)
    vis[i] = True
    while q:
        parent = q.popleft()
        for child in adj_list[parent]:
            myparent[child].add(parent)
            if not vis[child]:
                vis[child] = True
                q.append(child)
    return
print(adj_list)
myparent = [set() for _ in range(name + 1)]
solve(0)
print(myparent)
# 모든 네임을 다 도는데, 각 네임이 가진 자식들이 임의로 하나가 지워졌을때 나머지들이
# 서로 서로를 다 잇는 경우, 안전하고
# 그렇지 않는 경우 단절점이라 괜찮지 않다.
# 이부분만 해결하면 될거같은데..
for i in range(name + 1):
    if len(myparent[i]) == 1:
        safe[i] = True
for r in range(N):
    for c in range(M):
        if earth[r][c] == '.':
            continue
        island = earth[r][c]
        if island == 0:
            earth[r][c] = '.'
        elif safe[island]:
            earth[r][c] = 'o'
        elif safe[island] == False:
            earth[r][c] = 'x'
for r in range(N):
    print(''.join(earth[r]))