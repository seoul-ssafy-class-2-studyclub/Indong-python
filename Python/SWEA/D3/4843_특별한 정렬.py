def special_sort(arr):
    max_num = arr[0]
    min_num = arr[0]
    n = 0
    m = 0
    if len(arr) == 2:
        return arr if arr[0] > arr[1] else [arr[1], arr[0]]
    for i in range(1, len(arr)):
        if arr[i] >= max_num:
            max_num = arr[i]
            n = i
        elif arr[i] <= min_num:
            min_num = arr[i]
            m = i
    arr[0], arr[n] = arr[n], arr[0]
    if m == 0:
        m = n
    arr[1], arr[m] = arr[m], arr[1]
    return arr[:2] + special_sort(arr[2:])


for case in range(1, int(input()) + 1):
    N = int(input())
    unsorted = list(map(int, input().split()))
    result = special_sort(unsorted)[:10]
    print(f'#{case} {" ".join(map(str, result))}')
