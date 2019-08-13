for case in range(1, int(input()) + 1):
    A, B, C = map(int, input().split())
    X = C // A
    Y = C // B
    print(f'#{case} {max(X, Y)}')
    