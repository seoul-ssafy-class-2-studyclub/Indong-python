case_size = int(input())
for case in range(1, case_size + 1):
    numbers = list(map(int, input().split()))
    result = [0, 0, 0, 0, 0]
    for i in range(7):
        for j in range(i + 1, 7):
            for k in range(j + 1, 7):
                sum_num = numbers[i] + numbers[j] + numbers[k]
                for l in range(5):
                    if sum_num in result:
                        continue
                    if sum_num > result[l]:
                        result.insert(l, sum_num)
                        result.pop()
                        break
    print(f'#{case} {result[4]}')
