def bi_search(l, r, num, di=0):
    global cnt
    m = (l + r) // 2
    mid = A[m]
    if mid == num:
        cnt += 1
        return True
    if num < mid and (di == 'r' or not di):
        bi_search(l, m-1, num, 'l')
    elif num > mid and (di == 'l' or not di):
        bi_search(m+1, r, num, 'r')

for case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))
    cnt = 0
    for n in B:
        bi_search(0, N-1, n)

    print(f'#{case} {cnt}')
