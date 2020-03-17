def zigzag(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return zigzag(n-1) - n
    else:
        return zigzag(n-1) + n

case_size = int(input())
for case in range(1, case_size + 1):
    number = int(input())
    result = zigzag(number)
    print(f'#{case} {result}')
    