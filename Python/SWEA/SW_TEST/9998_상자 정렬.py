import random

def swap5(K, origin, target):
    temp = box[origin[-1]]
    for i in range(K - 2, -1, -1):
        box[target[i]] = box[origin[i]]
    box[target[-1]] = temp
    return True


def arrange():
    vis = [False] * N
    origin = []
    length = 0
    is_arr = True
    for i in range(N):
        if i == box[i] or vis[i]:
            continue
        is_arr = False
        vis[i] = True
        queue = [box[i]]
        path = [i]
        p_l = 1
        while queue and p_l < 5:
            node = queue.pop()
            if node == i:
                break
            if vis[node]:
                path.extend(vis[node])
                p_l += len(vis[node])
                while p_l > 5:
                    path.pop()
                    p_l -= 1
            vis[node] = True
            path.append(node)
            p_l += 1
            queue.append(box[node])
        
        if length < p_l:
            length = p_l
            origin = path[:]
        if p_l == 5:
            break

    if not is_arr:
        target = origin[1:length] + [origin[0]]
        print(origin, target)
        swap5(length, origin, target)
    return is_arr


N = 16
# box = [15, 2, 0, 8, 1, 6, 7, 5, 9, 11, 13, 3, 14, 10, 12, 4]
box = list(range(N))
random.shuffle(box)
print(box)
cnt = 0
is_arr = False
while not is_arr:
    is_arr = arrange()
    if not is_arr:
        cnt += 1

sorted_box = sorted(box)
print(box == sorted_box)
print(cnt)