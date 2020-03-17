case_size = int(input())
for case in range(1, case_size + 1):
    numbers = list(map(int, input().split()))
    numbers.remove(max(numbers))
    numbers.remove(min(numbers))
    result = round(sum(numbers) / len(numbers))
    print(f'#{case} {result}')
