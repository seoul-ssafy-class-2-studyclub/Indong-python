for case in range(1, 11):
    N = int(input())
    pw = list(map(int, input().split()))
    i = 1
    while not (0 in pw):
        ele = pw.pop(0) - i
        if ele <= 0:
            ele = 0
        pw.append(ele)
        i += 1
        if i > 5:
            i = 1
    str_pw = ' '.join(map(str, pw))
    print(f'#{case} {str_pw}')
