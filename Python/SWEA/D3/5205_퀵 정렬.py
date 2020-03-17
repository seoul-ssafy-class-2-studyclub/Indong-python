def q_sort(l, r):
    if l < r:
        pivot = partition(l, r)
        if idx > pivot:
            q_sort(pivot+1, r)
        else:
            q_sort(l, pivot-1)
        
        
def partition(l, r):
    pivot = arr[r]
    i = l - 1
    for j in range(l, r):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i + 1


for case in range(1, int(input()) + 1):
    N = int(input())
    idx = N // 2
    arr = list(map(int, input().split()))
    q_sort(0, N-1)
    print(f'#{case} {arr[N//2]}')
    