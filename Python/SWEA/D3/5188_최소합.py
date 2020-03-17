dxy = [(0, 1), (1, 0)]
def move(idx, res):
    global min_sum
    if idx == (N - 1, N - 1):
        if res < min_sum:
            min_sum = res
        return True

    y, x = idx
    for b, a in dxy:
        yi = y + b
        xi = x + a
        if 0 <= yi < N and 0 <= xi < N:
            temp = res + board[yi][xi]
            if temp < min_sum:
                move((yi, xi), temp)

for case in range(1, int(input()) + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 999999999999
    move((0, 0), board[0][0])
    print(f'#{case} {min_sum}')
