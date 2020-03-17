def inorder(node=1):
    left = node * 2
    right = node * 2 + 1
    if left <= N:
        inorder(left)
    print(tree[node], end='')
    if right <= N:
        inorder(right)


for case in range(1, 11):
    N = int(input())
    tree = [0] * (N + 1)
    for i in range(N):
        word = list(input().split())
        tree[int(word[0])] = word[1]

    print(f'#{case} ', end='')
    inorder()
    print()