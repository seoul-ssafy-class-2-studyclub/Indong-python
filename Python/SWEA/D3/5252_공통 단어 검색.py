for case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    cnt_dict = dict()
    for a in range(N):
        word = input()
        if word not in cnt_dict:
            cnt_dict[word] = 1
        else:
            cnt_dict[word] += 1
    for b in range(M):
        word = input()
        if word not in cnt_dict:
            cnt_dict[word] = 1
        else:
            cnt_dict[word] += 1
    result = len(list(filter(lambda x: cnt_dict[x] > 1, cnt_dict.keys())))
    print(f'#{case} {result}')
    