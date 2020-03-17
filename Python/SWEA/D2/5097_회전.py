for case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))
    for i in range(M):
        queue.append(queue.pop(0))
    print('#{0} {1}'.format(case, queue[0]))
    