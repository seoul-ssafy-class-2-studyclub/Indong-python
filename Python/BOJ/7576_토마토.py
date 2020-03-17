import sys
from collections import deque

dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def main():
    tomatoes = deque()
    for r in range(N):
        for c in range(M):
            if warehouse[r][c] == 1:
                tomatoes.append((r, c))
    
    res = -1
    while tomatoes:
        for i in range(len(tomatoes)):
            r, c = tomatoes.popleft()
            for dy, dx in dxy:
                ri = r + dy
                ci = c + dx
                if 0 <= ri < N and 0 <= ci < M and not warehouse[ri][ci]:
                    warehouse[ri][ci] = 1
                    tomatoes.append((ri, ci))
        res += 1

    for r in range(N):
        for c in range(M):
            if not warehouse[r][c]:
                return -1
    
    return res


M, N = map(int, input().split())
warehouse = [list(map(int, input().split())) for _ in range(N)]

print(main())
