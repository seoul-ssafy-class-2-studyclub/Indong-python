from collections import deque

dx = [1, 0]
dy = [0, 1]
for case in range(1, int(input()) + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    mat_list = []
    for j in range(N):
        for i in range(N):
            if board[j][i]:
                mat = [0, 0, 0]
                stack = deque()
                stack.append((j, i))
                board[j][i] = -1
                while stack:
                    y, x = queue.pop()
                    for k in delta:
                        xi = x + dx[k]
                        yi = y + dy[k]
                        if 0 <= xi < N and 0 <= yi < N:
                            if board[yi][xi] > 0:
                                stack.append((yi, xi))
                                board[yi][xi] = -1
                            elif board[yi][xi] == 0:
                                print(yi, xi)
                                if k == 0:
                                    mat[2] = abs(i - xi) + 1
                                else:
                                    mat[1] = abs(j - yi) + 1
                                mat[0] = mat[1] * mat[2]
                            if 0 not in mat:
                                stack = []
                                break
                mat_list.append(mat)

    mat_list.sort()
    print(mat_list)
    print(f'#{case} {len(mat_list)}', end='')
    for i in mat_list:
        print(f' {i[1]} {i[2]}', end='')
    print()
