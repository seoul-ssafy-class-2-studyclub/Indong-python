for case in range(1, int(input()) + 1):
    str1 = [i for i in input()]
    str2 = [i for i in input()]
    filtering = list(filter(lambda x: x in str1, str2))
    visit = []
    result = 0
    for char in filtering:
        if char in visit:
            continue
        visit.append(char)
        cnt = filtering.count(char)
        if result < cnt:
            result = cnt
    print(f'#{case} {result}')
