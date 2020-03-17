from collections import deque

delta = [(0, -1), (1, 0), (0, 1), (-1, 0)]
def demolish(board, y, x, brick):
    q = deque()
    q.append((y, x, brick))
    board[y][x] = 0
    while q:
        y, x, size = q.popleft()
        for i in range(size):
            for a, b in delta:
                xi = x + (a * i)
                yi = y + (b * i)
                if 0 <= xi < W and 0 <= yi < H:
                    bomb = board[yi][xi]
                    if bomb:
                        if bomb > 1:
                            q.append((yi, xi, bomb))
                        board[yi][xi] = 0


def fall(board, w, h):
    cnt = 0
    for c in range(w):
        stack = deque()
        for r in range(h):
            brick = board[r][c]
            if brick:
                stack.append(brick)
                cnt += 1
        idx = h - 1
        while stack:
            board[idx][c] = stack.pop()
            idx -= 1
        while idx >= 0:
            board[idx][c] = 0
            idx -= 1
    return cnt


def cycle(board, k=0, cnt=0):
    global min_cnt
    if k == N:
        if min_cnt > cnt:
            min_cnt = cnt
        return True
    
    flag = True
    for i in range(W):
        is_clear = True
        for j in range(H):
            if board[j][i]:
                is_clear = False
                temp = [row[:] for row in board]
                demolish(temp, j, i, temp[j][i])
                break
        if is_clear:
            continue
        flag = False
        cnt = fall(temp, W, H)
        cycle(temp, k+1, cnt)
    
    if flag:
        min_cnt = 0
        return True


for case in range(1, int(input()) + 1):
    N, W, H = map(int, input().split())
    game = [list(map(int, input().split())) for _ in range(H)]
    min_cnt = 999999
    cycle(game)
    print('#{0} {1}'.format(case, min_cnt))
            