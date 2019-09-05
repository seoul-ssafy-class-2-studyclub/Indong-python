from pprint import pprint

def block(ls):
    global n, score
    x, y, d = ls
    if bd[x][y] == 1:
        score += 1
        if d < 2:
            d += 2
        elif d == 2:
            d += 3
        elif d == 3:
            d += 1
    elif bd[x][y] == 2:
        score += 1
        if d == 0 :
            d += 1
        elif 1 <= d < 3:
            d += 2
        elif d == 3:
            d += 3
    elif bd[x][y] == 3:
        score += 1
        if d == 0:
            d += 3
        elif d == 1:
            d += 1
        elif d > 1:
            d += 2
    elif bd[x][y] == 4:
        score += 1
        if d == 0 :
            d += 2
        elif d == 1:
            d += 3
        elif d == 2:
            d += 1
        elif d == 3:
            d += 2
    elif bd[x][y] == 5:
        score += 1
        d += 2
    elif bd[x][y] == -1:
        return [1]
    elif bd[x][y] > 5:
        for i in warm:
            if bd[x][y] == i[0]:
                if [x, y] != i[1]:
                    x, y = i[1]
                    break
    elif [x, y] == start[:2]:
        return [1]

    nls = [x, y, d]
    return move(nls)


def wall(ls):
    global n, score
    x, y, d = ls
    if x < 0:
        d = 2
    elif y < 0:
        d = 1
    elif x > n - 1:
        d = 0
    elif y > n - 1:
        d = 3
    nls = [x, y, d]
    score += 1
    nls = move(nls)
    return nls

def move(ls):
    global score, n
    x, y, d = ls
    d %= 4
    dx, dy = dxy[d]
    X = x+dx
    Y = y+dy
    while 0 <= X < n and 0 <= Y < n:
        if [X, Y] == start[:2]:
            return [1]
        elif bd[X][Y] == 0:
            X += dx
            Y += dy
        else :
            break
    nls = [X, Y, d%4]
    return nls


for T in range(int(input())):
    n = int(input())
    warm = []
    bd=[list(map(int, input().split())) for i in range(n)]
    q = []
    dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for x in range(n):
        for y in range(n):
            for d in range(4):
                if bd[x][y] == 0:
                    q.append([x, y, d])
    for x in range(n):
        for y in range(n):
            if bd[x][y] > 5:
                warm.append([bd[x][y], [x, y]])
    rs_set = []
    while q:
        score = 0
        start = q.pop(0)
        # start = [0, 2 ,3]
        use_ls = move(start)
        while True:
            if len(use_ls) == 1:
                break
            elif 0 <= use_ls[0] < n and 0 <= use_ls[1] < n:
                use_ls = block(use_ls)
                if len(use_ls) == 1:
                    break  # 웜홀, 블랙홀 해줘야함
            else :
                use_ls = wall(use_ls)
        rs_set.append(score)
        # print(score, start)
    print('#{}'.format(T+1), max(rs_set))
    