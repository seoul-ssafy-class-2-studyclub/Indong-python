for case in range(1, int(input()) + 1):
    N = int(input())
    board = []
    for i in range(N):
        board.append(list(map(int, input())))
    middle = N // 2
    result = 0

    for i in range(middle):
        result += (sum(board[i][middle-i:middle+i+1]) + sum(board[-1-i][middle-i:middle+i+1]))
    result += sum(board[middle])
    
    print(f'#{case} {result}')
