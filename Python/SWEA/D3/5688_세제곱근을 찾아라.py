import math

for case in range(1, int(input()) + 1):
    N = int(input())
    X = N ** (1.0/3.0)
    if math.isclose(X, round(X, 0)):
        print(f'#{case} {int(round(X, 0))}')
    else:
        print(f'#{case} -1')
