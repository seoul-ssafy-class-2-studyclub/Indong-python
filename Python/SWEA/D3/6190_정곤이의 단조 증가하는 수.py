def monotonic(n):
    a = n % 10
    n = int(n / 10)
    while n != 0:
        if n % 10 > a:
            return False
        else:
            a = n % 10
            n = int(n / 10)
    return True

case_size = int(input())
for case in range(1, case_size + 1):
    N = int(input())
    num_list = list(map(int, input().split()))
    result = -1
    for i in range(N):
        for j in range(i + 1, N):
            mul = num_list[i] * num_list[j]
            if result >= mul:
                continue
            if monotonic(mul):
                result = mul

    print(f'#{case} {result}')
