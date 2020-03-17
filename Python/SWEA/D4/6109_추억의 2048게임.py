from collections import deque

def move_v(c):
    for i in range(N):
        queue = deque()
        for j in range(N):
            if board[j][i]:
                queue.append(board[j][i])
                board[j][i] = 0
        if c == 'up':
            idx = 0
            while queue:
                nxt = queue.popleft()
                if board[idx][i] == 0:
                    board[idx][i] = nxt
                elif board[idx][i] == nxt:
                    board[idx][i] += nxt
                    idx += 1
                else:
                    idx += 1
                    board[idx][i] = nxt
        else:
            idx = N - 1
            while queue:
                nxt = queue.pop()
                if board[idx][i] == 0:
                    board[idx][i] = nxt
                elif board[idx][i] == nxt:
                    board[idx][i] += nxt
                    idx -= 1
                else:
                    idx -= 1
                    board[idx][i] = nxt


def move_h(c):
    for j in range(N):
        queue = deque()
        for i in range(N):
            if board[j][i]:
                queue.append(board[j][i])
                board[j][i] = 0
        if c == 'left':
            idx = 0
            while queue:
                nxt = queue.popleft()
                if board[j][idx] == 0:
                    board[j][idx] = nxt
                elif board[j][idx] == nxt:
                    board[j][idx] += nxt
                    idx += 1
                else:
                    idx += 1
                    board[j][idx] = nxt
        else:
            idx = N - 1
            while queue:
                nxt = queue.pop()
                if board[j][idx] == 0:
                    board[j][idx] = nxt
                elif board[j][idx] == nxt:
                    board[j][idx] += nxt
                    idx -= 1
                else:
                    idx -= 1
                    board[j][idx] = nxt


for case in range(1, int(input()) + 1):
    N, C = input().split()
    N = int(N)
    board = [list(map(int, input().split())) for _ in range(N)]
    if C == 'up' or C == 'down':
        move_v(C)
    else:
        move_h(C)
    print('#{0}'.format(case))
    for i in range(N):
        print(' '.join(map(str, board[i])))
