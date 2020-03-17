def insert_node(idx):
    global cur
    left = idx * 2
    right = idx * 2 + 1
    if left <= N:
        insert_node(left)
    tree[idx] = cur
    cur += 1
    if right <= N:
        insert_node(right)


for case in range(1, int(input()) + 1):
    N = int(input())
    tree = [0] * (N + 1)
    cur = 1
    insert_node(1)
    print(f'#{case} {tree[1]} {tree[N//2]}')
