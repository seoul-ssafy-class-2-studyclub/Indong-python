def add_path(cards, N):
    temp = cards.split('-')
    m = N // 2
    path = []

    for x in range(N):
        temp = temp[:]
        if x > m:
            x = N - x
        for i in range(x):
            temp[m-x+(2*i)], temp[m-x+(2*i)+1] = temp[m-x+(2*i)+1], temp[m-x+(2*i)]
        path.append('-'.join(temp))
    adj[cards] = path
    return path


def bfs(queue):
    for i in range(len(queue)):
        node = queue.pop(0)
        if node not in adj:
            queue += add_path(node, N)
        else:
            queue += adj[node]
    queue = list(set(queue))
    return queue


for case in range(1, int(input()) + 1):
    N = int(input())
    cards = list(map(int, input().split()))
    result = '-'.join(map(str, sorted(cards)))
    rev_result = '-'.join(map(str, sorted(cards, reverse=True)))
    start = '-'.join(map(str, cards))
    if start == result or start == rev_result:
        print(f'#{case} 0')
        continue

    adj = dict()
    queue = [start]
    can_shu = False
    cnt = 0
    
    for i in range(5):
        queue = bfs(queue)
        cnt += 1
        if result in queue or rev_result in queue:
            can_shu = True
            break
    if not can_shu:
        cnt = -1
    
    print(f'#{case} {cnt}')
