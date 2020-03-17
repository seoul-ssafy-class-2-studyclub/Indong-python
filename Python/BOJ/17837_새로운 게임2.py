from sys import stdin
from pprint import pprint

def find(x):
    if parent[x] == x:
        return x
    return find(parent[x])


def find_leaf(x):
    if child[x] == x:
        return x
    return find_leaf(child[x])


def union(x, y):
    parent[x] = y
    child[y] = x


def partition(x):
    y = parent[x]
    parent[x] = x
    if x != y:
        child[y] = y
        return False
    return True


def red(x, r, c):
    while True: 
        parent[x], child[x] = child[x], parent[x]
        x = parent[x]
        units[x][0] = r
        units[x][1] = c
        if parent[x] == x:
            break
    return x


def calc_rank(x):
    cnt = 1
    x2 = x
    while x != parent[x]:
        x = parent[x]
        cnt += 1
    while x2 != child[x2]:
        x2 = child[x2]
        cnt += 1
    return cnt


dxy = [0, (0, 1), (0, -1), (-1, 0), (1, 0)]
blue = [0, 2, 1, 4, 3]
N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
root = [[0] * N for _ in range(N)]
units = [0]
for i in range(1, K + 1):
    r, c, di = map(int, input().split())
    r -= 1
    c -= 1
    root[r][c] = i
    units.append([r, c, di])
parent = [i for i in range(K + 1)]
child = [i for i in range(K + 1)]
turn = 0

flag = False
while turn <= 1000 and not flag:
    for i in range(1, K + 1):
        r, c, di = units[find(i)]
        di = units[i][2]
        if partition(i):
            root[r][c] = 0
        ri = r + dxy[di][0]
        ci = c + dxy[di][1]
        move = True
        if ri < 0 or ri >= N or ci < 0 or ci >= N or board[ri][ci] == 2:
            di = blue[di]
            ri = r + dxy[di][0]
            ci = c + dxy[di][1]
            if ri < 0 or ri >= N or ci < 0 or ci >= N or board[ri][ci] == 2:
                ri = r
                ci = c
                move = False

        units[i][0] = ri
        units[i][1] = ci
        units[i][2] = di
        
        if move and board[ri][ci] == 1:
            i = red(i, ri, ci)
        
        if root[ri][ci]:
            union(i, find_leaf(root[ri][ci]))
            if calc_rank(i) >= 4:
                flag = True
                break
        else:
            root[ri][ci] = i
    turn += 1
    
if not flag:
    turn = -1
print(turn)