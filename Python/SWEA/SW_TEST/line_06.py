from sys import stdin

def fill(num, start, wid):
    height = 2 * wid - 1
    if num == 1:
        c = start + wid - 1
        for r in range(height):
            board[r][c] = '#'

    elif num == 2:
        mid = height // 2
        for r in (0, mid, height - 1):
            for c in range(start, start + wid):
                board[r][c] = '#'
        for r, c in ((1, start + wid - 1), (mid + 1, start)):
            for i in range(mid - 1):
                board[r+i][c] = '#'
    
    elif num == 3:
        mid = height // 2
        for r in (0, mid, height - 1):
            for c in range(start, start + wid):
                board[r][c] = '#'
        for r, c in ((1, start + wid - 1), (mid + 1, start + wid - 1)):
            for i in range(mid - 1):
                board[r+i][c] = '#'

    elif num == 4:
        mid = height // 2
        c = start + wid - 1
        for r in range(height):
            board[r][c] = '#'
        for r in range(mid + 1):
            board[r][start] = '#'
        for c in range(1, wid - 1):
            board[mid][start+c] = '#'
    
    elif num == 5:
        mid = height // 2
        for r in (0, mid, height - 1):
            for c in range(start, start + wid):
                board[r][c] = '#'
        for r, c in ((1, start), (mid + 1, start + wid - 1)):
            for i in range(mid - 1):
                board[r+i][c] = '#'

    elif num == 6:
        mid = height // 2
        for r in range(height):
            board[r][start] = '#'
        c = start + wid - 1
        for r in range(mid, height):
            board[r][c] = '#'
        for r in (mid, height - 1):
            for c in range(1, wid - 1):
                board[r][start+c] = '#'
    
    elif num == 7:
        for c in range(wid):
            board[0][start+c] = '#'
        c = start + wid - 1
        for r in range(1, height):
            board[r][c] = '#'
    
    elif num == 8:
        mid = height // 2
        c = start + wid - 1
        for r in range(height):
            board[r][start] = '#'
            board[r][c] = '#'
        for r in (0, mid, height - 1):
            for c in range(1, wid - 1):
                board[r][start+c] = '#'

    elif num == 9:
        mid = height // 2
        c = start + wid - 1
        for r in range(height):
            board[r][c] = '#'
        for r in range(0, mid + 1):
            board[r][start] = '#'
        for r in (0, mid):
            for c in range(1, wid - 1):
                board[r][start+c] = '#'
    
    elif num == 0:
        c = start + wid - 1
        for r in range(height):
            board[r][start] = '#'
            board[r][c] = '#'
        for r in (0, height - 1):
            for c in range(1, wid - 1):
                board[r][start+c] = '#'


input = stdin.readline
numbers = []
N, com = input().split()

all_w = 0
max_w = 0
for _ in range(int(N)):
    width, num = input().split()
    width = int(width)
    if width > max_w:
        max_w = width
    for n in num:
        numbers.append((int(n), width))
        all_w += width

hei = 2 * max_w - 1
all_w += len(numbers) - 1
board = [['.'] * all_w for _ in range(hei)]

start = 0
for num, wid in numbers:
    fill(num, start, wid)
    start += wid
    if start < all_w:
        for r in range(hei):
            board[r][start] = ' '
    start += 1

for i in range(hei):
    print(''.join(board[i]))
    