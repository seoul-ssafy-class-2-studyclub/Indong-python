from pprint import pprint
def fill_outline():
    global a, b, x, y
    if b == y:
        if x < a:
            x += 1
            while x != a:
                board[y][x] = 1
                x += 1
        else:
            x -= 1
            while x != a:
                board[y][x] = 1
                x -= 1
    elif a == x:
        if y < b:
            y += 1
            while y != b:
                board[y][x] = 1
                y += 1
        else:
            y -= 1
            while y != b:
                board[y][x] = 1
                y -= 1


def calc_area(arr, n):
    res = 0
    for i in range(n):
        res += (arr[i][0] + arr[i+1][0]) * (arr[i][1] - arr[i+1][1])

    return abs(res) // 2


dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
N = int(input())
board = [[0] * 15 for _ in range(15)]
idx = []
for i in range(N // 5 + 1):
    idx.extend(list(map(int, input().split())))
idx = [(idx[i+1], idx[i]) for i in range(0, N * 2, 2)]

print(idx)
y, x = idx[0]
board[y][x] = []
for b, a in idx[1:]:
    print(b, a)
    board[y][x].append((b, a))
    board[b][a] = [(y, x)]
    fill_outline()

b, a = idx[0]
board[y][x].append((b, a))
board[b][a].append((y, x))
fill_outline()
for i in range(15):
    print(board[i])

for y, x in idx:
    cand = []
    for i in range(2):
        b, a = board[y][x][i]
        if b == y:
            if a < x:
                cand.append(1)
            else:
                cand.append(3)
        elif a == x:
            if b < y:
                cand.append(2)
            else:
                cand.append(0)
    
    for i in range(2):
        dy, dx = dxy[cand[i]]
        yi = y + dy
        xi = x + dx
        if 0 <= yi < 15 and 0 <= xi < 15 and board[yi][xi]:
            if board[yi][xi] == 1:
                if cand[i] == 0 or cand[i] == 2:
                    

