# 연산자를 연산 결과로 대체하며 후위 순회를 진행한다. 
def postorder(node=1):
    if type(tree[node]) == int:
        return tree[node]
    left = postorder(child[node][0])
    right = postorder(child[node][1])
    if tree[node] == '+':
        # 3. 현재 = 1. 왼쪽 _연산자_ 2. 오른쪽
        return left + right
    elif tree[node] == '-':
        return left - right
    elif tree[node] == '*':
        return left * right
    elif tree[node] == '/':
        return left / right
    

for case in range(1, 11):
    N = int(input())
    # tree에 연산자, 수를 저장
    tree = [0] * (N + 1)
    # 자식 노드의 정보를 저장하는 리스트
    child = [[] for _ in range(N + 1)]
    for i in range(N):
        node = list(input().split())
        idx = int(node[0])
        if len(node) == 4:
            tree[idx] = node[1]
            child[idx].extend([int(j) for j in node[2:]])
        else:
            tree[idx] = int(node[1])

    print(f'#{case} {int(postorder(1))}')
