def calc_mode(number_list):
    count_result = 0
    result = 0
    for i in number_list:
        count = number_list.count(i)
        if count > count_result:
            result = i
            count_result = count
        elif count == count_result:
            result = max(i, result)
    return result

case_size = int(input())
for case in range(1, case_size + 1):
    N = int(input())
    score_list = list(map(int, input().split()))
    mode = calc_mode(score_list)
    print(f'#{case} {mode}')
