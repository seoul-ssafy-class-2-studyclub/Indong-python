def postorder(node=1):
    if tree[node] or node > N:
        return
    left = node * 2
    right = node * 2 + 1
    postorder(left)
    postorder(right)
    tree[node] = tree[left] + tree[right]


for case in range(1, int(input()) + 1):
    N, M, L = map(int, input().split())
    level = 1
    while True:
        if N <= (1 << level) - 1:
            break
        level += 1

    tree = [0] * (2 ** level)
    for i in range(M):
        leaf, value = map(int, input().split())
        tree[leaf] = value

    postorder()
    print(f'#{case} {tree[L]}')
