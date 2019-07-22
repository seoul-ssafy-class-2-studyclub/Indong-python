case_size = int(input())

result_list = []
try:
    if 1 <= case_size <= 50:
        for case in range(case_size):
            count_list = []
            card_num = int(input())
            numbers = [int(i) for i in input()]
            if (5 <= card_num <= 100) and (max(set(numbers).union(set(range(10))))) <= 10:
                dict_num = {number: numbers.count(number) for number in numbers}
                sorted_list_num = sorted(dict_num.items(), key=lambda x: x[1], reverse=True)
                for j in sorted_list_num:
                    if j[1] >= sorted_list_num[0][1]:
                        count_list.append(j)
                if len(count_list) >= 2:
                    count_list = sorted(dict(count_list).items(), key=lambda x: x[0], reverse=True)
                    result_list += [count_list[0]]
                else:
                    result_list += [count_list[0]]
            else:
                raise ValueError
    else:
        raise ValueError

    for key, value in enumerate(result_list):
        print("#{0} {1} {2}".format(key + 1, value[0], value[1]))

except ValueError:
    print("올바른 수를 입력하세요.")
