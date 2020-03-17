N = int(input())
result_list = []
if 10 <= N <= 1000:
    for i in range(1, N + 1):
        count = 0
        for j in str(i):
            if j in ['3', '6', '9']:
                count += 1
        if count > 0:
            result_list.append('-' * count)
        else:
            result_list.append(i)
    result = ' '.join(map(str, result_list))
    print(result)
    