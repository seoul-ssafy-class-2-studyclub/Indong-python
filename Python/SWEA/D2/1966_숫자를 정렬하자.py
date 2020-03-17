case_size = int(input())
for case in range(1, case_size + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort()
    numbers = ' '.join(map(str, numbers))
    print(f'#{case} {numbers}')
