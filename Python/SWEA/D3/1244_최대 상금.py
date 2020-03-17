from collections import deque, defaultdict

def add_path(money):
    new = money
    m_list = []
    for i in range(size):
        m_list.insert(0, new % 10)
        new //= 10
    for i in range(size - 1, -1, -1):
        x = m_list[-1-i]
        for j in range(i - 1, -1, -1):
            if i == j:
                continue
            y = m_list[-1-j]
            temp = money - (x * (10 ** i)) + (y * (10 ** i)) - (y * (10 ** j)) + (x * (10 ** j))
            if temp not in adj[money]:
                adj[money].append(temp)
 

for case in range(1, int(input()) + 1):
    M, C = map(int, input().split())
    chk = [i for i in str(M)]
    size = len(chk)
    adj = defaultdict(lambda: [])
    queue = deque()
    queue.append(M)
    overlap = False
    if size != len(set(chk)):
        overlap = True
 
    max_prize = int(''.join(sorted(chk, reverse=True)))
    for i in range(C):
        for j in range(len(queue)):
            node = queue.popleft()
            if not adj[node]:
                add_path(node)
            queue.extend(adj[node])
        queue = deque(list(set(queue)))
        if max_prize in queue and ((C - i) % 2 or overlap):
            break
 
    print(f'#{case} {max(queue)}')
