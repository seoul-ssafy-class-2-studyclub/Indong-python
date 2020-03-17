def m_sort(start, end):
    global N
    if start + 1 == end:
        return [arr[start]]
    mid = (start + end) // 2
    l = m_sort(start, mid)
    r = m_sort(mid, end)
    return merge(l, r)


def merge(left, right):
    global cnt
    if left[-1] > right[-1]:
        cnt += 1
    i = 0
    j = 0
    sorted_list = []
    len_l = len(left)
    len_r = len(right)
    while i < len_l and j < len_r:
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    if i < len_l:
        sorted_list += left[i:]
    else:
        sorted_list += right[j:]
    
    return sorted_list


for case in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    res = m_sort(0, N)
    print(f'#{case} {res[N//2]} {cnt}')
