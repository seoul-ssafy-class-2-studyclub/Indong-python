def prefix_sum(int_num, interval_num, numbers):
    total_list = []
    i = 0
    while i + interval_num <= int_num:
        sum_num = sum(numbers[i:i + interval_num])
        total_list += [sum_num]
        i += 1
    return total_list


case_size = int(input())
result_list = []
try:
    if 1 <= case_size <= 50:
        for j in range(case_size):
            input_int, input_interval = map(int, input().split())
            input_numbers = list(map(int, input().split()))
            if (10 <= input_int <= 100) and (2 <= input_interval <= input_int) and (max(set(input_numbers).union(set(range(1, 10001)))) <= 10000):
                prefix_list = prefix_sum(input_int, input_interval, input_numbers)
                result = max(prefix_list) - min(prefix_list)
                result_list += [result]
            else:
                raise ValueError
    else:
        raise ValueError

    for key, value in enumerate(result_list):
        print("#{0} {1}".format(key + 1, value))

except ValueError:
    print("올바른 수를 입력하세요")
    