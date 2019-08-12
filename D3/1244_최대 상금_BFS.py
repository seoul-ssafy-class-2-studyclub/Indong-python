def add_path(money):
    global adj
    m = [i for i in money]
    for i in range(len(m)):
        for j in range(i + 1, len(m)):
            sw = m[:]
            sw[i], sw[j] = sw[j], sw[i]
            str_sw = ''.join(sw)
            if money not in adj:
                adj[money] = [str_sw]
            elif str_sw not in adj[money]:
                adj[money] += [str_sw]
    
    return adj[money][:]


def bfs(queue):
    global adj
    for i in range(len(queue)):
        node = queue.pop(0)
        if node not in adj:
            queue += add_path(node)
        else:
            queue += adj[node]
    queue = list(set(queue))
    return queue


result_list = []
for case in range(1, int(input()) + 1):
    M, C = input().split()
    M_list = [i for i in M]
    C = int(C)
    adj = dict()
    queue = add_path(M)
    if C == 1:
        result_list.append(max(queue))
    else:
        is_du = False
        if len(M_list) != len(set(M_list)):
            is_du = True
        max_prize = ''.join(sorted(M_list, reverse=True))
        for i in range(1, C):
            queue = bfs(queue)
            max_queue = max(queue)
            if max_prize == max_queue:
                if (C % 2 != 0 and i % 2 == 0) or (C % 2 == 0 and i % 2 != 0) or is_du:
                    break
        result_list.append(max_queue)

for i in range(len(result_list)):
    print(f'#{i + 1} {result_list[i]}')
