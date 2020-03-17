def bi_search(start, end, page, count=0):
    l = start
    r = end
    c = int((l + r) / 2)
    cnt = count + 1
    if page == c:
        return cnt
    elif page < c:
        return bi_search(l, c, page, cnt)
    else:
        return bi_search(c, r, page, cnt)

for case in range(1, int(input()) + 1):
    P, A, B = map(int, input().split())
    cnt_A = bi_search(1, P, A)
    cnt_B = bi_search(1, P, B)
    if cnt_A > cnt_B:
        print(f'#{case} B')
    elif cnt_A < cnt_B:
        print(f'#{case} A')
    else:
        print(f'#{case} 0')
