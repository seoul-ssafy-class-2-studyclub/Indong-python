case_size = int(input())
for case in range(1, case_size + 1):
    m, i, n, j = map(int, input().split())
    hour_total = m + n
    minute_total = i + j
    if minute_total >= 60:
        hour_total += 1
        minute_total -= 60
    if hour_total > 12:
        hour_total -= 12
    print(f'#{case} {hour_total} {minute_total}')
