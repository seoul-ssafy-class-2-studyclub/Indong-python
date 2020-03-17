from sys import stdin, setrecursionlimit
from collections import deque
input = stdin.readline


def find(N):
    odd_vis = [-1] * 500001
    even_vis = [-1] * 500001
    queue = deque()
    queue.append((N, 0))
    if N % 2:
        odd_vis[N] = 0
    else:
        even_vis[N] = 0
    while queue:
        dis, cnt = queue.popleft()
        cnt += 1
        tele, forward, backward = dis * 2, dis + 1, dis - 1
        if tele <= 500000:
            if cnt % 2 and odd_vis[tele] == -1:
                odd_vis[tele] = cnt
                queue.append((tele, cnt))
            elif not cnt % 2 and even_vis[tele] == -1:
                even_vis[tele] = cnt
                queue.append((tele, cnt))
        if forward <= 500000:
            if cnt % 2 and odd_vis[forward] == -1:
                odd_vis[forward] = cnt
                queue.append((forward, cnt))
            elif not cnt % 2 and even_vis[forward] == -1:
                even_vis[forward] = cnt
                queue.append((forward, cnt))
        if 0 <= backward < 500000:
            if cnt % 2 and odd_vis[backward] == -1:
                odd_vis[backward] = cnt
                queue.append((backward, cnt))
            elif not cnt % 2 and even_vis[backward] == -1:
                even_vis[backward] = cnt
                queue.append((backward, cnt))
    
    for i in range(limit):
        if i % 2 and odd_vis[sis[i]] >= 0:
            if i < odd_vis[sis[i]]:
                continue
            return i
        if not i % 2 and even_vis[sis[i]] >= 0:
            if i < even_vis[sis[i]]:
                continue
            return i
    return -1

    
    

N, K = map(int, input().split())
sis = [False] * 1001
i = 0
while K <= 500000:
    sis[i] = K
    i += 1
    K += i
limit = i
    
print(find(N))
