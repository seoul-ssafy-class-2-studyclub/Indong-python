for case in range(1, int(input()) + 1):
    bbr = ((11 * 24) + 11) * 60 + 11
    D, H, M = map(int, input().split())
    taehyuk = ((D * 24) + H) * 60 + M
    if bbr > taehyuk:
        print(f'#{case} -1')
    else:
        print(f'#{case} {taehyuk - bbr}')
