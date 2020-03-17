from collections import deque

for case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))
    queue = deque([[idx + 1, p] for idx, p in enumerate(queue)])
    oven = deque()
    for i in range(N):
        oven.append(queue.popleft())
    while len(oven) != 1:
        pizza = oven.popleft()
        pizza[1] //= 2
        if pizza[1] > 0:
            oven.append(pizza)
        elif queue:
            oven.append(queue.popleft())
    print(f'#{case} {oven.pop()[0]}')
