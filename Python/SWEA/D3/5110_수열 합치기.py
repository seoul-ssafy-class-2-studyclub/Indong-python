for case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    length = N
    arr = list(map(int, input().split()))
    for _ in range(M - 1):
        add_list = list(map(int, input().split()))
        num = add_list[0]
        is_exist = False
        for i in range(length):
            if arr[i] > num:
                idx = i
                is_exist = True
                break
        if is_exist:
            arr[idx:0] = add_list
        else:
            arr.extend(add_list)
        length += N
    
    result = ''
    for i in range(10):
        result += ' ' + str(arr[-1-i])  

    print('#{0}{1}'.format(case, result))
