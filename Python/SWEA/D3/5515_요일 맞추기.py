days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for case in range(1, int(input()) + 1):
    m, d = map(int, input().split())
    result = (sum(days[:m]) + d + 3) % 7
    print(f'#{case} {result}')
