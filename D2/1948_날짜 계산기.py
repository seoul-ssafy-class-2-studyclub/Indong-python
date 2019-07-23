from datetime import datetime, timedelta

case_size = int(input())
for case in range(1, case_size + 1):
    m, i, n, j = map(int, input().split())
    first_day = datetime(2019, m, i)
    second_day = datetime(2019, n, j)
    result = (second_day - first_day).days + 1
    print(f'#{case} {result}')
