case_size = int(input())
for case in range(1, case_size + 1):
    N = int(input())
    ev = 0
    for i in range(N):
        p, x = map(float, input().split())
        ev += p * x
    print(f'#{case} {ev:.6f}')
    