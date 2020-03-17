def calc_range(x, length, arr):
    sum_array = [0]
    for i in range(x):
        if i == 0:
            sum_array.append(arr[i])
        else:
            sum_array.append(sum_array[-1] + arr[i])

    max_sum = 0
    min_sum = sum_array[length] - sum_array[0]
    for i in range(x - length + 1):
        prefix_sum = sum_array[i+length] - sum_array[i]
        if prefix_sum > max_sum:
            max_sum = prefix_sum
        elif prefix_sum < min_sum:
            min_sum = prefix_sum

    return max_sum - min_sum

case_size = int(input())
for case in range(1, case_size + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    result = calc_range(N, M, A)
    print(f'#{case} {result}')
