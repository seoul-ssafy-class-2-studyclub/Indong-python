def power(x, n):
    if n == 1:
        return x
    return x * power(x, n-1)

for case in range(10):
    num = int(input())
    y, m = map(int, input().split())
    print(f'#{num} {power(y, m)}')
