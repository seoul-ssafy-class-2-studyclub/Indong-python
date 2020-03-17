def heappush(value, idx):
    global size, heap
    heap.append(value)
    size += 1
    if size == 2:
        return
    parent = idx // 2
    while heap[parent] > value:
        heap[parent], heap[idx] = heap[idx], heap[parent]
        idx = parent
        parent = idx // 2


def sum_parent(idx):
    parent = idx // 2
    res = 0
    while parent:
        res += heap[parent]
        parent //= 2
    return res


for case in range(1, int(input()) + 1):
    N = int(input())
    heap = [0]
    size = 1
    for num in list(map(int, input().split())):
        heappush(num, size)
    res = sum_parent(N)
    print(f'#{case} {res}')
