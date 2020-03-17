def puzzle(board, N, K):
    cnt = 0
    for i in range(N):
        stack = []
        length = 0
        for j in range(N):
            if board[i][j]:
                stack.append(1)
                length += 1
            elif not board[i][j]:
                if length == K:
                    cnt += 1
                stack.clear()
                length = 0

        if stack and length == K:
            cnt += 1
            stack.clear()
            length = 0

    return cnt


for case in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    board = []

    for _ in range(N):
        board.append(list(map(int, input().split())))
    result = 0
    result += puzzle(board, N, K) + puzzle(list(zip(*board)), N, K)

    print(f'#{case} {result}')
    