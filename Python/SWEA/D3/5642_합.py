def calc_maxsum(arr, N):
    sum_array = [arr[0]]
    max_num = arr[0]
    for i in range(1, N):
        if sum_array[i-1] < 0 or sum_array[i-1] + arr[i] < 0:
            sum_array.append(arr[i])
        else:
            sum_array.append(sum_array[i-1] + arr[i])
        if sum_array[-1] > max_num:
            max_num = sum_array[-1]
    return max_num

        
case_size = int(input())
for case in range(1, case_size + 1):
    length = int(input())
    num_list = list(map(int, input().split()))
    result = calc_maxsum(num_list, length)
    print(f'#{case} {result}')
